You can create a free AWS account and receive $100 credits upfront, with an additional $100 available via activities shown in below image.

<img width="642" height="460" alt="image" src="https://github.com/user-attachments/assets/f10a0601-1c7b-477f-839c-790f2090f008" />


---
> **Note**: Most of the AWS services(IAM,S3,Glue,Lambda,Quicksight,RDS,DynamoDB) required for this roadmap are covered under the Free Tier and included with total of $200 credits which is more than enough to gain hands-on experience.

---

#### **Phase 1: AWS Foundations**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| AWS IAM            | Create users, roles, policies                                        | Understand least privilege and use MFA                 |
| AWS S3             | Create versioned bucket, upload objects, enable lifecycle policy     | Explore S3 storage classes                             |
| AWS CLI            | Install CLI, configure profile, run basic commands (`aws s3 ls`)     | Track credentials and regions                          |
| Boto3              | Write Python scripts to list buckets, upload files                   | Practice with boto3 sessions and clients               |
| Console Usage      | Explore AWS Console UI, CloudShell                                  | Use tagging best practices                             |

---

#### **Phase 2: Ingestion (Batch & Real-Time)**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| AWS Kinesis        | Set up Data Streams & Firehose                                       | Ingest mock streaming data using CLI/scripts           |
| Glue Crawlers      | Crawl S3 data to create Data Catalog tables                          | Understand partitioned datasets                        |
| AWS Lambda         | Trigger on S3/Kinesis events                                         | Write Python handler, test locally                     |
| AWS DMS            | Migrate data between RDS and S3                                      | Use public MySQL RDS for demo                          |
| API Gateway        | Create REST API to trigger Lambda                                    | Test endpoints using Postman or curl                   |

---

#### **Phase 3: ETL Pipelines**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| AWS Glue (PySpark) | Build ETL job to clean/transform data                                | Use Glue Studio or script editor                       |
| S3 Partitioning    | Write data using partition keys                                      | Validate folder structure, use Athena for verification |
| Delta Lake         | Write ACID-compliant tables                                          | Use with Glue or Spark                                 |
| Schema Evolution   | Modify schema and handle downstream impact                           | Use Glue DynamicFrames                                 |

---

#### **Phase 4: Querying and Visualization**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| AWS Athena         | Run CTAS queries, create views                                       | Store results in S3 output bucket                      |
| Glue Catalog       | Register & query tables across services                              | Add partition metadata                                 |
| QuickSight         | Build dashboard on top of Athena data                                | Configure SPICE, manage row-level access               |

---

#### **Phase 5: Orchestration and Monitoring**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| Step Functions     | Build state machines with Lambda steps                               | Handle retries and failures                            |
| Amazon MWAA        | Deploy Airflow DAGs to orchestrate Glue, Lambda                      | Store DAGs in S3                                       |
| CloudWatch Logs    | Monitor Lambda, Step Function logs                                   | Create metric filters and alarms                       |
| CloudTrail         | Enable activity logging                                              | Track changes and anomalies                            |

---

#### **Phase 6: Infra as Code + CI/CD**

| Tool / Concept     | Task                                                                 | Notes                                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------|
| Terraform          | Write modules for S3, IAM, Lambda, Glue                              | Use remote state with S3 backend                       |
| CodePipeline       | Automate deployment for Glue/Lambda                                 | Trigger on GitHub push                                 |
| Multi-env Setup    | Parameterize dev/stage/prod using workspaces                         | Enforce separation of environments                     |

---

#### **Phase 7: Capstone Project**

| Task                        | Description                                                               | Notes                                                   |
|-----------------------------|---------------------------------------------------------------------------|---------------------------------------------------------|
| End-to-End Pipeline         | Ingest → Clean → Transform → Store → Query → Visualize                    | Use all learned tools in one project                    |
| Architecture Diagram        | Visualize service interaction using draw.io or Lucidchart                 | Include IAM, S3, Glue, Athena, Lambda, etc.             |
| Cost Estimation             | Use AWS Pricing Calculator                                                | Cross-check with Free Tier usage                       |
| GitHub Documentation        | Write a full README with goals, design decisions, and trade-offs          | Include diagrams and sample outputs                    |
| Portfolio Integration       | Add to resume, blog, or LinkedIn with architecture snapshot               | Emphasize engineering choices and outcomes             |
