## Boto3

### What is Boto3?

Boto3 is the AWS SDK for Python. It allows developers to create, configure, and manage AWS services using Python code.

---

### Why Use Boto3 in Data Engineering?

* Automate infrastructure provisioning (e.g., S3 buckets, Glue jobs)
* Programmatically move data between services
* Useful for orchestration, monitoring, and dynamic pipeline logic
* Enables fine-grained control over AWS services without manual UI actions

---

### Key Concepts

* **Session**: Entry point to manage credentials, regions.
* **Client**: Low-level access to AWS service APIs.
* **Resource**: High-level abstraction (only for some services like S3, DynamoDB).

```python
import boto3

# Create a session
session = boto3.Session(profile_name='default', region_name='us-east-1')

# Create S3 client and resource
s3_client = session.client('s3')
s3_resource = session.resource('s3')
```

---

### Common Use Cases

#### 1. Uploading a file to S3

```python
s3_client.upload_file('local_file.csv', 'my-bucket', 'data/local_file.csv')
```

#### 2. Listing S3 buckets

```python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

#### 3. Reading objects

```python
obj = s3_resource.Object('my-bucket', 'data/local_file.csv')
content = obj.get()['Body'].read().decode('utf-8')
```

#### 4. Starting a Glue Job

```python
glue = boto3.client('glue')
response = glue.start_job_run(JobName='my-glue-job')
print(response['JobRunId'])
```

#### 5. Creating a new S3 bucket

```python
s3_client.create_bucket(Bucket='my-new-bucket')
```

---

### IAM and Boto3

To use Boto3, your IAM role/user must have appropriate permissions for each service action.

**Example policy actions for S3:**

```json
"Action": [
  "s3:PutObject",
  "s3:GetObject",
  "s3:ListBucket"
]
```

---

### Best Practices

* Use sessions and profiles to manage multi-account setups.
* Handle exceptions using `botocore.exceptions`.
* Don’t hardcode credentials. Use environment variables or config files.
* Use pagination when listing large resources.

---

### When Not to Use Boto3

* For extremely high-performance ETL, use native AWS services (like Glue) directly.
* Avoid for bulk transfers - use `aws s3 sync` CLI or S3 Transfer Manager.

---

### Final Tip

Boto3 is essential for automation and orchestration in any serious AWS pipeline. Combine it with logging, retries, and modular functions to build production-grade tools.
