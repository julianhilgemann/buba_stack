---

# 🧠 BI Pipeline Cheatsheet: Core Python, SQL, dbt, and Docker Commands

Quick-access reference for key functions, methods, and commands across your end-to-end BI stack.

---

## 🐍 Python Cheatsheet

### 📦 Package Management
```bash
# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt
```

### 🗂️ File I/O
```python
# Reading a CSV
import pandas as pd
df = pd.read_csv("file.csv")

# Writing to a CSV
df.to_csv("file.csv", index=False)

# Working with paths
from pathlib import Path
Path("data").mkdir(exist_ok=True)
```

### 📬 API Requests
```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

### 📐 Data Processing with Pandas
```python
df.head()                    # Preview
df.info()                    # Structure
df.describe()                # Summary stats
df.dropna()                  # Drop missing
df.fillna(0)                 # Fill missing
df['col'].astype(float)      # Convert types
df.groupby("col").mean()     # Grouped agg
pd.merge(df1, df2, on="id")  # Join tables
```

---

## 🗃️ PostgreSQL + SQL

### 🔌 Connect (via psycopg2)
```python
import psycopg2
conn = psycopg2.connect(dbname="db", user="user", password="pass", host="localhost", port="5432")
```

### 🧾 SQL Commands
```sql
-- Create table
CREATE TABLE rates (
    date DATE,
    value NUMERIC,
    series_id VARCHAR
);

-- Insert data
INSERT INTO rates VALUES ('2024-01-01', 3.2, 'IR_EUR');

-- Select data
SELECT * FROM rates WHERE value > 3;

-- Join tables
SELECT * FROM rates r
JOIN series s ON r.series_id = s.series_id;
```

---

## 🧱 dbt Cheatsheet

### 🔧 Common Commands
```bash
dbt init my_project                 # Create project
dbt run                             # Execute models
dbt test                            # Run tests
dbt seed                            # Load CSVs
dbt docs generate && dbt docs serve  # Build + host docs
```

### 🧠 Jinja + SQL Snippets
```sql
-- Use Jinja variables
SELECT * FROM {{ ref('stg_interest_rates') }}

-- Create a model (models/my_model.sql)
SELECT
  date,
  value,
  currency
FROM {{ ref('raw_interest_rates') }}
WHERE value IS NOT NULL
```

---

## ⏱️ Airflow Basics

### 🛠️ DAG Definition
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract():
    print("Fetching data...")

with DAG(dag_id='my_pipeline', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    task = PythonOperator(task_id='extract_task', python_callable=extract)
```

---

## 📦 Docker Cheatsheet

### 🧱 Dockerfile
```Dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

### 🧩 docker-compose.yml
```yaml
version: "3.8"
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
  app:
    build: .
    depends_on:
      - db
```

### 🔧 Commands
```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
docker-compose up --build
```

---

## 📊 Power BI Integration

### 🔗 Connect PostgreSQL to Power BI:
1. Go to **Home > Get Data > PostgreSQL**.
2. Input host, database, and credentials.
3. Use Power Query for cleaning and transformation.

---

## 🧠 Git & GitHub

### 🚀 Common Git Commands
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourname/project.git
git push -u origin main
```

### 📄 .gitignore Example
```gitignore
venv/
__pycache__/
.env
*.pyc
```

---