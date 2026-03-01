# 🏥 Hospital Patients & Claims ETL Analytics Pipeline

An end-to-end AWS Data Engineering project demonstrating the design and implementation of a scalable ETL pipeline using AWS Glue, Amazon S3, and Amazon Redshift.

This project processes hospital patient and claims data through a structured multi-layer architecture and prepares analytics-ready datasets for reporting and business intelligence.

---

## 📌 Project Overview

This pipeline simulates a real-world healthcare data engineering use case where patient and claims data are:

- Extracted from raw sources
- Transformed using PySpark in AWS Glue
- Loaded into Amazon Redshift
- Structured using dimensional modeling
- Prepared for analytical consumption

The architecture follows a Medallion-style layered approach (Raw → Staging → Curated).

---

## 🏗️ Architecture

### 🔹 Data Flow

1. Raw data is ingested into Amazon S3 (CSV/JSON format)
2. AWS Glue ETL jobs process and transform the data using PySpark
3. Cleaned and structured data is written back to S3
4. Data is loaded into Amazon Redshift for analytics
5. SQL queries are used for reporting and insights

---

## 🧠 Technologies Used

- AWS Glue (ETL processing)
- Amazon S3 (Data Lake Storage)
- Amazon Redshift (Data Warehouse)
- Python
- PySpark
- SQL

---

## 📂 Repository Structure

```
etl-glue-hospital-patients-claims-analytics/
│
├── glue_job_scripts/          # AWS Glue PySpark ETL scripts
├── redshift_sql_queries/      # SQL scripts for schema & analytics
├── data_lookup/               # Lookup/reference datasets
├── data_producer/             # Sample data generation scripts
├── er_schema_design/          # ER diagram & schema design files
├── images/                    # Architecture diagrams
├── README.md
└── LICENSE
```

---

## 🔄 ETL Pipeline Workflow

### Step 1: Data Ingestion
- Upload hospital patients and claims datasets to Amazon S3 (Raw layer)

### Step 2: Transformation (AWS Glue)
- Data cleansing
- Schema standardization
- Deduplication
- Business rule implementation
- Slowly Changing Dimension (SCD Type 2) logic

### Step 3: Load to Redshift
- Creation of dimension and fact tables
- Optimized SQL transformations
- Aggregation queries for analytics

---

## 📊 Data Modeling

The warehouse follows a dimensional model:

- Fact Table: Claims
- Dimension Tables:
  - Patients
  - Providers
  - Treatment Categories
  - Time

This structure enables efficient analytical queries and BI reporting.

---

## 🚀 How to Run

1. Clone the repository:
   ```
   git clone https://github.com/SatoruGojo16/etl-glue-hospital-patients-claims-analytics.git
   ```

2. Set up AWS resources:
   - Create S3 buckets (raw and curated)
   - Configure AWS Glue job and IAM role
   - Launch Amazon Redshift cluster

3. Upload source data to S3

4. Deploy and execute Glue job scripts

5. Run SQL scripts in Redshift

---

## 📈 Example Use Cases

- Analyze patient admission trends
- Identify high-cost treatment categories
- Claims approval rate analysis
- Provider performance tracking

---

## 🏆 Key Learning Outcomes

- Building serverless ETL pipelines using AWS Glue
- Implementing Medallion architecture
- Designing dimensional data models
- Applying SCD Type 2 for historical tracking
- Writing optimized SQL for analytics workloads

---

## 🔮 Future Enhancements

- Add Airflow / AWS Step Functions orchestration
- Implement automated data quality validation
- Integrate monitoring & alerting
- Add dashboard visualization layer
- CI/CD pipeline for deployment automation

---

## 📜 License

This project is licensed under the MIT License.
