# 🛒 Walmart Data Engineering Pipeline with Apache Airflow & dbt

> An end-to-end modern Data Engineering project that automates data ingestion, transformation, testing, and analytics using **Apache Airflow**, **dbt**, **PostgreSQL**, and **Docker**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Airflow](https://img.shields.io/badge/Apache-Airflow-red)
![dbt](https://img.shields.io/badge/dbt-Core-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue)
![Docker](https://img.shields.io/badge/Docker-2496ED)

---

# 📖 Project Overview

This project demonstrates how a production-grade data pipeline can be built using modern Data Engineering tools.

The pipeline automatically:

- Extracts Walmart sales data
- Loads raw data into PostgreSQL
- Transforms raw tables using dbt
- Performs automated data quality tests
- Orchestrates the entire workflow using Apache Airflow

The goal is to simulate how analytics pipelines are built in real-world companies.

---

# 🏗️ Architecture

```text
                Walmart Dataset
                      │
                      ▼
             PostgreSQL (Raw Layer)
                      │
                      ▼
               dbt Transformations
                      │
                      ▼
          Clean Analytics Models
                      │
                      ▼
               dbt Data Tests
                      │
                      ▼
             Apache Airflow DAG
```

---

# 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Database | PostgreSQL |
| Transformation | dbt Core |
| Orchestration | Apache Airflow |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
Walmart_Airflow_DBT_Project/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   ├── plugins/
│   └── docker-compose.yaml
│
├── walmart_project/
│   ├── models/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── dataset/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Workflow

## Step 1

Load Walmart dataset into PostgreSQL.

↓

## Step 2

Apache Airflow triggers the pipeline.

↓

## Step 3

dbt executes models.

↓

## Step 4

Data quality tests are performed.

↓

## Step 5

Analytics-ready tables are created.

---

# ✨ Features

- Automated ETL pipeline
- Apache Airflow orchestration
- dbt models
- Incremental transformations
- Data quality testing
- Modular SQL transformations
- Dockerized environment
- Easy local deployment
- Production-like workflow

---

# 🗂 dbt Layers

### Raw

Stores untouched source data.

### Staging

- Data cleaning
- Renaming columns
- Type conversions

### Intermediate

Business transformations and reusable logic.

### Mart

Analytics-ready tables used for reporting and dashboards.

---

# 📊 Airflow DAG

The DAG automates:

```
Start
   │
   ▼
Load Raw Data
   │
   ▼
dbt Seed
   │
   ▼
dbt Run
   │
   ▼
dbt Test
   │
   ▼
Pipeline Complete
```

---

# 🧪 Data Quality Checks

The project validates:

- Unique IDs
- Not Null columns
- Accepted values
- Referential Integrity
- Relationship Tests

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/shourya845/Walmart_Airflow_DBT_Projects.git
```

```bash
cd Walmart_Airflow_DBT_Projects
```

---

## Create Virtual Environment

```bash
python -m venv walmart_project_dbt
```

Windows

```bash
walmart_project_dbt\Scripts\activate
```

Linux / Mac

```bash
source walmart_project_dbt/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Airflow

```bash
docker-compose up
```

---

## Run dbt

```bash
dbt debug
```

```bash
dbt seed
```

```bash
dbt run
```

```bash
dbt test
```

---

## Run Airflow

Open

```
http://localhost:8080
```

Default credentials

```
Username : airflow
Password : airflow
```

---

# 📈 Skills Demonstrated

- Data Engineering
- Apache Airflow
- dbt
- SQL
- Python
- Docker
- PostgreSQL
- ETL Pipeline Design
- Data Modeling
- Data Quality Testing
- Workflow Orchestration
- Git

---

# 🎯 Future Improvements

- AWS S3 Integration
- Snowflake Support
- CI/CD Pipeline
- Great Expectations
- Slack Notifications
- Email Alerts
- Incremental Loading
- Docker Compose Optimization
- Monitoring Dashboard

---

# 📸 Screenshots

Add screenshots of:

- Airflow UI
- DAG Success
- dbt Documentation
- dbt Lineage Graph
- PostgreSQL Tables

---

# 👨‍💻 Author

**Shourya Negi**

GitHub: https://github.com/shourya845

LinkedIn: https://www.linkedin.com/in/shourya-negi-2587b7291/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
