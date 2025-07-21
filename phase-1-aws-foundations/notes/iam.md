# IAM (Identity and Access Management)

IAM is used to control who can access AWS resources and what actions they can perform.

## Core Concepts

- **Root User**: The **Root User** is the identity created when you first sign up for AWS. It has Full access to all AWS Services and Resources; should be avoided for day-to-day tasks.
- **IAM User**: Individual identity with long-term credentials.
- **IAM Group**: Collection of users with common permissions.
- **IAM Role**: Temporary permissions assumed by users, services, or apps.
- **Policies**: JSON documents that define permissions.

## Root User vs IAM User

| Feature                     | Root User                            | IAM User                                  |
|-----------------------------|---------------------------------------|--------------------------------------------|
| Access Level                | Full, unrestricted                    | Controlled via policies                    |
| Use Case                    | Account setup, billing, critical ops | Daily tasks, pipeline access               |
| Modifiable Permissions      | No (has all by default)              | Yes (assign permissions via policies)      |
| Can Be Deleted              | No                                    | Yes                                        |
| MFA Recommended             | Required                              | Strongly recommended                       |
| JSON Policies Attached      | Not applicable                        | Yes                                        |

## Best Practices

- Never use root user for regular tasks.
- Enable MFA for the root account.
- Use IAM users with limited privileges for daily tasks.
- Apply the principle of least privilege.

## Example Policy: S3 Full Access

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    }
  ]
}

```

> This policy allows full access to all S3 resources. Use only in controlled environments.
