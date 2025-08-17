
import sys
from awsglue.transforms import * # type: ignore
from awsglue.utils import getResolvedOptions # type: ignore
from pyspark.context import SparkContext # type: ignore
from awsglue.context import GlueContext # type: ignore
from awsglue.job import Job # type: ignore
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
# Hardcoded for development; will be parameterized later for prod
database_name = "ingestion_db"

# List all tables in the given database
tables = [t.name for t in spark.catalog.listTables(database_name)]

print(f"Database in use: {database_name}")
print(f"Total tables detected: {len(tables)}")
#print(f"Sample table names: {tables[:10]}")
def get_non_empty_tables(db_name):
    valid_tables = []
    empty_count = 0

    for table in spark.catalog.listTables(db_name):
        try:
            df = spark.table(f"{db_name}.{table.name}")
            if df.head(1):  # Check if table has at least one row
                valid_tables.append(table.name)
            else:
                empty_count += 1 # empty table
        except:
            empty_count += 1 # unreadable table

    print(f"Total valid tables with data: {len(valid_tables)}")
    print(f"Total empty or unreadable tables: {empty_count}")
    return valid_tables

valid_tables = get_non_empty_tables(database_name)

def drop_extra_first_col(db_name, valid_tables, standard_col_count=9):
    """
    Drops the first column if table has more than `standard_col_count` columns.
    Returns cleaned DataFrames keyed by table name.
    Prints a summary of columns dropped and count of tables kept unchanged.
    """
    cleaned_tables = {}
    dropped_columns = []
    kept_count = 0

    for table_name in valid_tables:
        try:
            df = spark.table(f"{db_name}.{table_name}")
            cols = df.columns

            if len(cols) > standard_col_count:
                df = df.drop(cols[0])
                dropped_columns.append(f"First column '{cols[0]}' dropped from table '{table_name}'")
            else:
                kept_count += 1

            cleaned_tables[table_name] = df

        except Exception as e:
            print(f"[ERROR] Failed to process table '{table_name}': {e}")

    # Summary
    print(f"\n[COLUMNS DROPPED] Total: {len(dropped_columns)}")
    for msg in dropped_columns:
        print(f"  - {msg}")

    print(f"\n[TABLES UNCHANGED] Total: {kept_count}")

    return cleaned_tables

# Execute
cleaned_dfs = drop_extra_first_col(database_name, valid_tables)

STANDARD_COLUMNS = [
    'name', 'main_category', 'sub_category', 'image', 'link',
    'ratings', 'no_of_ratings', 'discount_price', 'actual_price'
]

def rename_cols_with_column_renamed(cleaned_tables: dict) -> dict:
    """
    Renames columns of each PySpark DataFrame using withColumnRenamed.
    Only renames tables with exactly 9 columns.
    Returns a dictionary of renamed PySpark DataFrames keyed by table name.
    """
    renamed_tables = {}
    renamed_count = 0
    skipped_count = 0

    for table_name, df in cleaned_tables.items():
        try:
            cols = df.columns
            if len(cols) == 9:
                for old_col, new_col in zip(cols, STANDARD_COLUMNS):
                    if old_col != new_col:
                        df = df.withColumnRenamed(old_col, new_col)
                renamed_count += 1
            else:
                skipped_count += 1

            renamed_tables[table_name] = df

        except Exception as e:
            print(f"[ERROR] Failed to rename table '{table_name}': {e}")

    print(f"\n[RENAMED TABLES] Total: {renamed_count}")
    print(f"[SKIPPED TABLES] Total: {skipped_count} (column count != 9)")

    return renamed_tables

# Execute
standardized_dfs = rename_cols_with_column_renamed(cleaned_dfs)

from functools import reduce
from pyspark.sql import DataFrame

def union_all_tables(standardized_tables: dict) -> DataFrame:
    """
    Unions all PySpark DataFrames in the dictionary.
    Assumes all DataFrames have the same schema (9 standardized columns).
    Returns a single combined DataFrame.
    """
    try:
        dfs = list(standardized_tables.values())
        if not dfs:
            print("[WARNING] No tables to union.")
            return None

        combined_df = reduce(DataFrame.unionByName, dfs)
        print(f"[UNION] Combined total tables: {len(dfs)} | Total rows: {combined_df.count()}")
        return combined_df

    except Exception as e:
        print(f"[ERROR] Failed to union tables: {e}")
        return None

# Execute
combined_df = union_all_tables(standardized_dfs)

from awsglue.dynamicframe import DynamicFrame # type: ignore

def write_to_s3_glue(combined_df, s3_path, database, table):
    """
    Writes PySpark DataFrame to S3 in Parquet format using Glue sink
    and updates Glue Data Catalog for QuickSight/Athena.
    """
    try:
        # Convert PySpark DataFrame to Glue DynamicFrame
        dyf = DynamicFrame.fromDF(combined_df, glueContext, "combined_dyf")

        # Configure sink
        sink = glueContext.getSink(
            path=s3_path,
            connection_type="s3",
            updateBehavior="UPDATE_IN_DATABASE",
            partitionKeys=[],   # can add partition columns if needed
            compression="snappy",
            enableUpdateCatalog=True,
            transformation_ctx="s3output",
        )

        # Set Glue Catalog info
        sink.setCatalogInfo(
            catalogDatabase=database,
            catalogTableName=table
        )
        sink.setFormat("glueparquet")

        # Write to S3
        sink.writeFrame(dyf)

        print(f"[SUCCESS] Data written to {s3_path} and registered as {database}.{table}")

    except Exception as e:
        print(f"[ERROR] Failed to write to S3: {e}")


# Example call
write_to_s3_glue(
    combined_df,
    "s3://output-de-data/",
    "output_db",
    "amazon_sales_combined"
)

# def print_table_columns(db_name, valid_tables):
#     counter = 0
#     for table_name in valid_tables:
#         counter += 1
#         df = spark.table(f"{db_name}.{table_name}")
#         print(f"{counter}. Table: {table_name}")
#         print(df.columns)
#         print("-" * 50)
#     print(f"Total tables printed: {counter}")

# # Usage
# print_table_columns(database_name, valid_tables)

# def summarize_table_schemas(db_name):
#     schema_summary = []

#     for idx, table in enumerate(spark.catalog.listTables(db_name), 1):
#         try:
#             df = spark.table(f"{db_name}.{table.name}")
#             cols = df.columns
#             schema_summary.append({
#                 "table_index": idx,
#                 "table_name": table.name,
#                 "num_columns": len(cols),
#                 "columns": cols
#             })
#         except Exception as e:
#             schema_summary.append({
#                 "table_index": idx,
#                 "table_name": table.name,
#                 "num_columns": None,
#                 "columns": f"Error: {e}"
#             })

#     # Print summary
#     for t in schema_summary:
#         print(f"{t['table_index']}. Table: {t['table_name']} | Columns: {t['num_columns']}")
#         print(t['columns'])
#         print('-'*50)

#     # Optional: count unique schemas
#     unique_schemas = {}
#     for t in schema_summary:
#         if t['num_columns'] is not None:
#             cols_tuple = tuple(t['columns'])
#             unique_schemas[cols_tuple] = unique_schemas.get(cols_tuple, 0) + 1

#     print(f"Total unique schemas: {len(unique_schemas)}")
#     for i, (schema, count) in enumerate(unique_schemas.items(), 1):
#         print(f"Schema {i} occurs in {count} table(s): {schema}\n")

#     return schema_summary, unique_schemas

# schema_summary, unique_schemas = summarize_table_schemas(database_name)

# def find_specific_schema_table(db_name, target_schema):
#     for table in spark.catalog.listTables(db_name):
#         try:
#             df = spark.table(f"{db_name}.{table.name}")
#             if tuple(df.columns) == target_schema:
#                 print(f"Table with target schema: {table.name}")
#                 print(f"Columns: {df.columns}")
#                 return table.name, df.columns
#         except Exception as e:
#             continue
#     print("No table found with the target schema.")
#     return None, None

# # Schema 3
# schema_3 = ('col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9')

# table_name, columns = find_specific_schema_table(database_name, schema_3)

# s3output = glueContext.getSink(
#   path="s3://bucket_name/folder_name",
#   connection_type="s3",
#   updateBehavior="UPDATE_IN_DATABASE",
#   partitionKeys=[],
#   compression="snappy",
#   enableUpdateCatalog=True,
#   transformation_ctx="s3output",
# )
# s3output.setCatalogInfo(
#   catalogDatabase="demo", catalogTableName="populations"
# )
# s3output.setFormat("glueparquet")
# s3output.writeFrame(DyF)
job.commit()