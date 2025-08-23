# Phase 3 – ETL & Storage

This phase focuses on transforming, cleaning, and storing data in optimized formats for downstream analytics. You will use AWS Glue (PySpark) to build ETL pipelines, manage schema changes, and write outputs in partitioned and query-efficient storage formats.

## Learning Goals

| Goal                                    | Description                                                   |
| --------------------------------------- | ------------------------------------------------------------- |
| Transform raw data                      | Apply cleansing, joins, aggregations using Glue & PySpark      |
| Optimize storage                        | Write partitioned data into S3 for scalable querying           |
| Learn open data formats                 | Work with Parquet, Delta for efficient analytics               |
| Handle schema evolution                 | Manage changing schemas in Glue tables                        |
| Build reusable ETL pipelines            | Modularize jobs for repeated and automated transformations     |

## Tools Covered

| Tool         | Purpose                                                         |
| ------------ | --------------------------------------------------------------- |
| AWS Glue     | Serverless ETL engine with PySpark for transformations          |
| S3           | Data lake storage with partitioning & optimized file formats    |
| Delta Lake   | Enable ACID transactions, schema evolution, and time travel     |
| Glue Catalog | Centralized metadata store for query engines (Athena, Redshift) |

## Folder Structure

```
phase2_ingestion/
├── glue_jobs
├── s3_partitioning/
├── cloudwatch/
├── glue_catalog/
├── delta_lake
└── README.md
```

Each folder will contain:

* ETL job scripts (PySpark on Glue)
* Notes on best practices (partitioning, compression, schema updates)
* Examples with input/output datasets

## Prerequisites

* IAM roles with Glue, S3, and Catalog permissions
* Output buckets created (`output-de-data/`)
* Basic Glue knowledge (from Phase 2)

## Output of Phase

* Clean, transformed datasets stored in partitioned S3 paths
* Tables registered in Glue Catalog
* Delta tables with schema evolution enabled
* Reusable ETL notebooks for future phases

## Next Phase

You will integrate the transformed data into query engines (Athena/Redshift) and BI tools (QuickSight).
