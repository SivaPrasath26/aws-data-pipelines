# AWS Glue Data Catalog

## Overview
- Central metadata repository for all structured and semi-structured data.  
- Stores **table definitions, schema, partition info, and locations in S3**.  
- Fully compatible with Hive Metastore.  

## Key Features
- **Schema Registry** – Keeps track of table/column definitions.  
- **Partition Management** – Tracks partitions for efficient querying.  
- **Integration** – Works with **Athena, Redshift Spectrum, EMR, Glue Jobs**.  
- **Versioning** – Tracks schema changes over time.  

## Common Challenges
- **Schema drift** – Handle evolving data with versioning or schema-on-read.  
- **Stale metadata** – Run crawlers or `MSCK REPAIR TABLE` to refresh.  
- **Access control** – Use Lake Formation for fine-grained permissions.  

## Best Practices
- Organize databases by **domain/project**.  
- Use **Parquet/ORC** formats for tables to reduce Athena scan costs.  
- Automate catalog updates via **Glue Crawlers** or ETL jobs.  
- Apply **naming conventions** for tables and columns.  

## Hands-On Practice
1. Create a Glue Catalog database.  
2. Crawl an S3 bucket to auto-generate schema.  
3. Query data in **Athena** using the catalog.  
4. Add new partitions manually or via crawler.  
5. Integrate catalog tables with **Spark or Redshift Spectrum**.  
