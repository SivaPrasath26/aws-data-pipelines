# AWS Glue Jobs

## What are Glue Jobs?

AWS Glue Jobs are managed, serverless data processing tasks that run your ETL/ELT code at scale. You can author jobs in **PySpark (Spark ETL/Streaming)**, **Python Shell**, or **Ray** (for Python-native data/ML workloads). Jobs can be script-based or built visually in **Glue Studio**.

---

## Key Use Cases

* Clean, join, and enrich raw data into analytics-ready datasets
* Incremental (bookmark-based) loads from S3/JDBC sources
* Format conversion (CSV/JSON → Parquet/Delta) and partitioning
* CDC merges into curated tables
* Feature engineering and batch inference (Glue for Ray)

---

## Job Types

* **Spark ETL (PySpark):** Distributed transformations on large data sets
* **Spark Streaming:** Low-latency micro-batch processing from streams
* **Python Shell:** Lightweight single-machine Python tasks, drivers, utilities
* **Ray (Python):** Python-native distributed compute for data/ML (pandas, NumPy, scikit-learn)

> Choose Spark ETL for big data transformations; Python Shell for orchestration/utilities; Ray for Python-first distributed tasks.

---

## Core Components

* **Script**: Your code (PySpark / Python). Stored in S3 or inline.
* **IAM Role**: Runtime permissions for S3, Glue Catalog, logs, JDBC, etc.
* **Connections**: Define network & auth for JDBC/RDS/Redshift (VPC, SG, subnet).
* **Job Parameters / Default Arguments**: Runtime flags (e.g., `--TempDir`, `--job-bookmark-option`, `--additional-python-modules`).
* **DPUs / Worker Type**: Compute capacity and concurrency settings.
* **Glue Data Catalog**: Central metadata for tables; used by Glue, Athena, Redshift Spectrum, QuickSight.
* **Triggers**: Time-based, on-demand, or job-event based; orchestrate multi-job pipelines.

---

## Development Modes

* **Glue Studio (Visual)**: Drag-and-drop ETL, auto-generates code.
* **Script Authoring**: Upload/edit PySpark/Python scripts in S3 or editor.
* **Notebooks**: Interactive authoring in Glue Notebook; convert to job when ready.

---

## Job Lifecycle (Typical)

1. **Author**: Write PySpark in notebook or script repo; test on samples.
2. **Configure**: Set worker type/number, IAM role, default args, retries, timeout.
3. **Run**: On-demand or via triggers; pass runtime params (e.g., dates, paths).
4. **Monitor**: CloudWatch Logs/Metrics; Glue run history; Spark UI.
5. **Publish**: Register outputs in Glue Catalog; validate with Athena/QuickSight.

---

## Default Arguments (Common)

* `--TempDir=s3://…/tmp/` – scratch space for shuffle and bookmarking
* `--job-bookmark-option=job-bookmark-enable|disable|pause`
* `--enable-metrics` and `--enable-continuous-cloudwatch-log`
* `--enable-glue-datacatalog` – use Catalog as Hive metastore
* `--additional-python-modules=pandas==x.x.x,pyarrow==x.x.x` (PyPI libs)
* Custom: `--run_date=2025-08-17`, `--env=prod`, etc.

> Keep dependencies minimal; pin versions for reproducibility.

---

## Starter PySpark Template (GlueContext)

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME", "TempDir", "env"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read from Catalog
source_dyf = glueContext.create_dynamic_frame.from_catalog(
    database="raw_db",
    table_name="orders_csv",
    transformation_ctx="source_dyf"
)

# Transform (DynamicFrame → DataFrame → DynamicFrame)
df = source_dyf.toDF()
# … your PySpark transforms …
df_out = df  # placeholder

dyf_out = DynamicFrame.fromDF(df_out, glueContext, "dyf_out")

# Write to S3 as partitioned Parquet & update Catalog
glueContext.write_dynamic_frame.from_options(
    frame=dyf_out,
    connection_type="s3",
    connection_options={
        "path": "s3://output-de-data/amazon_sales_data/",
        "partitionKeys": ["year", "month"],
    },
    format="glueparquet",
    transformation_ctx="s3sink",
)

job.commit()
```

---

## DynamicFrame vs DataFrame

* **DynamicFrame** is Glue-native (schema on read, tolerant to semi-structured data, mapping, resolveChoice).
* Convert to/from **Spark DataFrame** for flexibility: `dyf.toDF()` and `DynamicFrame.fromDF(df, glueContext, name)`.

---

## Incremental Loads (Job Bookmarks)

* Enable bookmarks to process **new or changed** files only.
* Behavior: `enable` (track processed), `pause` (reuse state but don’t update), `disable` (full scan).
* For JDBC: combine bookmarks with **watermark columns** (e.g., `updated_at`).

**Pattern**

```python
# in default args: --job-bookmark-option=job-bookmark-enable
source_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": ["s3://raw-bucket/path/"],
        "recurse": True
    },
    format="json",
)
```

---

## Storage Formats & Partitioning

* Prefer **Parquet** (columnar, compressed) or **Delta** (ACID, time travel, schema evolution).
* Partition on **low-cardinality, high-selectivity** columns (e.g., `date`, `region`).
* Avoid over-partitioning (too many small files) and under-partitioning (wide scans).

**Write Parquet**

```python
glueContext.write_dynamic_frame.from_options(
    frame=dyf_out,
    connection_type="s3",
    connection_options={"path": "s3://output/...", "partitionKeys": ["dt"]},
    format="glueparquet"
)
```

**Write Delta** (Spark session must include Delta libs)

```python
(df_out
 .write
 .format("delta")
 .mode("append")
 .partitionBy("dt")
 .save("s3://output/.../delta_table"))
```

---

## Schema Evolution

* Use **Glue Crawlers** or explicit schemas to register tables.
* For Parquet: evolve via new columns (nullable) + Catalog updates.
* For Delta: use `merge`, `ALTER TABLE`, and automatic schema evolution (`.option("mergeSchema", "true")`).
* Handle type changes explicitly (cast) to avoid reader failures.

---

## Performance Tuning

* **Input pruning**: specify `paths`, `pushDownPredicate`, and Catalog partitions.
* **Partition sizing**: Use `repartition()` (increase) or `coalesce()` (decrease) to target 128–512 MB output files.
* **Joins**: Broadcast small tables (`broadcast(df)`) and apply selective filters early.
* **Skew**: Salting keys / `skewHint`, or skew join strategies.
* **Caching**: Persist reused DataFrames selectively; unpersist when done.
* **I/O**: Prefer column pruning (`select` only needed columns); compress outputs (Parquet defaults).

---

## Security & Networking

* **IAM**: Least-privilege role for job execution.
* **Encryption**: SSE-S3 or SSE-KMS for S3; KMS for logs/catalog; client-side if required.
* **VPC Access**: Required for JDBC/RDS/Redshift in private subnets; configure **Connections** (subnets + SGs).
* **Secrets**: Store DB creds in **Secrets Manager**; reference from job.

---

## Monitoring & Troubleshooting

* **CloudWatch Logs**: Driver/executor logs; enable continuous logging.
* **CloudWatch Metrics**: DPUs, duration, errors; set alarms.
* **Glue Run History**: Inputs, outputs, bookmark state, error traces.
* **Spark UI**: Stage/task view (enable via job run details link when available).
* **Retries & Timeouts**: Configure max retries and job timeout.

---

## Cost Optimization

* Right-size workers (Standard/G.1X/G.2X) and number of workers.
* Use **bookmarks** to avoid reprocessing.
* Compact small files (e.g., periodic coalesce) and prune inputs.
* Prefer Parquet/Delta over CSV/JSON for downstream efficiency.
* Schedule non-urgent jobs in off-peak windows.

---

## Hands-On Exercises

1. Build a PySpark job that reads CSV from S3, cleans/joins, writes Parquet partitioned by `year/month`, registers in Catalog.
2. Enable **job bookmarks** and re-run with new files—verify only new files are processed.
3. Add a JDBC source (via **Connection** + VPC), load incremental rows by `updated_at` watermark.
4. Convert an existing Parquet dataset to **Delta**, then run an upsert (`merge`).
5. Tune performance: add partition pruning, broadcast a small dimension, and compact output files.

---

## Naming & Repo Hygiene

* Jobs: `etl_<domain>_<dataset>_<layer>` (e.g., `etl_sales_orders_curated`)
* S3: `s3://<org>-<env>-datalake/{raw,staging,curated}/...`
* Catalog DBs: `<env>_<domain>`; Tables: snake\_case; columns: snake\_case
* Version control scripts; promote via dev→test→prod with params.

---

## Resources

* Glue Developer Guide: [https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
* Glue Studio Jobs: [https://docs.aws.amazon.com/glue/latest/ug/etl-jobs-glue-studio.html](https://docs.aws.amazon.com/glue/latest/ug/etl-jobs-glue-studio.html)
* Job Bookmarks: [https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html)
* Using the Data Catalog: [https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)
* Delta Lake on AWS: [https://delta.io/](https://delta.io/)
