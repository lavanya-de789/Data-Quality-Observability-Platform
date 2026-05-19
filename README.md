# Data Quality & Observability Platform

## Overview

This project demonstrates an end-to-end Data Quality and Observability platform built using Great Expectations, PySpark, Airflow, Prometheus, and Grafana.

The platform validates incoming datasets using automated quality checks, processes clean data through Spark pipelines, generates operational metrics, and exposes monitoring dashboards for observability.

The goal is to simulate a production-style data reliability framework where data quality issues are detected early and pipeline health is continuously monitored.

---

## Architecture

```text
Raw Data
    ↓
Great Expectations Validation
    ↓
Validated Data
    ↓
Spark Transformations
    ↓
Prometheus Metrics
    ↓
Grafana Dashboards
    ↓
Airflow Orchestration
```

---

## Repository Structure

```text
data-quality-observability/

├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   │   └── customers.csv
│   │
│   └── validated/
│
├── validation/
│   └── validate_data.py
│
├── spark/
│   └── transform.py
│
├── airflow/
│   └── dags/
│       └── quality_pipeline.py
│
├── monitoring/
│   ├── metrics.py
│   └── prometheus.yml
│
├── dashboards/
│   └── grafana_dashboard.json
│
└── docs/
    └── architecture.png
```

---

## Tech Stack

- Python
- Great Expectations
- PySpark
- Apache Airflow
- Prometheus
- Grafana
- Docker
- Pandas
- Parquet

---

## Features

- Automated data validation rules
- Null value detection
- Numeric range checks
- Spark data transformations
- Metrics generation
- Pipeline monitoring
- Dashboard visualization
- Workflow orchestration
- Production reliability simulation

---

## Sample Dataset

```csv
customer_id,name,city,spend

1,John,Dallas,500
2,Edward,Austin,700
3,Sarah,,200
4,Mike,Dallas,-100
5,,Chicago,900
```

Intentional issues:

- Missing city values
- Missing customer names
- Invalid spend values

---

## Validation Rules

Examples:

```python
expect_column_values_to_not_be_null(
'name'
)

expect_column_values_to_not_be_null(
'city'
)

expect_column_values_to_be_between(
'spend',
min_value=0
)
```

Validation detects:

- null records
- invalid ranges
- malformed data
- schema issues

---

## Spark Transformation Layer

Example:

```python
clean=df.dropDuplicates()

clean.write.mode(
'overwrite'
).parquet(
'data/final'
)
```

Tasks:

- remove duplicates
- standardize records
- prepare analytical data

---

## Monitoring Layer

Prometheus metrics:

```python
records.set(100)

validation.set(1)
```

Metrics tracked:

- processed records
- validation status
- pipeline health
- failed checks

Prometheus endpoint:

```text
http://localhost:8000
```

---

## Dashboard Layer

Grafana dashboards visualize:

- validation success rate
- processed volume
- pipeline failures
- system health

---

## Airflow Workflow

```text
Validate Data
      ↓
Spark Transform
```

Task dependency:

```python
validate>>transform
```

---

## Setup Instructions

### Clone repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start services

```bash
docker-compose up -d
```

### Run validation

```bash
python validation/validate_data.py
```

### Run Spark processing

```bash
spark-submit spark/transform.py
```

### Start metrics service

```bash
python monitoring/metrics.py
```

### Start Airflow

```bash
airflow standalone
```

---

## Future Enhancements

- Slack alert integration
- anomaly detection
- row-level lineage
- OpenLineage support
- cloud deployment
- Kubernetes orchestration
- automated remediation
- CI/CD integration
- data SLA monitoring

---

## Business Use Cases

- production ETL monitoring
- financial reporting validation
- fraud data quality checks
- customer profile verification
- enterprise data governance
