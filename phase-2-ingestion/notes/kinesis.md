## Amazon Kinesis (Data Streams & Firehose)

### What is Kinesis Data Streams?

Kinesis Data Streams (KDS) is a real-time, highly scalable, and durable data streaming service. It enables ingestion of gigabytes of data per second from thousands of sources into AWS for analytics and processing.

---

### Key Concepts

* **Shard**: Base throughput unit. 1 shard = 1MB/s write, 2MB/s read, 1000 records/sec.
* **Record**: Data unit in stream. Contains `data`, `partition key`, and `sequence number`.
* **Partition Key**: Used to group data to a shard.
* **Retention**: By default 24 hours, extendable to 7 days or 365 days with extended retention.
* **Producer**: Application/service that sends data to stream.
* **Consumer**: Application that reads/processes records from stream (can be Lambda, KCL, etc).

---

### Use Cases

* Real-time log ingestion and monitoring
* Clickstream analytics
* Financial transactions tracking
* IoT sensor data streaming
* Application telemetry

---

### Limits and Throughput

| Resource         | Limit (default)          |
| ---------------- | ------------------------ |
| Shard write      | 1 MB/s or 1000 records/s |
| Shard read       | 2 MB/s                   |
| Record size      | Up to 1 MB               |
| Stream retention | 24h–365 days             |

---

### Common Use Cases:

* Real-time dashboards
* Anomaly detection
* Real-time ETL

---

### Pricing Factors

* Number of shards provisioned (per hour)
* PUT payload volume (per GB)
* Enhanced fan-out consumers (optional)
* Extended retention (optional)

---

### Summary

* A managed, real-time streaming service for ingesting large amounts of time -ordered data.
* Ideal for logs, events, telemetry, and clickstreams.

---

## Amazon Kinesis Data Firehose

### What It Is:

* A fully managed service for **loading streaming data into destinations** like:

  * Amazon S3
  * Amazon Redshift
  * Amazon OpenSearch
  * Custom HTTP endpoints (via Lambda)

---

### Key Differences from Data Streams:

| Feature           | Data Streams              | Firehose                             |
| ----------------- | ------------------------- | ------------------------------------ |
| Data Buffering    | Manual                    | Automatic                            |
| Consumer Handling | You build                 | Managed                              |
| Latency           | Low                       | Slightly higher (60s buffer default) |
| Destinations      | Flexible (you write code) | Pre-built connectors                 |

---

### Buffering Options:

* **Size-based**: E.g., 5 MB
* **Time-based**: E.g., 60 seconds (default)

---

### Transformations:

* Optional data transformation using **AWS Lambda**

---

### Compression and Encryption:

* Supports GZIP, Snappy, ZIP
* KMS-based encryption at rest

---

### Common Use Cases:

* Real-time log delivery to S3
* Loading transformed event data into Redshift
* Near real-time analytics with minimal code

---

## Summary: When to Use What

| Use Case                            | Use Service     |
| ----------------------------------- | --------------- |
| Real-time processing logic          | Kinesis Streams |
| Auto-load into storage without code | Firehose        |
| Flexible multiple consumers         | Streams         |
| Simple ETL pipelines                | Firehose        |

