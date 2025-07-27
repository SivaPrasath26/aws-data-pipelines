## AWS API Gateway

## What is API Gateway?

AWS API Gateway is a fully managed service to create, publish, maintain, monitor, and secure APIs at any scale. It supports REST, WebSocket, and HTTP APIs.

---

## Key Use Cases

* Create RESTful endpoints for Lambda functions or HTTP backends
* Proxy requests to other AWS services (e.g., DynamoDB, S3)
* Secure and throttle API access
* Enable microservices architecture

---

## API Types

* **REST API:** Feature-rich, suitable for complex request validation and transformation
* **HTTP API:** Lightweight, faster, cheaper. Ideal for simple use cases
* **WebSocket API:** For real-time two-way communication (e.g., chat apps)

---

## Core Components

### 1. **Resources and Methods**

* Define RESTful resources (`/users`, `/orders`)
* Attach HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) to each resource

### 2. **Integrations**

* **Lambda Proxy Integration** (most common)
* HTTP/HTTPS Backends
* AWS Service Integrations (S3, DynamoDB, etc.)

### 3. **Stages and Deployments**

* **Stage:** Named environments like `dev`, `test`, `prod`
* You deploy an API to a stage to make it callable

### 4. **Throttling and Quotas**

* Protect backend from overload
* Control usage per API key, user, or method

### 5. **Security**

* API Key (basic control)
* IAM Authorization (fine-grained AWS access)
* Cognito User Pools (OAuth2-based user auth)
* Lambda Authorizer (custom logic)

### 6. **Monitoring**

* Integrated with **CloudWatch** for request count, latencies, error rates
* Enable **logging and tracing** (X-Ray)

---

## Common Integration Pattern: Lambda + API Gateway

1. Create Lambda Function (e.g., handler for `/submit-form`)
2. Create REST or HTTP API in API Gateway
3. Define resource `/submit-form`, attach `POST` method
4. Set integration target to the Lambda function
5. Deploy API to a stage and invoke via HTTPS endpoint

---

## Pricing

* Based on **number of requests**, **data transfer**, and **caching (if used)**
* HTTP APIs are cheaper than REST APIs

---

## Focus Areas

* Differences between REST, HTTP, and WebSocket APIs
* When to use which integration (Lambda vs HTTP backend vs AWS service)
* Security features: IAM vs Cognito vs Lambda authorizer
* How throttling and quota work

---

## Hands-On Practice

* Build a simple Lambda-backed REST API
* Create an HTTP API to proxy to an external URL
* Secure an API using API keys and test throttling settings

---

## Resources

* [API Gateway Docs](https://docs.aws.amazon.com/apigateway/index.html)
* [HTTP vs REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
