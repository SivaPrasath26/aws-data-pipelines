## AWS Services for Data Engineering – Category-wise Bucketing

---

## 1. **Storage & Object Management**

* **S3** – Scalable object storage for raw and processed data
* **EBS** – Block storage used with EC2 for low-latency workloads
* **EFS** – Shared file system for Linux-based applications

---

## 2. **Compute**

* **EC2** – Virtual servers to run batch jobs or hosted services
* **Lambda** – Event-driven serverless compute
* **ECS/EKS** – Container orchestration (for Dockerized pipelines)

---

## 3. **Ingestion & Streaming**

* **Kinesis Data Streams** – Real-time streaming data capture
* **Kinesis Firehose** – Stream data directly into S3/Redshift
* **AWS DMS** – Migrate/replicate data between DBs
* **AWS Glue Crawlers** – Auto-discover schema and catalog data
* **API Gateway** – REST/HTTP endpoint for external ingestion

---

## 4. **Data Transformation & Processing**

* **AWS Glue (Jobs, Triggers, Workflows)** – Serverless ETL framework
* **Lambda** – Lightweight transformation or filtering logic
* **EMR** – Managed Spark/Hadoop clusters for large-scale processing

---

## 5. **Data Catalog & Governance**

* **Glue Data Catalog** – Central metadata repository
* **Lake Formation** – Secure, govern access to data lakes

---

## 6. **Orchestration & Workflow Automation**

* **Step Functions** – Visual workflow orchestration
* **Glue Workflows** – Native ETL pipeline orchestration
* **EventBridge** – Event-driven automation across services

---

## 7. **Databases (Structured/Relational)**

* **RDS (MySQL/Postgres/SQL Server)** – Managed relational DB
* **Aurora** – High-perf MySQL/PostgreSQL-compatible DB
* **Redshift** – Columnar, MPP warehouse for analytics

---

## 8. **Monitoring & Logging**

* **CloudWatch** – Metrics, logs, alarms
* **CloudTrail** – Audit logs for AWS API activity
* **X-Ray** – Distributed tracing

---

## 9. **Security & IAM**

* **IAM** – Fine-grained access control for services/resources
* **KMS** – Key management for encrypting S3, RDS, etc.
* **Secrets Manager** – Store/manage credentials securely

---

## 10. **Analytics & BI Integration**

* **Athena** – Serverless querying on S3 with SQL
* **QuickSight** – AWS-native BI dashboarding tool
* **OpenSearch (Elasticsearch)** – Search & analytics on logs or semi-structured data

---

## 11. **DevOps & CI/CD (Optional for Data Projects)**

* **CloudFormation** – IaC for provisioning AWS resources
* **CodePipeline / CodeBuild** – Automation of ETL deployment workflows
* **Cloud9** – Browser-based IDE to develop/test Python or Glue jobs
