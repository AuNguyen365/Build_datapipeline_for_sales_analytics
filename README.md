# Build_datapipeline_for_sales_analytics

## 1. Project Overview

This project builds a data pipeline to process sales data.

The pipeline performs:
- Extract data from csv
- Transform and clean the data into a SQL database
- Load the data into a SQL database
- Analyze the data using SQL queries
- Visualize insights using Python

This project simulates a real-world workflow of a Data Engineer.

---

## 2. Tech Stack

- Python
- Pandas
- SQL
- PostgreSQL / MySQL
- Matplotlib
- VS code

---

## 3. Project Structure:
Build_datapipeline_for_sales_analytics
│
├── data
│   └── sales.csv
│
├── scripts
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── sql
│   └── analysis.sql
│
├── notebooks
│   └── analysis.ipynb
│
└── README.md

---

## 4. Data Pipeline:

Raw Data (CSV)
    ↓
Extract with Python
    ↓
Transform & Clean (Pandas)
    ↓
Load into SQL Database
    ↓
SQL Analysis
    ↓
Visualization

