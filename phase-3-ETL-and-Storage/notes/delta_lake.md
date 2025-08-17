# Delta Lake Notes

## What is Delta Lake?
- Open-source storage layer that brings **ACID transactions** to data lakes on S3, ADLS, or HDFS.  
- Built on top of **Parquet**, adds a transaction log (`_delta_log`) for reliability.  

## Key Features
- **ACID Transactions** – Ensures consistency during concurrent writes/reads.  
- **Schema Enforcement & Evolution** – Validates incoming data types and allows schema updates.  
- **Time Travel** – Query older versions of data using snapshots.  
- **Upserts & Deletes** – Supports `MERGE`, `UPDATE`, `DELETE` operations.  
- **Scalable Metadata Handling** – Handles large tables more efficiently than Hive metastore.  

## Why Delta Lake over Raw Parquet?
- Parquet alone is immutable, no transactions.  
- Delta Lake enables **incremental loads, deduplication, and SCD Type 2**.  
- Better suited for streaming + batch unified pipelines.  

## Common Commands (PySpark)
```python
# Write data in Delta format
df.write.format("delta").mode("overwrite").save("s3://bucket/delta/sales")

# Read Delta table
df = spark.read.format("delta").load("s3://bucket/delta/sales")

# Time travel (query older version)
df = spark.read.format("delta").option("versionAsOf", 3).load("s3://bucket/delta/sales")

# Merge (Upsert)
from delta.tables import DeltaTable
delta_table = DeltaTable.forPath(spark, "s3://bucket/delta/sales")
delta_table.alias("t").merge(
    source_df.alias("s"),
    "t.id = s.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
```

## Integration
- Works with **AWS Glue, EMR, Databricks, Spark on Kubernetes**.  
- Can be queried using **Athena (via Delta Athena connector)**.  

## Best Practices
- Compact small files using **OPTIMIZE** or Spark `repartition()`.  
- Use partitioning wisely (e.g., `year`, `month`, not high-cardinality IDs).  
- Periodically **VACUUM** old snapshots to manage storage.  
- Enable **checkpointing** for faster reads in large tables.  

## Hands-On Practice
1. Convert existing Parquet dataset into **Delta Lake**.  
2. Run **MERGE** to implement incremental updates.  
3. Test **time travel queries**.  
4. Compare Athena scan size for **Parquet vs Delta**. 