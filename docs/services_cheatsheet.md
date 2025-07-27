## AWS Services for Data Engineering – Category-wise Bucketing

---

## 1. **Storage & Object Management**

* [**S3**](https://aws.amazon.com/s3/) – Scalable object storage for raw and processed data
* [**EBS**](https://aws.amazon.com/ebs/) – Block storage used with EC2 for low-latency workloads
* [**EFS**](https://aws.amazon.com/efs/) – Shared file system for Linux-based applications

---

## 2. **Compute**

* [**EC2**](https://aws.amazon.com/ec2/) – Virtual servers to run batch jobs or hosted services
* [**Lambda**](https://aws.amazon.com/lambda/) – Event-driven serverless compute
* [**ECS**](https://aws.amazon.com/ecs/) / [**EKS**](https://aws.amazon.com/eks/) – Container orchestration (for Dockerized pipelines)

---

## 3. **Ingestion & Streaming**

* [**Kinesis Data Streams**](https://aws.amazon.com/kinesis/data-streams/) – Real-time streaming data capture
* [**Kinesis Firehose**](https://aws.amazon.com/kinesis/data-firehose/) – Stream data directly into S3/Redshift
* [**AWS DMS**](https://aws.amazon.com/dms/) – Migrate/replicate data between DBs
* [**AWS Glue Crawlers**](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) – Auto-discover schema and catalog data
* [**API Gateway**](https://aws.amazon.com/api-gateway/) – REST/HTTP endpoint for external ingestion

---

## 4. **Data Transformation & Processing**

* [**AWS Glue**](https://aws.amazon.com/glue/) – Serverless ETL framework (Jobs, Triggers, Workflows)
* [**Lambda**](https://aws.amazon.com/lambda/) – Lightweight transformation or filtering logic
* [**EMR**](https://aws.amazon.com/emr/) – Managed Spark/Hadoop clusters for large-scale processing

---

## 5. **Data Catalog & Governance**

* [**Glue Data Catalog**](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html) – Central metadata repository
* [**Lake Formation**](https://aws.amazon.com/lake-formation/) – Secure, govern access to data lakes

---

## 6. **Orchestration & Workflow Automation**

* [**Step Functions**](https://aws.amazon.com/step-functions/) – Visual workflow orchestration
* [**Glue Workflows**](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-glue-workflows.html) – Native ETL pipeline orchestration
* [**EventBridge**](https://aws.amazon.com/eventbridge/) – Event-driven automation across services

---

## 7. **Databases (Structured/Relational)**

* [**RDS**](https://aws.amazon.com/rds/) – Managed relational DB (MySQL/Postgres/SQL Server)
* [**Aurora**](https://aws.amazon.com/rds/aurora/) – High-perf MySQL/PostgreSQL-compatible DB
* [**Redshift**](https://aws.amazon.com/redshift/) – Columnar, MPP warehouse for analytics

---

## 8. **Monitoring & Logging**

* [**CloudWatch**](https://aws.amazon.com/cloudwatch/) – Metrics, logs, alarms
* [**CloudTrail**](https://aws.amazon.com/cloudtrail/) – Audit logs for AWS API activity
* [**X-Ray**](https://aws.amazon.com/xray/) – Distributed tracing

---

## 9. **Security & IAM**

* [**IAM**](https://aws.amazon.com/iam/) – Fine-grained access control for services/resources
* [**KMS**](https://aws.amazon.com/kms/) – Key management for encrypting S3, RDS, etc.
* [**Secrets Manager**](https://aws.amazon.com/secrets-manager/) – Store/manage credentials securely

---

## 10. **Analytics & BI Integration**

* [**Athena**](https://aws.amazon.com/athena/) – Serverless querying on S3 with SQL
* [**QuickSight**](https://aws.amazon.com/quicksight/) – AWS-native BI dashboarding tool
* [**OpenSearch**](https://aws.amazon.com/opensearch-service/) – Search & analytics on logs or semi-structured data

---

## 11. **DevOps & CI/CD (Optional for Data Projects)**

* [**CloudFormation**](https://aws.amazon.com/cloudformation/) – IaC for provisioning AWS resources
* [**CodePipeline**](https://aws.amazon.com/codepipeline/) / [**CodeBuild**](https://aws.amazon.com/codebuild/) – Automation of ETL deployment workflows
* [**Cloud9**](https://aws.amazon.com/cloud9/) – Browser-based IDE to develop/test Python or Glue jobs
