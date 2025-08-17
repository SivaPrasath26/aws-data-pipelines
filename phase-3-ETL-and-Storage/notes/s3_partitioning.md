## S3 Partitioning

## What is Partitioning?

Partitioning in Amazon S3 is the technique of organizing large datasets into smaller, manageable subsets based on one or more keys (e.g., `year`, `month`, `day`, `region`). Each partition is stored as a separate prefix (folder) in S3.

---

## Why Partition Data?

* **Performance** – Reduces the amount of data scanned in Athena, Glue, and Redshift Spectrum.
* **Cost Efficiency** – You pay only for the data scanned, not the entire dataset.
* **Manageability** – Easier data lifecycle management and incremental updates.

---

## Partitioning Strategy

### 1. **Time-based Partitioning**
* Common for logs, transactions, clickstreams.
* Example path:  
  `s3://bucket/events/year=2025/month=08/day=17/`

### 2. **Category-based Partitioning**
* Useful for customer, region, product.
* Example path:  
  `s3://bucket/sales/region=APAC/`

### 3. **Hybrid Partitioning**
* Combine time and category for better granularity.
* Example path:  
  `s3://bucket/orders/region=NA/year=2025/month=08/`

---

## Best Practices

* Choose partition keys with high selectivity (e.g., date, region).
* Avoid over-partitioning (too many small files).
* Use **Parquet/ORC** for efficient columnar storage.
* Register partitions in **Glue Data Catalog** for query engines.
* Automate partition discovery with **Glue Crawlers** or **MSCK REPAIR TABLE** in Athena.

---

## Example: Glue Catalog Table with Partitions

```sql
CREATE EXTERNAL TABLE sales (
    order_id STRING,
    amount DECIMAL(10,2)
)
PARTITIONED BY (year STRING, month STRING, day STRING)
STORED AS PARQUET
LOCATION 's3://bucket/sales/';
```
## Adding Partitions

Partitions must be added explicitly:

```sql
ALTER TABLE sales ADD PARTITION (year='2025', month='08', day='17')
LOCATION 's3://bucket/sales/year=2025/month=08/day=17/';
```

## Common Challenges

- **Too many small files** – Merge using Glue jobs or Spark `coalesce()` / `repartition()`.  
- **Missing partitions in Athena/Glue** – Run repair command or enable crawler.  
- **Skewed partitions** – Avoid keys with high cardinality (e.g., `customer_id`).  

## Tools for Partition Management

- **AWS Glue Crawlers** – Auto-detect partitions.  
- **Hive-compatible partitioning** – Ensures query engines like Athena work out of the box.  
- **Partition Projection** – Define partition scheme in Athena without crawling.  

## Hands-On Practice

1. Create a bucket with partitioned data (`year=2025/month=08/day=17`).  
2. Load Parquet data via Glue job into partitioned S3 paths.  
3. Register partitions with Glue Catalog.  
4. Query partitions in Athena and measure data scan size.  
5. Optimize by merging small files.  