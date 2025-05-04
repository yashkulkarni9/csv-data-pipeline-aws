# 📊 Serverless CSV Data Pipeline with Visualization using AWS

A fully serverless data pipeline that ingests CSV files into AWS S3, processes them with AWS Glue, and visualizes the results using Amazon QuickSight — all without provisioning or managing servers.

---

## 🌐 Project Overview

This project demonstrates a real-time, automated, and serverless data pipeline that:
- Accepts raw CSV uploads via Amazon S3
- Processes and transforms the data using AWS Glue (Spark job)
- Stores clean data in a separate S3 bucket
- Visualizes insights using Amazon QuickSight dashboards

---

## 🚀 Use Case

This architecture is ideal for organizations that:
- Regularly receive structured CSV data (e.g., reports, logs, IoT metrics)
- Need automated ETL workflows without manual processing
- Want to visualize the results for decision-making or reporting (dashboards)

**Examples:**
- Finance teams uploading daily transaction reports
- Retail companies tracking inventory logs
- Health systems analyzing patient intake data in CSV format

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Amazon S3** | File storage for raw, processed, and final data |
| **AWS Lambda** | Optional: Can be used for file validation or triggering Glue |
| **AWS Glue** | Serverless Spark-based ETL job to transform CSV data |
| **Amazon QuickSight** | BI tool for data visualization |
| **IAM Roles & Policies** | Secure access and permissions control |
| **Python (PySpark)** | Transformation logic in Glue scripts |

---

## 🔄 Project Flow

1️⃣ User uploads CSV → S3 bucket

2️⃣ AWS Glue Job:
     - Reads raw data from raw bucket
     - Cleans/transforms it using PySpark (Glue script)
     - Writes final output to a separate final bucket in S3

3️⃣ Amazon QuickSight:
     - Reads from final S3 bucket via manifest file
     - Loads data into SPICE for faster querying
     - Creates visualizations (charts, tables, dashboards)

4️⃣ Optional:
     - Use Lambda to monitor uploads or trigger workflows

---

## 📈 Example Visualizations

Some visualizations that could be built using Amazon QuickSight:

- **Bar Chart:** Age distribution of entries
- **Pie Chart:** Frequency of records by Name
- **Table View:** Full record inspection by ID (sortable/filterable)

These can help uncover trends, groupings, or anomalies in your CSV data quickly.

---

## ✅ Advantages

- **Serverless:** No need to provision or manage EC2 instances. Pay only for what you use.
- **Scalable:** Automatically scales AWS Glue and QuickSight based on your data volume and user activity.
- **Secure:** Uses IAM roles and S3 bucket policies for strict access control.
- **Real-time-ready:** Can easily integrate with AWS Lambda and EventBridge for near real-time data processing.
- **Reusable & Extensible:** Swap out or extend the CSV schema easily. Can be adapted to different data sources or output formats (e.g., Parquet, JSON).

---

## 🧼 Cleanup Guide (Cost-Saving)

After testing or if no longer needed, clean up to avoid unnecessary AWS costs:

- S3 Buckets: raw, processed, and final CSV buckets
- AWS Glue: Job, crawler, database, and tables
- QuickSight: Dataset, analysis, dashboard (go to Manage QuickSight → Unsubscribe)
- IAM Roles: Custom roles created for Glue or Lambda

---

## Final Outcome

