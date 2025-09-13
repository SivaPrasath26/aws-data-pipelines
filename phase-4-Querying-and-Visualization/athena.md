# AWS Athena

Amazon Athena is a serverless query service for analyzing data in **Amazon S3** using standard SQL. It requires no infrastructure setup and charges per TB scanned.

---

## Key Concepts

- **Serverless**: No cluster setup required.
- **Data Source**: Reads directly from S3.
- **Schema**: Managed in Glue Data Catalog or Athena’s internal catalog.
- **Output**: Query results are written back to S3.
- **Cost**: Billed per TB of data scanned, so file format and partitioning matter.

---

## Setup

1. Store raw data in **S3**.
2. Configure **IAM permissions**:
   - `AmazonAthenaFullAccess`
   - `AmazonS3ReadOnlyAccess` (input data)
   - `AmazonS3FullAccess` or scoped permissions (Athena results bucket)
3. Create a dedicated bucket/folder for Athena query results:  
   `s3://my-bucket/athena-results/`

---

## Glue Integration

- Glue Catalog stores table definitions (schemas, partitions, locations).
- Athena queries use these tables like a database.
- Partitioning in Glue reduces scan cost (e.g., partition by `year`, `month`).

---

## Typical Workflow

1. Upload CSV/Parquet/ORC files to S3.
2. Define an **external table** in Athena linked to the S3 location.
3. Run queries directly against the table.
4. Use **CTAS (Create Table As Select)** for optimized storage in Parquet/ORC.
5. Expose data to BI tools (e.g., QuickSight).

---

## Best Practices

- **Use columnar formats** (Parquet or ORC) → faster queries, lower cost.
- **Partition wisely** → by date, region, or other filters.
- **Compress files** → GZIP, Snappy.
- **Prune columns** → only select what you need.
- **Store results separately** from raw data.

---

## Cost Management

- Athena scans the entire file unless optimized.
- Partition + columnar storage reduces scan size drastically.
- Use CTAS queries to create curated, optimized datasets in S3.

---

## Integrations

- **QuickSight** → dashboards on Athena queries.
- **Glue** → schema and partition management.
- **S3** → single source of truth for data lake.
