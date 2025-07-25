# AWS CLI

The AWS CLI (Command Line Interface) allows programmatic access to AWS services through shell commands. It is essential for automating AWS tasks, integrating with CI/CD, and managing cloud infrastructure efficiently without relying on the AWS Console UI.

---

## 1. Installation and Configuration

Install CLI v2: [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Configure credentials:

```bash
aws configure
```

This prompts for:

* Access Key ID
* Secret Access Key
* Default region (e.g., `us-east-1`)
* Output format (`json`, `text`, `table`)

Credentials stored in:

* `~/.aws/credentials`
* `~/.aws/config`

---

## 2. Syntax Format

```bash
aws <service> <command> [parameters]
```

Example usage:

```bash
aws s3 ls
aws s3 cp file.csv s3://my-bucket/
aws glue get-databases
aws ec2 describe-instances
```

---

## 3. Key Commands for Data Engineers

### S3 (Object Storage)

```bash
aws s3 ls                                       # List all buckets
aws s3 mb s3://my-bucket-name                   # Create new bucket
aws s3 cp local_file.csv s3://my-bucket/        # Upload file
aws s3 sync ./local_folder/ s3://my-bucket/     # Sync local to S3
aws s3 rm s3://my-bucket/file.csv               # Delete file
```

### Glue (ETL + Data Catalog)

```bash
aws glue get-databases                          # List Glue databases
aws glue get-tables --database-name my_db       # List tables in database
aws glue start-job-run --job-name my_job        # Trigger Glue job
```

### IAM (Permissions)

```bash
aws iam list-users                              # List all IAM users
aws iam list-roles                              # List all IAM roles
```

### CloudWatch (Logs)

```bash
aws logs describe-log-groups                    # Show log groups
aws logs get-log-events                         # Fetch log data
```

---

## 4. Output Formatting

You can change output style using:

```bash
--output json
--output table
--output text
```

Example:

```bash
aws s3 ls --output table
```

To set globally:

```bash
aws configure set output json
```

---

## 5. Common Flags

* `--region` – override default region
* `--profile` – specify named profile
* `--output` – control formatting
* `--query` – filter output using JMESPath

Example:

```bash
aws s3 ls --region us-west-2 --output json
```

---

## 6. Use Cases in Data Engineering

* Automate data uploads to S3
* Trigger Glue jobs via scripts
* Monitor ETL logs with CloudWatch
* Manage IAM access policies and users
* Create and deploy infrastructure using CLI + IaC (e.g., CloudFormation)

---
