## AWS Kinesis Data Streams

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

### Architecture

```
Data Producers (apps, IoT, logs)
        |
   PutRecord / PutRecords API
        |
     Kinesis Stream
   (sharded stream pipeline)
        |
    Consumers (Lambda, KCL app, Firehose)
        |
    S3 / Redshift / Elasticsearch / EMR
```

---

### Writing to a Stream (Producer)

* Use AWS SDK (e.g., Boto3 for Python):

```python
import boto3
client = boto3.client('kinesis')
client.put_record(
    StreamName='mystream',
    Data=b'mydata',
    PartitionKey='mypartition'
)
```

---

### Reading from a Stream (Consumer)

* **Lambda** (easiest): Event-driven consumption
* **KCL (Kinesis Client Library)**: Java-based lib for advanced control
* **Enhanced fan-out**: Parallel consumer reads with dedicated throughput

---

### Limits and Throughput

| Resource         | Limit (default)          |
| ---------------- | ------------------------ |
| Shard write      | 1 MB/s or 1000 records/s |
| Shard read       | 2 MB/s                   |
| Record size      | Up to 1 MB               |
| Stream retention | 24h–365 days             |

---

### Monitoring Tools

* **CloudWatch Metrics**: IncomingBytes, GetRecords.IteratorAgeMilliseconds, ReadProvisionedThroughputExceeded, WriteProvisionedThroughputExceeded
* **CloudTrail**: API audit
* **CloudWatch Alarms**: Alert when throttling or lag happens

---

### Security

* **IAM Policies** for access control
* **Encryption at rest** with AWS KMS
* **HTTPS endpoints** for data-in-transit

---

### Pricing Factors

* Number of shards provisioned (per hour)
* PUT payload volume (per GB)
* Enhanced fan-out consumers (optional)
* Extended retention (optional)

---

### Summary

Kinesis Data Streams is essential for building scalable real-time data pipelines. It provides reliable ingestion of streaming data with high durability, fine-grained throughput control, and tight AWS integration.

---

### Next Step

Move to **Kinesis Firehose** after solid understanding and optional hands-on with Data Streams.
