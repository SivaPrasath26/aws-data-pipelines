
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
# Define source database and table
database_name = "output_db"
table_name = "amazon_sales_combined"

# Load combined dataset from Glue Catalog
df = spark.table(f"{database_name}.{table_name}")

print("Schema of source dataset:")
df.printSchema()
from pyspark.sql import SparkSession, DataFrame

def drop_unwanted_columns(df: DataFrame, cols_to_drop: list) -> DataFrame:
    """
    Drops unwanted columns from a PySpark DataFrame.
    
    Args:
        df (DataFrame): Input Spark DataFrame.
        cols_to_drop (list): List of column names to drop.
    
    Returns:
        DataFrame: Spark DataFrame without the specified columns.
    """
    try:
        existing_cols = set(df.columns)
        drop_candidates = [c for c in cols_to_drop if c in existing_cols]
        
        if not drop_candidates:
            print("[INFO] No matching columns found to drop.")
            return df
        
        df_cleaned = df.drop(*drop_candidates)
        print(f"[SUCCESS] Dropped columns: {drop_candidates}")
        print(f"[INFO] Updated schema: {df_cleaned.columns}")
        return df_cleaned
    
    except Exception as e:
        print(f"[ERROR] Failed to drop columns: {e}")
        return df

# Execute drop
df = drop_unwanted_columns(df, ["image", "link"])

from pyspark.sql import functions as F

def profile_categories(df):
    """
    Profiles main_category and sub_category fields.
    Prints distinct counts, top frequency distributions, and null checks.
    """
    try:
        # Distinct counts
        main_distinct = df.select("main_category").distinct().count()
        sub_distinct = df.select("sub_category").distinct().count()
        
        print(f"[INFO] Distinct main categories: {main_distinct}")
        print(f"[INFO] Distinct sub categories: {sub_distinct}")
        
        # Null or empty checks
        null_main = df.filter((F.col("main_category").isNull()) | (F.trim(F.col("main_category")) == "")).count()
        null_sub = df.filter((F.col("sub_category").isNull()) | (F.trim(F.col("sub_category")) == "")).count()
        
        print(f"[INFO] Null/empty main_category rows: {null_main}")
        print(f"[INFO] Null/empty sub_category rows: {null_sub}")
        
        # Frequency distribution - top 20
        print("\n[TOP MAIN CATEGORIES]")
        df.groupBy("main_category").count().orderBy(F.desc("count")).show(20, truncate=False)
        
        print("\n[TOP SUB CATEGORIES]")
        df.groupBy("sub_category").count().orderBy(F.desc("count")).show(20, truncate=False)
    
    except Exception as e:
        print(f"[ERROR] Failed to profile categories: {e}")

# Execute profiling
profile_categories(df)
from pyspark.sql import functions as F

def category_sanity_check(df):
    try:
        total_rows = df.count()
        print(f"[INFO] Total rows in dataset: {total_rows}")
        
        main_sum = df.groupBy("main_category").count().agg(F.sum("count")).collect()[0][0]
        sub_sum = df.groupBy("sub_category").count().agg(F.sum("count")).collect()[0][0]
        
        print(f"[INFO] Sum of counts by main_category: {main_sum}")
        print(f"[INFO] Sum of counts by sub_category: {sub_sum}")
        
        if main_sum == total_rows:
            print("[SUCCESS] main_category grouping is consistent with total rows.")
        else:
            print("[WARNING] main_category grouping mismatch with total rows.")
        
        if sub_sum == total_rows:
            print("[SUCCESS] sub_category grouping is consistent with total rows.")
        else:
            print("[WARNING] sub_category grouping mismatch with total rows.")
    
    except Exception as e:
        print(f"[ERROR] Failed category sanity check: {e}")

# Execute check
category_sanity_check(df)

def normalize_categories(df):
    """
    Cleans and standardizes category fields for consistency.
    """
    try:
        df_norm = (
            df.withColumn("main_category",
                          F.lower(F.trim(F.regexp_replace("main_category", r'["\']', ""))))
              .withColumn("main_category",
                          F.regexp_replace("main_category", r'\s+', " "))
              .withColumn("sub_category",
                          F.lower(F.trim(F.regexp_replace("sub_category", r'["\']', ""))))
              .withColumn("sub_category",
                          F.regexp_replace("sub_category", r'\s+', " "))
        )
        
        print("[SUCCESS] Category normalization applied.")
        return df_norm
    
    except Exception as e:
        print(f"[ERROR] Failed to normalize categories: {e}")
        return df

# Apply normalization
df_normalized = normalize_categories(df).cache()
df_normalized.count()  # materialize the cache

# Re-profile distinct counts after normalization
main_distinct = df_normalized.select("main_category").distinct().count()
sub_distinct = df_normalized.select("sub_category").distinct().count()

print(f"[INFO] Distinct main categories after normalization: {main_distinct}")
print(f"[INFO] Distinct sub categories after normalization: {sub_distinct}")

# Frequency distribution - top 20
print("\n[TOP MAIN CATEGORIES]")
df_normalized.groupBy("main_category").count().orderBy(F.desc("count")).show(20, truncate=False)
        
print("\n[TOP SUB CATEGORIES]")
df_normalized.groupBy("sub_category").count().orderBy(F.desc("count")).show(20, truncate=False)

from pyspark.sql.functions import lower, trim, col, count

df_normalized.groupBy(trim(lower(col("sub_category"))).alias("sub_category")) \
  .agg(count("*").alias("count")) \
  .filter(col("sub_category").like("%accessories%")) \
  .show(truncate=False, n=100)
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def evaluate_main_category_tokens(df: DataFrame, top_n: int = 50) -> None:
    """
    Deep evaluation of 'main_category' tokens.
    Produces token frequency, document frequency, and doc ratio statistics.

    Args:
        df (DataFrame): Spark DataFrame with normalized 'main_category'.
        top_n (int): number of top/bottom tokens to display.

    Returns:
        None (prints diagnostics).
    """
    try:
        # --- 1. Tokenize ---
        tokens = (
            df.withColumn("main_category_clean",
                          F.trim(F.lower(F.col("main_category"))))
              .withColumn("main_category_clean",
                          F.regexp_replace("main_category_clean", r"[^a-z0-9\s]", " "))
              .withColumn("word", F.explode(F.split("main_category_clean", r"\s+")))
              .filter(F.length("word") > 2)              # drop very short
              .filter(~F.col("word").rlike("^[0-9]+$"))  # drop pure numbers
        )

        # --- 2. Frequency counts ---
        freq_df = tokens.groupBy("word").count().withColumnRenamed("count", "freq")

        # --- 3. Document frequency (distinct categories containing the word) ---
        doc_df = tokens.select("word", "main_category").distinct().groupBy("word").count() \
                       .withColumnRenamed("count", "doc_freq")

        total_docs = df.select("main_category").distinct().count()

        # --- 4. Combine ---
        stats_df = (freq_df.join(doc_df, "word")
                    .withColumn("doc_ratio", F.round(F.col("doc_freq") / F.lit(total_docs), 6))
                    .orderBy(F.desc("freq"))
                   )

        # --- 5. Summary stats ---
        total_tokens = stats_df.count()
        max_freq = stats_df.agg(F.max("freq")).collect()[0][0]
        max_doc_ratio = stats_df.agg(F.max("doc_ratio")).collect()[0][0]

        print(f"[INFO] Total distinct tokens: {total_tokens}")
        print(f"[INFO] Max token frequency: {max_freq}")
        print(f"[INFO] Max document ratio: {max_doc_ratio:.3f}")

        # --- 6. Top-N tokens ---
        print("\n[TOP TOKENS BY FREQUENCY]")
        stats_df.select("word", "freq", "doc_freq", "doc_ratio").show(top_n, truncate=False)

        # --- 7. Rare tokens ---
        print("\n[RARE TOKENS]")
        stats_df.orderBy(F.asc("freq")).select("word", "freq", "doc_freq", "doc_ratio").show(top_n, truncate=False)

        # --- 8. Distribution bins ---
        bins = stats_df.groupBy(
            F.when(F.col("doc_ratio") <= 0.01, "≤1%")
             .when(F.col("doc_ratio") <= 0.05, "1–5%")
             .when(F.col("doc_ratio") <= 0.10, "5–10%")
             .otherwise(">10%")
             .alias("doc_ratio_bin")
        ).count()

        print("\n[DOC RATIO DISTRIBUTION]")
        bins.show(truncate=False)

    except Exception as e:
        print(f"[ERROR] Failed to evaluate main_category tokens: {e}")

evaluate_main_category_tokens(df_normalized, top_n=50)
df_normalized.printSchema()
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def auto_bucket_main_categories(df: DataFrame, top_n_words: int = 50, max_doc_ratio: float = 0.05) -> DataFrame:
    """
    Automatically bucket 'main_category' values using discriminative tokens.

    Steps:
      1. Normalize text (lowercase, trim, remove punctuation).
      2. Tokenize into words.
      3. Compute frequency + document frequency per token.
      4. Drop tokens with doc_ratio > max_doc_ratio (too generic across categories).
      5. Rank remaining tokens by score = freq * idf.
      6. Assign each row a bucket = first matching token, else 'other'.
      7. Print diagnostics.

    Args:
        df (DataFrame): Input Spark DataFrame with 'main_category'.
        top_n_words (int): Number of top tokens to retain as candidate buckets.
        max_doc_ratio (float): Threshold; tokens appearing in more than this fraction
                               of categories are considered non-discriminative.

    Returns:
        DataFrame: Original DF + new column 'main_category_grouped'.
    """
    try:
        # --- 1. Normalize ---
        df_clean = (
            df.withColumn(
                "main_category_clean",
                F.trim(F.lower(F.regexp_replace(F.col("main_category"), r"[^a-z0-9\s]", " ")))
            )
        )

        # --- 2. Tokenize ---
        tokens = (
            df_clean.withColumn("word", F.explode(F.split("main_category_clean", r"\s+")))
            .filter(F.length("word") > 2)              # drop short
            .filter(~F.col("word").rlike("^[0-9]+$"))  # drop numeric
        )

        # --- 3. Frequency + document frequency ---
        freq_df = tokens.groupBy("word").count().withColumnRenamed("count", "freq")
        doc_df = tokens.select("word", "main_category_clean").distinct() \
                       .groupBy("word").count().withColumnRenamed("count", "doc_freq")

        total_docs = df_clean.select("main_category_clean").distinct().count()

        # --- 4. Compute IDF and filter ---
        scored_df = (
            freq_df.join(doc_df, "word")
                   .withColumn("doc_ratio", F.col("doc_freq") / F.lit(total_docs))
                   .withColumn("idf", F.log(F.lit(total_docs) / F.col("doc_freq")))
                   .filter(F.col("doc_ratio") <= max_doc_ratio)
                   .withColumn("score", F.col("freq") * F.col("idf"))
        )

        # --- 5. Select top tokens ---
        top_tokens = [r["word"] for r in scored_df.orderBy(F.desc("score")).limit(top_n_words).collect()]

        # --- 6. Map each row to first matching token ---
        mapped_col = F.lit("other")
        for w in top_tokens:
            mapped_col = F.when(F.col("main_category_clean").rlike(fr"\b{w}\b"), w).otherwise(mapped_col)

        df_grouped = df_clean.withColumn("main_category_grouped", mapped_col)

        # --- 7. Diagnostics ---
        before_count = df.select("main_category").distinct().count()
        after_count = df_grouped.select("main_category_grouped").distinct().count()

        print(f"[INFO] Distinct categories before grouping: {before_count}")
        print(f"[INFO] Distinct categories after grouping: {after_count}")
        print(f"[INFO] Top candidate tokens retained (doc_ratio ≤ {max_doc_ratio}): {top_tokens}")

        discarded = [r["word"] for r in scored_df.orderBy(F.asc("score")).limit(20).collect()]
        print(f"[INFO] Example discarded low-signal tokens: {discarded}")

        return df_grouped

    except Exception as e:
        print(f"[ERROR] Failed in auto_bucket_main_categories: {e}")
        return df

# Run auto bucketing on normalized categories
df_grouped = auto_bucket_main_categories(df_normalized, top_n_words=50, max_doc_ratio=0.05)

# Inspect results
df_grouped.groupBy("main_category_grouped") \
          .count() \
          .orderBy(F.desc("count")) \
          .show(50, truncate=False)
df_grouped.printSchema()
def auto_bucket_sub_categories(df: DataFrame, top_n_words: int = 50, max_doc_ratio: float = 0.05) -> DataFrame:
    """
    Automatically bucket 'main_category' values using discriminative tokens.

    Steps:
      1. Normalize text (lowercase, trim, remove punctuation).
      2. Tokenize into words.
      3. Compute frequency + document frequency per token.
      4. Drop tokens with doc_ratio > max_doc_ratio (too generic across categories).
      5. Rank remaining tokens by score = freq * idf.
      6. Assign each row a bucket = first matching token, else 'other'.
      7. Print diagnostics.

    Args:
        df (DataFrame): Input Spark DataFrame with 'sub_category'.
        top_n_words (int): Number of top tokens to retain as candidate buckets.
        max_doc_ratio (float): Threshold; tokens appearing in more than this fraction
                               of categories are considered non-discriminative.

    Returns:
        DataFrame: Original DF + new column 'main_category_grouped'.
    """
    try:
        # --- 1. Normalize ---
        df_clean = (
            df.withColumn(
                "sub_category_clean",
                F.trim(F.lower(F.regexp_replace(F.col("sub_category"), r"[^a-z0-9\s]", " ")))
            )
        )

        # --- 2. Tokenize ---
        tokens = (
            df_clean.withColumn("word", F.explode(F.split("sub_category_clean", r"\s+")))
            .filter(F.length("word") > 2)              # drop short
            .filter(~F.col("word").rlike("^[0-9]+$"))  # drop numeric
        )

        # --- 3. Frequency + document frequency ---
        freq_df = tokens.groupBy("word").count().withColumnRenamed("count", "freq")
        doc_df = tokens.select("word", "sub_category_clean").distinct() \
                       .groupBy("word").count().withColumnRenamed("count", "doc_freq")

        total_docs = df_clean.select("sub_category_clean").distinct().count()

        # --- 4. Compute IDF and filter ---
        scored_df = (
            freq_df.join(doc_df, "word")
                   .withColumn("doc_ratio", F.col("doc_freq") / F.lit(total_docs))
                   .withColumn("idf", F.log(F.lit(total_docs) / F.col("doc_freq")))
                   .filter(F.col("doc_ratio") <= max_doc_ratio)
                   .withColumn("score", F.col("freq") * F.col("idf"))
        )

        # --- 5. Select top tokens ---
        top_tokens = [r["word"] for r in scored_df.orderBy(F.desc("score")).limit(top_n_words).collect()]

        # --- 6. Map each row to first matching token ---
        mapped_col = F.lit("other")
        for w in top_tokens:
            mapped_col = F.when(F.col("sub_category_clean").rlike(fr"\b{w}\b"), w).otherwise(mapped_col)

        df_grouped = df_clean.withColumn("sub_category_grouped", mapped_col)

        # --- 7. Diagnostics ---
        before_count = df.select("sub_category").distinct().count()
        after_count = df_grouped.select("sub_category_grouped").distinct().count()

        print(f"[INFO] Distinct categories before grouping: {before_count}")
        print(f"[INFO] Distinct categories after grouping: {after_count}")
        print(f"[INFO] Top candidate tokens retained (doc_ratio ≤ {max_doc_ratio}): {top_tokens}")

        discarded = [r["word"] for r in scored_df.orderBy(F.asc("score")).limit(20).collect()]
        print(f"[INFO] Example discarded low-signal tokens: {discarded}")

        return df_grouped

    except Exception as e:
        print(f"[ERROR] Failed in auto_bucket_sub_categories: {e}")
        return df

# Run auto bucketing on normalized categories
df_grouped_sub = auto_bucket_sub_categories(df_grouped, top_n_words=50, max_doc_ratio=0.05)

# Inspect results
df_grouped_sub.groupBy("sub_category_grouped") \
          .count() \
          .orderBy(F.desc("count")) \
          .show(50, truncate=False)
df_grouped_sub.printSchema()
# Execute drop
df_cleaned = drop_unwanted_columns(df_grouped_sub, ["main_category_clean", "sub_category_clean"])

df_cleaned.count()
def profile_grouped_categories(df: DataFrame) -> None:
    """
    Profiles grouped category columns in a Spark DataFrame.
    Prints distinct counts and top frequency distributions for grouped categories.

    Args:
        df (DataFrame): Input DataFrame with grouped category columns.

    Returns:
        None
    """
    try:
        if "main_category_grouped" in df.columns:
            main_distinct = df.select("main_category_grouped").distinct().count()
            print(f"[INFO] Distinct main_category_grouped: {main_distinct}")
            print("\n[TOP MAIN_CATEGORY_GROUPED]")
            df.groupBy("main_category_grouped").count().orderBy(F.desc("count")).show(20, truncate=False)

        if "sub_category_grouped" in df.columns:
            sub_distinct = df.select("sub_category_grouped").distinct().count()
            print(f"[INFO] Distinct sub_category_grouped: {sub_distinct}")
            print("\n[TOP SUB_CATEGORY_GROUPED]")
            df.groupBy("sub_category_grouped").count().orderBy(F.desc("count")).show(20, truncate=False)

    except Exception as e:
        print(f"[ERROR] Failed to profile grouped categories: {e}")

profile_grouped_categories(df_cleaned)

df_cleaned.show(20)
from pyspark.sql import DataFrame, functions as F

def clean_numeric_columns(df: DataFrame, columns: dict, pattern: str = r"[^0-9.\-]") -> DataFrame:
    """
    Cleans and overwrites numeric-like columns using a supplied dtype map.

    Args:
        df (DataFrame): Input DataFrame.
        columns (dict): {column_name: spark_sql_type} to cast to (e.g., {"ratings":"double","no_of_ratings":"long"}).
        pattern (str): Regex of characters to remove before casting (default removes currency, commas, text; keeps digits, '.', '-').

    Returns:
        DataFrame: DataFrame with the specified columns cleaned and cast; nulls coerced to 0 of target type.
    """
    try:
        out = df
        fill_map_numeric = {}
        for col_name, dtype in columns.items():
            if col_name not in out.columns:
                continue
            # strip non-numeric symbols, cast, then normalize null/empty to 0
            cleaned = F.regexp_replace(F.col(col_name), pattern, "")
            casted  = F.when(F.length(cleaned) == 0, None).otherwise(cleaned).cast(dtype)
            out = out.withColumn(col_name, casted)
            # prepare type-appropriate zero for fill
            if dtype.lower().startswith("decimal") or dtype.lower() in {"double","float"}:
                fill_map_numeric[col_name] = 0.0
            else:
                fill_map_numeric[col_name] = 0
        if fill_map_numeric:
            out = out.fillna(fill_map_numeric)
        return out
    except Exception as e:
        print(f"[ERROR] Failed to clean numeric columns: {e}")
        return df

df_cleaned = clean_numeric_columns(
    df_cleaned,
    {
        "ratings": "double",
        "no_of_ratings": "long",
        "discount_price": "double",
        "actual_price": "double",
    }
)

df_cleaned.show(20)
def rename_columns(df: DataFrame, mapping: dict) -> DataFrame:
    """
    Renames columns in a Spark DataFrame.

    Args:
        df (DataFrame): Input DataFrame.
        mapping (dict): Dictionary {old_name: new_name}.

    Returns:
        DataFrame: DataFrame with columns renamed.
    """
    try:
        out = df
        for old, new in mapping.items():
            if old in out.columns:
                out = out.withColumnRenamed(old, new)
        print(f"[SUCCESS] Renamed columns: {mapping}")
        return out
    except Exception as e:
        print(f"[ERROR] Failed to rename columns: {e}")
        return df


# Example:
df_cleaned = rename_columns(
    df_cleaned,
    {"ratings": "ratings_num", 
     "no_of_ratings": "no_of_ratings_num",
     "discount_price": "discount_price_num",
     "actual_price": "actual_price_num"}
)
df_cleaned.printSchema()
def add_discount_features(df: DataFrame) -> DataFrame:
    """
    Adds discount_amount, discount_pct, and is_discounted using *_num columns.
    """
    try:
        out = (
            df.withColumn(
                "discount_amount",
                F.when(
                    (F.col("actual_price_num").isNotNull()) & (F.col("discount_price_num").isNotNull()),
                    F.col("actual_price_num") - F.col("discount_price_num")
                ).otherwise(F.lit(0.0))
            ).withColumn(
                "discount_pct",
F.round(
    F.when(
        F.col("actual_price_num") > 0,
        (F.col("actual_price_num") - F.col("discount_price_num")) / F.col("actual_price_num") * 100.0
    ).otherwise(0.0), 2
).alias("discount_pct")
            ).withColumn(
                "is_discounted",
                (F.col("discount_price_num") < F.col("actual_price_num")) &
                F.col("discount_price_num").isNotNull() &
                F.col("actual_price_num").isNotNull()
            )
        )
        print("[SUCCESS] Discount features added.")
        return out
    except Exception as e:
        print(f"[ERROR] add_discount_features failed: {e}")
        return df

df1 = add_discount_features(df_cleaned)
from pyspark.sql import DataFrame, functions as F

def add_rating_flags(df: DataFrame) -> DataFrame:
    """
    Adds has_rating and has_no_of_ratings boolean flags from ratings_num and no_of_ratings_num.
    """
    try:
        out = (
            df.withColumn("has_rating",        (F.col("ratings_num") > 0))
              .withColumn("has_no_of_ratings", (F.col("no_of_ratings_num") > 0))
        )
        print("[SUCCESS] Rating flags added.")
        return out
    except Exception as e:
        print(f"[ERROR] add_rating_flags failed: {e}")
        return df

df2 = add_rating_flags(df1)
def add_price_bucket(df: DataFrame, low: float = 500.0, mid: float = 2000.0, use_discounted: bool = True) -> DataFrame:
    """
    Adds price_bucket using thresholds: (<low)=low, [low,mid]=mid, >mid=premium.
    Selects effective price from discount_price_num (if enabled and >0) else actual_price_num.
    """
    try:
        eff_price = F.when(F.lit(use_discounted) & (F.col("discount_price_num") > 0),
                           F.col("discount_price_num")) \
                     .otherwise(F.col("actual_price_num"))

        out = df.withColumn(
            "price_bucket",
            F.when(eff_price.isNull() | (eff_price <= 0), F.lit("unknown"))
             .when(eff_price < low,                      F.lit("low"))
             .when(eff_price <= mid,                     F.lit("mid"))
             .otherwise(                                 F.lit("premium"))
        )
        print("[SUCCESS] Price bucket added.")
        return out
    except Exception as e:
        print(f"[ERROR] add_price_bucket failed: {e}")
        return df

df3 = add_price_bucket(df2, low=500.0, mid=2000.0, use_discounted=True)
df3.printSchema()
df3.show()
def add_surrogate_pk(df: DataFrame, cols: list, pk_col: str = "pk") -> DataFrame:
    """
    Adds a deterministic surrogate primary key using SHA-256 over selected columns.

    Args:
        df (DataFrame): Input DataFrame.
        cols (list): Column names to hash (order matters).
        pk_col (str): Name of the output primary key column.

    Returns:
        DataFrame: DataFrame with `pk_col` appended.
    """
    try:
        safe_cols = [F.coalesce(F.col(c).cast("string"), F.lit("")) for c in cols]
        key_str = F.concat_ws("\u0001", *safe_cols)
        return df.withColumn(pk_col, F.sha2(key_str, 256))
    except Exception as e:
        print(f"[ERROR] add_surrogate_pk failed: {e}")
        return df

# Usage on your df_cleaned
# 1) Primary key over stable business fields (adjust as needed)
df_pk = add_surrogate_pk(
    df3,
    cols=[
        "name",
        "main_category_grouped",
        "sub_category_grouped",
        "actual_price_num",
        "discount_price_num"
    ],
    pk_col="pk"
)
df_pk.show()
from typing import List, Optional
def repartition_df(df: DataFrame, partition_cols: List[str], partitions: Optional[int] = None) -> DataFrame:
    """
    Repartitions a DataFrame by given columns.

    Args:
        df (DataFrame): Input DataFrame.
        partition_cols (list[str]): List of column names to cluster/partition by.
        partitions (int | None): Number of partitions; if None, Spark decides.

    Returns:
        DataFrame: Repartitioned DataFrame.
    """
    try:
        for c in partition_cols:
            if c not in df.columns:
                raise ValueError(f"Missing required column: {c}")
        if partitions and partitions > 0:
            return df.repartition(partitions, *[df[c] for c in partition_cols])
        return df.repartition(*[df[c] for c in partition_cols])
    except Exception as e:
        print(f"[ERROR] repartition_df failed: {e}")
        return df
# Define the partition columns
partition_cols = ["main_category_grouped", "sub_category_grouped"]

# Repartition
df_clustered = repartition_df(df_pk, partition_cols, partitions=400)
from awsglue.dynamicframe import DynamicFrame # type: ignore

def write_partitioned_glue(
    df: DataFrame,
    glue_context,
    s3_path: str,
    catalog_db: str,
    catalog_table: str,
    partition_cols: list[str],
) -> None:
    """
    Writes a DataFrame to S3 in Parquet + registers in Glue Catalog, partitioned by given cols.

    Args:
        df (DataFrame): Input DataFrame.
        glue_context: Active GlueContext.
        s3_path (str): S3 prefix (e.g., s3://bucket/prefix/).
        catalog_db (str): Glue database name.
        catalog_table (str): Glue table name.
        partition_cols (list[str]): Partition columns to use.

    Returns:
        None
    """
    try:
        for c in partition_cols:
            if c not in df.columns:
                raise ValueError(f"Partition column '{c}' not in DataFrame.")

        dyf = DynamicFrame.fromDF(df, glue_context, "dyf_out")
        sink = glue_context.getSink(
            path=s3_path,
            connection_type="s3",
            updateBehavior="LOG",
            partitionKeys=partition_cols,
            compression="snappy",
            enableUpdateCatalog=True,
            transformation_ctx="s3_sink",
        )
        sink.setCatalogInfo(catalogDatabase=catalog_db, catalogTableName=catalog_table)
        sink.setFormat("glueparquet")
        sink.writeFrame(dyf)
        print(f"[SUCCESS] Wrote to {s3_path} with partitions {partition_cols}")
    except Exception as e:
        print(f"[ERROR] write_partitioned_glue failed: {e}")

# Write to S3 + Glue
write_partitioned_glue(
    df=df_clustered,
    glue_context=glueContext,
    s3_path="s3://output-de-data/amazon_sales_enriched/",
    catalog_db="output_db",
    catalog_table="amazon_sales_enriched",
    partition_cols=partition_cols
)
df_clustered.printSchema()
job.commit()