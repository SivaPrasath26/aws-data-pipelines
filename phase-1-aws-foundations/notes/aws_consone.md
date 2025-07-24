# AWS Console

This guide provides a concise overview of the AWS Console for data engineering use cases.

---

## 1. What Is the AWS Console?

- A web-based graphical interface to manage AWS services.
- Useful for creating, configuring, and monitoring AWS resources.
- No need for terminal or SDK access for basic operations.

---

## 2. Console Layout & Navigation

- **Search Bar**: Find any AWS service instantly.
- **Region Selector**: Top-right corner; most services are regional.
- **Pinned Services**: Frequently accessed services can be pinned to the top menu.
- **Service Categories**:
  - **Compute**: EC2, Lambda
  - **Storage**: S3, EBS
  - **Analytics**: Athena, Glue, QuickSight
  - **Security & Identity**: IAM, KMS
  - **Monitoring**: CloudWatch, CloudTrail

---

## 3. Common Use Cases

| Task                  | How Console Helps                            |
| --------------------- | -------------------------------------------- |
| S3                    | Create buckets, upload/download files        |
| IAM                   | Create users, roles, policies                |
| Glue                  | Launch crawlers, jobs, manage schema catalog |
| Athena                | Run SQL queries, view results                |
| Kinesis & Lambda      | Configure streams, test triggers             |
| CloudWatch            | Set up logs and monitoring                   |
| Step Functions / MWAA | Build visual workflows                       |

---

## 4. Pros and Cons

| Pros                                      | Cons                                  |
|-------------------------------------------|---------------------------------------|
| No setup; works via browser               | Not suitable for production automation |
| Easy for testing and exploration          | Manual changes are error-prone         |
| Great for visualizing service dependencies| Slower for repeated tasks              |

---

## 5. Key Features to Know

- **Tag Editor**: Add/edit tags across services for cost allocation.
- **Billing Dashboard**: Track estimated monthly charges.
- **CloudShell**: Built-in terminal with AWS CLI access.
- **Trusted Advisor**: Security, cost, performance, fault tolerance insights.
- **Resource Groups**: Filter/manage by tags or types.

---

## 6. Security Best Practices

- Avoid using the **root account** except for initial setup.
- Use **IAM roles/users** with least-privilege permissions.
- **Enable MFA** on all accounts.
- Use **CloudTrail** for activity logging.
- Monitor service health and thresholds using **CloudWatch Alarms**.

---

## Next Steps

Familiarize yourself with:
- Navigating to key services (S3, IAM, Glue, Athena)
- Creating IAM users and setting up MFA
- Exploring the Billing dashboard and Tag Editor
