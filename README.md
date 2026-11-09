# DataPulse – Serverless Data Processing Platform

> **Project Stage:** Day 1 – Initial Development & Environment Setup  
> **Notice:** The AWS infrastructure and serverless processing logic are not yet implemented. This project is in its foundational setup phase.

---

## 1. Project Overview

**DataPulse** is a scalable, cloud-native serverless data processing platform being developed on Amazon Web Services (AWS). DataPulse enables users to upload structured CSV files, select a predefined data processing task, and obtain structured processing metrics and results via REST APIs.

The platform processes datasets asynchronously, decouples ingestion from heavy processing, and provides a cost-effective, event-driven architecture.

---

## 2. Problem Statement

Organizations regularly ingest high volumes of tabular data (e.g., daily sales summaries, inventory updates, partner data feeds) that must be verified, aggregated, and transformed:

- **Manual processing is error-prone and slow:** Spreadsheets and manual scripts break easily and lack auditability.
- **Traditional server servers are costly:** Keeping 24/7 provisioned servers for periodic batch uploads is expensive and hard to scale.
- **Lack of asynchronous feedback:** Direct file uploads to web servers often time out on larger files or complex calculations.

**DataPulse** addresses these challenges using an event-driven serverless architecture that scales automatically from zero, charges only for execution time, and decouples ingestion from compute.

---

## 3. Main Features

- **Asynchronous Serverless File Processing:** Upload files to S3, queue processing requests with SQS, and run tasks with AWS Lambda.
- **Multiple Processing Workflows:** Choose between specialized processing modes (Sales Analysis, Data Validation, Inventory Analysis).
- **Automated Validation & Sanitization:** Detect missing fields, bad data types, and out-of-range numerical values.
- **REST API Result Retrieval:** Query job status and retrieve structured execution results anytime via API Gateway.
- **Reproducible Infrastructure as Code:** Managed with Terraform and automated via GitHub Actions CI/CD.

---

## 4. Supported Processing Tasks

Initially, DataPulse will support three core processing tasks:

1. **Sales Analysis:**
   - Aggregates transaction records.
   - Computes total orders, total units sold, gross revenue, and distinct product counts.
2. **Data Validation:**
   - Audits input rows against schema rules.
   - Identifies missing fields, negative prices or quantities, and duplicate order identifiers.
3. **Inventory Analysis:**
   - Evaluates current warehouse stock levels against reorder thresholds.
   - Identifies items requiring replenishment.

---

## 5. Technology Stack

### Current Local Environment (Day 1)
- **Python 3.12** – Core backend programming language
- **pytest** – Automated unit testing framework
- **Ruff** – Fast Python linter and formatter

### Future Cloud Architecture (Planned)
- **AWS Lambda** – Serverless compute for file processing and API handlers
- **Amazon S3** – Durable object storage for raw CSV uploads and processed outputs
- **Amazon API Gateway** – Secure REST API entry points for job submission and status queries
- **Amazon SQS** – Message queuing to decouple uploads from background processing
- **Amazon DynamoDB** – Fast NoSQL database for job metadata, statuses, and analytical results
- **Amazon Cognito** – User authentication and access control
- **Amazon CloudWatch** – Centralized logging, alarms, and execution metrics
- **Terraform** – Declarative Infrastructure as Code (IaC)
- **GitHub Actions** – Continuous Integration and Continuous Deployment (CI/CD)

---

## 6. Initial Project Structure

```text
datapulse-serverless-data-platform/
│
├── src/
│   └── datapulse/
│       └── __init__.py           # Package root and version metadata
│
├── tests/
│   └── test_project_setup.py     # Verification tests for Day 1 setup
│
├── sample_data/
│   ├── sales/
│   │   └── sales_sample.csv      # Sample sales transactions dataset
│   │
│   ├── validation/
│   │   └── validation_sample.csv # Sample dataset with intentional validation anomalies
│   │
│   └── inventory/
│       └── inventory_sample.csv  # Sample inventory and reorder threshold dataset
│
├── docs/
│   └── csv_schemas.md            # Detailed schema definitions and expectations
│
├── .gitignore                    # Git exclusion rules for caches, secrets, and environments
├── .python-version               # Python version specification (3.12)
├── pyproject.toml                # Project configuration, dependencies, and tool settings
├── README.md                     # Project documentation
└── LICENSE                       # MIT License
```

---

## 7. CSV Schema References

For complete schema details, field definitions, data types, and sample calculation expectations, refer to [`docs/csv_schemas.md`](docs/csv_schemas.md).

Summary of datasets:
- **Sales:** `order_id`, `order_date`, `product_id`, `product_name`, `quantity`, `unit_price`
- **Validation:** `order_id`, `product_name`, `quantity`, `unit_price`
- **Inventory:** `product_id`, `product_name`, `stock_quantity`, `reorder_level`

---

## 8. Local Development Setup

### Prerequisites
- Python 3.12 or newer installed on your machine (`python --version` or `py -3.12 --version`)
- Git installed and configured

---

## 9. Installation Instructions

Follow these steps from the root of the project:

### 1. Create a Virtual Environment

On Windows (PowerShell):
```powershell
python -m venv .venv
```

On macOS / Linux:
```bash
python3.12 -m venv .venv
```

### 2. Activate the Virtual Environment

On Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

On Windows (Command Prompt):
```cmd
.\.venv\Scripts\activate.bat
```

On macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the development tools (pytest and ruff):
```bash
pip install -e ".[dev]"
```

Or install them directly:
```bash
pip install pytest ruff
```

---

## 10. Testing and Code Quality Instructions

DataPulse uses `pytest` for tests and `Ruff` for linting and code formatting.

### Running Tests

Execute pytest with verbose output:
```bash
python -m pytest -v
```

### Running Ruff Linting

Check code for style and lint violations:
```bash
ruff check .
```

To automatically fix safe lint issues:
```bash
ruff check --fix .
```

### Checking Formatting (Dry-Run)

Verify that files follow the formatting rules without modifying them:
```bash
ruff format --check .
```

### Running Ruff Formatting

Format all Python files to adhere to project standards:
```bash
ruff format .
```

---

## 11. Future AWS Architecture Overview

When deployed in upcoming phases, the platform will follow this serverless flow:

1. **Client Request:** Authenticated clients request a presigned S3 upload URL via Amazon API Gateway.
2. **File Ingestion:** The client uploads the CSV file directly to an Amazon S3 intake bucket.
3. **Queue Notification:** S3 upload triggers an Amazon SQS message containing file metadata and the selected processing task.
4. **Lambda Processing:** A worker AWS Lambda function consumes the SQS message, downloads the CSV, runs the appropriate processor (Sales, Validation, or Inventory), and writes results to Amazon DynamoDB.
5. **Result Query:** The client polls or fetches structured results by Job ID via API Gateway.

---

## 12. Development Roadmap

- [x] **Day 1: Project Initialization & Standards**
  - Establish Python 3.12 workspace and `.venv`
  - Configure `pyproject.toml`, `pytest`, and `Ruff`
  - Define CSV schemas and generate sample data
  - Setup initial automated tests and Git documentation
- [ ] **Day 2: Core Processing Logic**
  - Implement Sales Analysis processor with unit tests
  - Implement Data Validation processor with unit tests
  - Implement Inventory Analysis processor with unit tests
- [ ] **Day 3: Cloud Infrastructure (IaC)**
  - Define S3 buckets, SQS queues, and DynamoDB tables in Terraform
  - Configure IAM roles with least-privilege permissions
- [ ] **Day 4: Serverless Handlers**
  - Package Lambda handlers for upload generation and background processing
  - Integrate SQS event triggers with Lambda
- [ ] **Day 5: API Gateway & Authentication**
  - Implement REST API endpoints with Cognito authorizers
  - End-to-end integration testing and CI/CD pipelines
