# Phase 2 – Data Ingestion

This phase focuses on ingesting structured, semi-structured, and streaming data into AWS. You will learn to connect external data sources, APIs, and real-time streams into AWS storage or processing layers.

## Learning Goals

| Goal                                             | Description                             |
| ------------------------------------------------ | --------------------------------------- |
| Understand batch and streaming ingestion methods | Know when to use each                   |
| Capture and move real-time data                  | Use Kinesis Data Streams and Firehose   |
| Ingest database data to AWS                      | Set up and test DMS migration pipelines |
| Ingest data via API                              | Configure API Gateway and Lambda        |
| Auto-discover and catalog data                   | Use Glue Crawlers to detect schema      |

## Tools Covered

| Tool                  | Purpose                                     |
| --------------------- | ------------------------------------------- |
| Kinesis Data Streams  | Real-time event ingestion                   |
| Kinesis Firehose      | Load streaming data into S3/Redshift        |
| AWS Glue Crawlers     | Auto-catalog raw/batch data                 |
| AWS DMS               | Migrate on-prem/remote databases to AWS     |
| API Gateway           | Ingest external API data via HTTP endpoints |
| Lambda (as connector) | Transform or forward data on ingestion      |

## Folder Structure

```
phase2_ingestion/
├── kinesis
├── glue_crawlers/
├── dms_migration/
├── api_gateway
├── lambda/
└── README.md
```

Each folder will contain:

* Service-specific setup notes
* Hands-on implementation (via console, CLI, and Python/Boto3 where possible)
* Sample payloads and data structures

## Prerequisites

* IAM roles with permissions for S3, Lambda, Glue, Kinesis, DMS
* At least one source DB or API to test DMS/API Gateway
* Basic S3 buckets set up (e.g., `raw/`, `staging/`)

## Output of Phase

* Real-time ingestion pipelines (Kinesis + Firehose)
* One working DMS migration task from source DB to S3/Redshift
* Cataloged metadata via Glue Crawlers
* Ingest REST API data via API Gateway + Lambda to S3

## Next Phase

You will move from ingestion to transformation and processing using Glue, PySpark, and EMR.
