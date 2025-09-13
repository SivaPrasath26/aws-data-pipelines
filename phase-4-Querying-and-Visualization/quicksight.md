# QuickSight

Amazon QuickSight is AWS’s serverless BI and visualization tool. It connects to Athena, Redshift, RDS, and other sources to build dashboards and share insights at scale.

---

## Learning Goals

| Goal                        | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| Connect QuickSight to Athena | Enable querying of Glue Catalog tables through Athena          |
| Build interactive dashboards | Create charts, KPIs, and drill-down dashboards                |
| Manage data in SPICE         | Import datasets into QuickSight’s in-memory engine for speed   |
| Implement row-level security | Control which data subsets different users can view            |
| Automate refresh             | Keep dashboards updated as new data arrives in S3              |

---

## Key Concepts

| Concept       | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| Dataset       | Logical view of a data source; can include joins, filters, and calculations |
| SPICE         | QuickSight’s in-memory cache for fast querying                              |
| Analysis      | Workspace to design visuals and explore data                                |
| Dashboard     | Published, shareable collection of visuals                                  |
| Row-level security | Feature to filter rows per user or group                               |

---

## Workflow

1. **Connect to Athena**
   - Configure QuickSight to access AWS Glue Catalog databases.
   - Ensure Athena output bucket is configured with correct permissions.

2. **Create Dataset**
   - Choose curated tables (`sales_curated`, `agg_store_dept`, etc.).
   - Apply filters, calculated fields, and joins if needed.

3. **SPICE Import**
   - Load data into SPICE for high-performance queries.
   - Configure refresh schedules (daily/weekly).

4. **Design Analysis**
   - Build visuals such as time-series sales trends, store-type comparisons, or holiday effects.
   - Use interactive filters and drill-down hierarchies.

5. **Publish Dashboard**
   - Share with users or groups.
   - Apply row-level security to restrict access by department, region, or role.

---

## Best Practices

- Use **SPICE** for speed and cost-efficiency; fall back to live queries only when needed.
- Keep datasets small enough for SPICE but partitioned for refresh efficiency.
- Apply **naming conventions** to datasets and dashboards for easier navigation.
- Use **themes** for consistent dashboard styling.
- Monitor **usage metrics** to understand adoption and optimize refresh intervals.

---

## Output of This Module

- Athena tables from Glue Catalog connected to QuickSight.
- Interactive dashboards showing sales trends, store comparisons, and holiday impact.
- Automated refresh and row-level security enabled.
- Published dashboards for business consumption.
