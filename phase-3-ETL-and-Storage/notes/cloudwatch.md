# Amazon CloudWatch

## Overview
Amazon CloudWatch is a monitoring and observability service for AWS resources, applications, and infrastructure. It collects **metrics, logs, and events**, and provides dashboards, alarms, and automated responses.

## Key Features
- **Metrics** – Built-in (CPU, memory, latency) and custom metrics.  
- **Logs** – Centralized storage of application, system, and service logs.  
- **Alarms** – Trigger actions when thresholds are breached.  
- **Dashboards** – Visualize metrics across services.  
- **Events / Rules** – Respond to state changes (via EventBridge).  

## Core Components
1. **Metrics**
   - Default service metrics (e.g., EC2 CPUUtilization, S3 BucketSizeBytes).
   - Custom metrics via CloudWatch API or embedded SDK.

2. **Logs**
   - Application logs from EC2, Lambda, ECS, Glue jobs.
   - Log groups → Log streams → Events.
   - Supports filters and subscriptions (e.g., to Lambda or Kinesis).

3. **Alarms**
   - Threshold-based (static or anomaly detection).
   - Actions: SNS notifications, Auto Scaling policies, Lambda triggers.

4. **Dashboards**
   - Custom visualization of metrics, alarms, and logs.
   - Shareable across accounts.

5. **Events (EventBridge)**
   - Event-driven integration with AWS services.
   - Example: On Glue job failure → trigger Lambda → send alert.

## Common Challenges
- **Log retention costs** – Set retention policies.  
- **High cardinality metrics** – Can cause cost spikes.  
- **Noise in alarms** – Tune thresholds and aggregation periods.  

## Best Practices
- Aggregate logs before exporting (reduce cost).  
- Use **metric filters** to extract KPIs from logs.  
- Configure **alarms on 99th percentile latency**, not just averages.  
- Integrate with **CloudWatch Agent** for EC2/ECS system metrics.  
- Route alarms to **SNS + Slack/Email** for visibility.  

## Hands-On Practice
1. Enable CloudWatch logs for a Glue job.  
2. Create a metric filter on the logs (e.g., count ERROR events).  
3. Set an alarm on the metric with SNS notification.  
4. Build a dashboard tracking job runtime and errors.  
5. Use EventBridge to trigger Lambda when a job fails.  

## Resources
- [CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)  
- [Metrics and Dimensions Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)  
