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

- S3 Raw Bucket — Initial upload destination for user-submitted CSV files triggering the pipeline:
<img width="1470" alt="2" src="https://github.com/user-attachments/assets/a3e842ce-ec4b-4c35-a6f9-738d737dc935" />

- S3 Processed Bucket — Output location for transformed CSV after AWS Glue job execution:
<img width="1470" alt="1" src="https://github.com/user-attachments/assets/7f0642fd-90e2-425b-a0eb-24f4aae44540" />

- S3 Final Bucket — Storage for transformed CSV output written by AWS Glue for QuickSight consumption:
<img width="1469" alt="Screenshot 2025-05-04 at 3 50 22 PM" src="https://github.com/user-attachments/assets/f2aad802-4cb3-4434-bc7b-3d41493bb576" />

- Raw S3 Bucket — Sample CSV file uploaded as input for Glue ETL pipeline:
<img width="1470" alt="3" src="https://github.com/user-attachments/assets/ffa17088-acde-480b-aa48-61ad95c40cd1" />

- Raw CSV File — Input dataset with missing values for Glue ETL to clean:
<img width="639" alt="4" src="https://github.com/user-attachments/assets/d60bff75-d1fc-4869-928b-eba2ef7ae1c1" />

- Cleaned CSV in Processed Bucket — Output from AWS Glue after data transformation:
<img width="1470" alt="5" src="https://github.com/user-attachments/assets/5ff6e533-5c1f-461d-8143-e6467613391e" />

- Cleaned CSV Output — Final result after AWS Glue transformation logic:
<img width="640" alt="6" src="https://github.com/user-attachments/assets/6fabefec-6e09-49ba-b95c-a1486f607db0" />

- AWS Glue Database Creation — Logical grouping for processed tables in Glue Catalog:
<img width="1182" alt="7" src="https://github.com/user-attachments/assets/aa18140c-a949-4358-a23b-fb0d7f5ee9c3" />

- AWS Glue Crawler Setup — Scans S3 and catalogs schema into Glue Data Catalog:
<img width="1180" alt="8" src="https://github.com/user-attachments/assets/f21f35cc-ea57-4e42-ae77-95d5a6f20f64" />

- Glue Crawler Configuration — Maps processed S3 data to Glue Data Catalog database:
<img width="1177" alt="9" src="https://github.com/user-attachments/assets/89bdfee0-237b-41ac-9a2f-938763a6c33a" />

- Glue Crawler successfully started — beginning schema detection for processed data:
<img width="1184" alt="10" src="https://github.com/user-attachments/assets/c9636132-aba7-4cf4-91a0-34ba9f9e88a8" />

- Glue Crawler output table created in data catalog from processed CSV in S3:
<img width="1185" alt="11" src="https://github.com/user-attachments/assets/96e239cc-3194-422c-a93c-13a5e8997546" />

- Glue Job successfully updated and ready to execute:
<img width="1470" alt="12" src="https://github.com/user-attachments/assets/ed795d30-0b20-4b45-8d77-c1590221975d" />

- Final transformed CSV output stored in S3 Bucket Post Glue Job execution:
<img width="1464" alt="14" src="https://github.com/user-attachments/assets/c75ed100-f16a-469f-8f96-2f27570eb67e" />

- AWS Glue Crawler Run Completed Successfully for Processed CSV Metadata Extraction:
<img width="1171" alt="16" src="https://github.com/user-attachments/assets/b6c69b91-9bf5-46b4-b2ac-dd0950f89a62" />

- AWS Glue Job Successfully Completed Data Transformation:
<img width="1137" alt="17" src="https://github.com/user-attachments/assets/93230653-609f-4f71-98ee-60f1a404409c" />

- Final Transformed CSV Files Written to S3 Bucket by AWS Glue Job:
<img width="1439" alt="18" src="https://github.com/user-attachments/assets/08a82347-d0cb-4be2-a908-4f5db61c6c3a" />

- Amazon QuickSight Visualization: Sum of Age by Name from Final Processed CSV Data:
<img width="861" alt="Screenshot 2025-05-04 at 4 23 22 AM" src="https://github.com/user-attachments/assets/fc6f5b26-f15f-417d-887d-fb40bf842db6" />

- Interactive Amazon QuickSight Dashboard Highlighting Age Sum by Name:
<img width="815" alt="Screenshot 2025-05-04 at 4 23 40 AM" src="https://github.com/user-attachments/assets/e8c31178-8310-40dd-beb5-427572210a0e" />



