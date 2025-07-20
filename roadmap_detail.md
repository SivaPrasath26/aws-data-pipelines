# AWS Data Pipelines – Detailed Learning Roadmap

---

## Phase 1: Foundations (2 weeks)
**Goal**: Learn core AWS navigation and scripting for data access and security.

| Tool / Service | Description |
|----------------|------------------------|
| IAM            | Manage access to AWS services through users, roles, and policies. |
| S3             | Object storage used as the primary data lake for raw and processed data. |
| AWS Console    | Web UI for configuring, managing, and debugging AWS resources. |
| AWS CLI        | Command-line tool to interact with AWS services for automation and scripting. |
| Boto3          | Python SDK to programmatically access and manipulate AWS resources. |

---

## Phase 2: Ingestion (3 weeks)
**Goal**: Build real-time and batch data ingestion pipelines from various sources.

| Tool / Service     | Description |
|--------------------|------------------------|
| AWS Glue Crawlers  | Automatically scan data and create metadata in Glue Data Catalog. |
| AWS Lambda         | Serverless compute to run lightweight code in response to events. |
| Amazon Kinesis     | Real-time stream processing service to ingest continuous data flows. |
| AWS DMS            | Service to migrate and replicate databases to AWS with minimal downtime. |

---

## Phase 3: ETL & Storage (4 weeks)
**Goal**: Design and build scalable data transformation pipelines.

| Tool / Service       | Description |
|----------------------|------------------------|
| AWS Glue (PySpark)   | Managed Spark environment to write ETL jobs in Python. |
| Delta Lake           | Storage layer supporting ACID transactions and schema evolution on S3. |
| S3 Partitioning      | Organize data in S3 for efficient querying with Athena or Glue. |
| Glue Job Bookmarks   | Track previously processed data to support incremental ETL. |

---

## Phase 4: Querying & Reporting (2 weeks)
**Goal**: Enable analysts to explore and report on processed datasets.

| Tool / Service     | Description |
|--------------------|------------------------|
| Amazon Athena      | Serverless SQL engine to query data stored in S3. |
| Amazon QuickSight  | Business intelligence tool to build interactive dashboards. |
| Glue Data Catalog  | Central metadata store used by Athena and other services. |

---

## Phase 5: Orchestration & Monitoring (4 weeks)
**Goal**: Build reliable workflows and track system behavior.

| Tool / Service     | Description |
|--------------------|------------------------|
| AWS Step Functions | Visual workflow builder to orchestrate Lambda, Glue, and other steps. |
| Amazon MWAA        | Managed Apache Airflow for defining and scheduling complex DAGs. |
| CloudWatch         | Centralized logging, metrics, and alarms for observability. |
| CloudTrail         | Records API activity across AWS accounts for security and auditability. |

---

## Phase 6: CI/CD & Infrastructure (4 weeks)
**Goal**: Automate environment provisioning and deployment workflows.

| Tool / Service     | Description |
|--------------------|------------------------|
| Terraform          | Infrastructure-as-code tool to define and provision AWS resources. |
| CodePipeline       | Orchestrates automated build-test-deploy pipelines. |
| CodeBuild          | Executes build and test scripts as part of CI/CD. |
| Multi-env Setup    | Use workspaces or parameterization to support dev, stage, and prod pipelines. |

---

## Phase 7: Capstone & Resume Integration (2 weeks)
**Goal**: Build a full pipeline project and prepare it for portfolio/resume use.

| Tool / Practice       | Description |
|-----------------------|------------------------|
| End-to-End Project     | Combine ingestion, transformation, querying, and orchestration into one pipeline. |
| GitHub Repository      | Maintain version-controlled, documented project with README and code. |
| Architecture Diagram   | Visualize data flow, tools, and layers in your pipeline. |
| Resume Integration     | Extract technical bullet points to showcase hands-on skills and ownership. |

