# Glue Catalog

Glue Catalog is AWS’s centralized metadata store that enables Athena, Redshift Spectrum, EMR, and other services to query the same S3 data consistently. It stores schema definitions, partitions, and table metadata.

---

## Learning Goals

| Goal                        | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| Understand Glue Catalog     | Learn how schemas and partitions are stored centrally          |
| Register datasets           | Add Phase 3 curated S3 data as Glue tables                     |
| Enable cross-service query  | Make the same tables queryable in Athena and Redshift Spectrum |
| Manage schema evolution     | Handle column additions and type changes over time             |
| Optimize metadata           | Organize partitions and avoid performance bottlenecks          |

---

## Key Concepts

| Concept            | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| Database           | Logical grouping of tables within Glue Catalog                         |
| Table              | Schema definition of data stored in S3 (format, location, partitioning)|
| Partitioning       | Splits large tables into smaller chunks for efficient querying         |
| Schema Evolution   | Ability to handle changes in columns without reloading full datasets   |
| Cross-Service Use  | Catalog tables can be used in Athena, EMR, Redshift Spectrum, etc.     |

---

## Schema Design

- Define schemas that reflect curated S3 datasets (from Phase 3).
- Use **Parquet** or **ORC** formats instead of CSV for efficiency.
- Align column names and types with transformation output.
- Add partition keys like `year`, `month`, `week` to improve query speed.

---

## Partitioning Strategy

- Partition on time-based fields (`year`, `month`) for predictable query filters.
- Avoid high-cardinality columns (e.g., `user_id`) which create too many small partitions.
- Compact small files within partitions to reduce overhead in Athena.

---

## Crawlers and Jobs

- **Glue Crawler**: Automatically infers schema and partitions from S3 paths.
- **ETL Job (PySpark on Glue)**: Provides more control for schema enforcement and evolution.
- Best approach: use Glue jobs to write partitioned Parquet, then run Crawlers for discovery.

---

## Schema Evolution

- Track changes to schemas as data evolves:
  - Adding new columns → supported (they appear as `NULL` in old data).
  - Dropping or renaming columns → breaks compatibility, requires explicit migration.
- Document schema versions in metadata or separate folder.

---

## Best Practices

- **Partition wisely**: Use fields that filter queries frequently.
- **Automate updates**: Schedule crawlers or Glue jobs to refresh Catalog metadata.
- **Monitor query costs**: Athena bills by data scanned, so optimize file formats and partitions.
- **Limit small files**: Compact to 128–256 MB files for performance.
- **Centralize metadata**: Keep all curated tables in one database for easier BI access.

---

## Output of This Module

- Phase 3 curated data registered in Glue Catalog.
- Partitioned tables accessible from Athena, Redshift Spectrum, and EMR.
- Documented schema evolution and partitioning strategy.
- Automated crawler or job for metadata refresh.
