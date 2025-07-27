# AWS Glue Crawlers

## What is a Crawler?

An AWS Glue Crawler connects to a data store (like S3, JDBC, etc.), scans the data, infers schema, and populates the Glue Data Catalog with metadata tables. This enables tools like Athena or Glue ETL jobs to query or process the data.

---

## Key Concepts

### 1. **Data Catalog**

* Central metadata repository
* Stores table definitions, schema, partition info

### 2. **Classifier**

* Determines file format: JSON, CSV, Parquet, Avro, etc.
* Built-in or custom classifiers

### 3. **Connection**

* Required for data stores like JDBC, MongoDB
* Not needed for S3-based crawling

### 4. **Crawl Frequency**

* On-demand
* Scheduled (cron-like)

### 5. **Output**

* Creates or updates tables in the Glue Data Catalog
* Can detect schema changes and update definitions

---

## Supported Data Stores

* Amazon S3
* Amazon RDS (MySQL, PostgreSQL, etc.)
* Amazon Redshift
* DynamoDB
* JDBC (external databases)

---

## Workflow

1. **Create Crawler**
2. **Choose Data Source** (S3, RDS, etc.)
3. **Set Classifier** (optional unless default doesn’t work)
4. **Set Output Database in Data Catalog**
5. **Configure IAM Role** (must allow Glue to read source and write to catalog)
6. **Run Crawler** (once or on schedule)
7. **Review Tables** in Glue Catalog

---

## Crawler vs Glue Job

| Feature    | Crawler                     | Glue Job            |
| ---------- | --------------------------- | ------------------- |
| Purpose    | Schema inference + metadata | ETL transformations |
| Output     | Catalog tables              | Transformed data    |
| Language   | No coding required          | PySpark / Scala     |
| Scheduling | Yes                         | Yes                 |

---

## Common Use Cases

* Discover schema of raw logs or JSON in S3
* Enable Athena queries by populating catalog
* Auto-detect partition columns
* Track schema evolution over time

---

## Best Practices

* Store crawled data in dedicated S3 folders
* Separate raw vs transformed tables in Glue Catalog
* Set up crawler logs in CloudWatch
* Use tags to manage environments (dev/test/prod)

---

## Alternatives

* Manual catalog table creation
* Use Glue Jobs to register tables directly
* Use Lake Formation + Glue Catalog for secure, governed data lakes
