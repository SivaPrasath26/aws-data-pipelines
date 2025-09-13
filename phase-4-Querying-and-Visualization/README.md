# Phase 4 – Querying & Visualization

This phase focuses on enabling interactive querying and dashboarding. You will use AWS Athena for ad-hoc SQL queries, Glue Catalog for metadata management, and QuickSight to build visual dashboards. The goal is to make curated datasets accessible to analysts and decision-makers.

## Learning Goals

| Goal                               | Description                                                       |
| ---------------------------------- | ----------------------------------------------------------------- |
| Query data with Athena              | Run SQL queries directly on S3 data lake                          |
| Use Glue Catalog                    | Manage schemas and partitions across AWS services                 |
| Build dashboards in QuickSight      | Create interactive visualizations for business users              |
| Optimize queries                    | Reduce Athena costs with partitioning and Parquet                 |
| Secure access                       | Apply IAM and QuickSight row-level security for governance        |

## Tools Covered

| Tool / Service   | Purpose                                                         |
| ---------------- | --------------------------------------------------------------- |
| AWS Athena       | Serverless SQL engine to query S3 data directly                 |
| Glue Catalog     | Central metadata store for schemas and partitions               |
| QuickSight       | Visualization and dashboarding tool for curated datasets        |
| S3               | Source of truth for all data lake storage                       |

## Folder Structure

```
-phase4-querying-and-visualization/
├── athena/
├── glue_catalog/
├── quicksight/
└── README.md
```

Each folder will contain:

* Athena query examples and CTAS workflows
* Glue Catalog notes and schema registration steps
* QuickSight dashboard configuration notes
* Best practices for performance and cost optimization

## Prerequisites

* Phase 3 outputs (partitioned data in S3, Glue tables registered)
* IAM roles with Athena, S3, and QuickSight permissions
* Athena results bucket created (`athena-query-results/`)
* QuickSight account configured for your AWS region

## Output of Phase

* Queryable datasets in Athena backed by Glue Catalog
* Optimized tables (Parquet/partitioned) for low-cost analytics
* QuickSight dashboards for interactive visualization
* Documentation of cost and security practices

## Next Phase

You will extend your pipeline with scheduling, automation, and monitoring. This includes orchestrating ETL + queries with tools like AWS Step Functions, MWAA, or external orchestrators.
