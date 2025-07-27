## AWS Lambda

## Overview

AWS Lambda is a **serverless compute service** that runs code in response to events and automatically manages the compute resources.

* No need to provision or manage servers
* Code is executed only when needed
* Automatically scales with the workload

---

## Key Concepts

### 1. **Function**

* A Lambda function is your unit of deployment and execution
* Written in Python, Node.js, Java, Go, Ruby, or other supported runtimes

### 2. **Event Source**

* Services that trigger Lambda execution

  * Examples: S3 (object upload), DynamoDB (item insert), API Gateway (HTTP request), CloudWatch (scheduler)

### 3. **Handler**

* Entry point for Lambda function
* Signature: `def lambda_handler(event, context):`

  * `event`: the input to your function (trigger data)
  * `context`: runtime info like request ID, timeout, etc.

---

## Lambda Lifecycle

1. Create function (from scratch, blueprint, or container image)
2. Define trigger (e.g., S3, API Gateway)
3. Upload or write code inline
4. Configure memory, timeout, environment variables
5. Deploy and invoke function

---

## Limits

| Attribute    | Default Limit                |
| ------------ | ---------------------------- |
| Memory       | 128 MB to 10 GB              |
| Timeout      | Max 15 minutes               |
| Package Size | Max 250 MB (unzipped)        |
| Concurrency  | 1000 per region (soft limit) |

---

## Use Cases

* Image/video processing
* Real-time file processing (e.g., S3 triggers)
* Serverless API backends (via API Gateway)
* Cron jobs (scheduled via CloudWatch)

---

## Pricing Basics

* Charged based on:

  * Number of requests
  * Duration (ms) × memory allocated
* Free tier includes 1M requests and 400,000 GB-seconds/month

---

## Deployment Tips

* Use environment variables for secrets/configs
* Package dependencies in `.zip` or use layers
* Monitor with CloudWatch Logs
* Version and alias functions for CI/CD

---

## Example Code (Python)

```python
import json

def lambda_handler(event, context):
    print("Received event:", event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

---

## Best Practices

* Keep function logic small and single-purpose
* Use VPC only when needed (adds cold start)
* Log relevant data, not entire payloads
* Avoid long-running operations
* Enable DLQ (Dead Letter Queue) for async errors

---

## Common Integrations

| Service     | Purpose                         |
| ----------- | ------------------------------- |
| S3          | Trigger on file uploads         |
| API Gateway | Build REST APIs                 |
| DynamoDB    | React to DB changes             |
| EventBridge | Event-driven workflows          |
| CloudWatch  | Alarms, logs, and cron triggers |

---

## Summary

AWS Lambda lets you run code without managing infrastructure. It's ideal for short-lived, event-driven workloads and integrates natively with most AWS services.
