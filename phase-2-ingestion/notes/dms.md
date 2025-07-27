## AWS Database Migration Service (DMS)

## What is AWS DMS?

AWS Database Migration Service (DMS) helps migrate databases to AWS securely and with minimal downtime. You can migrate:

* **Homogeneous** databases (e.g., Oracle to Oracle)
* **Heterogeneous** databases (e.g., SQL Server to Aurora)

DMS supports continuous replication with high availability.

---

## Core Concepts

### 1. **Source and Target Endpoints**

* **Source:** The existing database you're migrating *from*
* **Target:** The AWS database you're migrating *to*
* Supported endpoints include RDS, Aurora, Redshift, S3, DynamoDB, and on-premise DBs

### 2. **Replication Instance**

* AWS-managed EC2 instance running the DMS software
* Responsible for connecting source and target, reading, transforming, and writing data
* Choose instance size based on DB size and throughput

### 3. **Migration Types**

* **Full Load:** All existing data is moved at once
* **CDC (Change Data Capture):** Replicates ongoing changes after full load
* **Full Load + CDC:** Preferred in production for minimal downtime

---

## Supported Databases (Source/Target)

| Source     | Target                           |
| ---------- | -------------------------------- |
| MySQL      | RDS (MySQL, PostgreSQL, MariaDB) |
| Oracle     | Aurora                           |
| SQL Server | Redshift                         |
| PostgreSQL | S3 (CSV, Parquet)                |
| MongoDB    | DynamoDB                         |

---

## Key Features

* No need to install agents on source/target
* Resilient to network failures
* Schema conversion using **AWS SCT** (Schema Conversion Tool) for heterogeneous migrations

---

## Use Cases

* Migrate on-prem DBs to AWS (lift & shift)
* Migrate data between regions or accounts
* Migrate OLTP DBs to analytics platforms (e.g., PostgreSQL to Redshift/S3)
* Consolidate multiple DBs into one

---

## Pricing

* Based on replication instance hours + storage + data transfer
* Replication instance pricing similar to EC2

---

## High-Level Steps

1. **Create Replication Instance**
2. **Configure Source and Target Endpoints**
3. **Test Endpoint Connections**
4. **Create Migration Task**

   * Choose migration type (Full load / CDC / Both)
   * Define table mappings and filters
5. **Start Task and Monitor in Console**

---

## Monitoring

* Use **CloudWatch** metrics for replication instance (CPU, latency, lag)
* Task logs available in **DMS Console**
* Alerts can be configured via SNS

---

## Limitations

* Schema migration is not automatic for heterogeneous DBs (use AWS SCT)
* No CDC for all engines (e.g., CDC not supported for SQLite)
* Some data types may not be migrated as-is (e.g., spatial data, user-defined types)

---

## Focus Points

* Understand replication instance, task creation, endpoints
* Know differences between full load and CDC
* Identify when to use DMS vs SCT
* Real-world scenarios: OLTP to S3, Oracle to Aurora

---

## Hands-On Ideas

* Migrate sample MySQL RDS to S3 using Full Load
* Migrate PostgreSQL to Aurora with Full Load + CDC
* Setup DMS with CloudWatch alarms

---

## Resources

* [AWS DMS Docs](https://docs.aws.amazon.com/dms/index.html)
* [AWS SCT Overview](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html)
