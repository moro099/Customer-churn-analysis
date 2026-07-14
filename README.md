# 📊 Customer Churn Analysis

## 📖 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses, especially in the telecom industry. Understanding why customers leave and identifying high-risk customers can help organizations improve retention strategies and reduce revenue loss.

This end-to-end data analytics project uses Python for data cleaning, preprocessing, exploratory data analysis (EDA), and feature engineering, followed by Power BI for creating an interactive dashboard that provides actionable business insights into customer behavior and churn patterns.

---

## 💼 Business Problem

Telecom companies lose significant revenue when customers discontinue their services. Without understanding the key factors influencing churn, it becomes difficult to implement effective retention strategies.

The goal of this project is to analyze customer data, identify the major drivers of churn, segment customers based on risk and value, and provide meaningful insights that can help businesses reduce customer attrition and improve overall customer retention.

---

## 🎯 Project Objectives

- Clean and preprocess raw customer data using Python.
- Perform Exploratory Data Analysis (EDA) to identify churn patterns.
- Engineer business-focused features such as Risk Score, Revenue at Risk, and Customer Value Segment.
- Build an interactive Power BI dashboard for business users.
- Generate actionable insights to support customer retention strategies.

---

## 📂 Dataset

The project uses the **Telco Customer Churn Dataset**, which contains customer demographics, account details, subscribed services, billing information, and churn status.

### Dataset Features

- Customer Demographics
- Subscription & Service Details
- Contract Information
- Payment Methods
- Monthly Charges
- Total Charges
- Customer Tenure
- Churn Status

### Data Processing Pipeline

The dataset was processed in three stages:

| Stage | File | Description |
|-------|------|-------------|
| Raw Data | `Telco_customer_churn.xlsx` | Original telecom customer dataset |
| Cleaned Data | `cleaned_customer_churn.csv` | Cleaned dataset after handling missing values, duplicates, and data type conversions |
| Final Dataset | `cleaned_customer_churn_final.csv` | Dataset after EDA and feature engineering, used for Power BI dashboard development |

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Libraries | Pandas, NumPy, Matplotlib |
| Data Source | Microsoft Excel |
| IDE | Jupyter Notebook, VS Code |
| Data Visualization | Power BI |
| Version Control | Git & GitHub |

---

## 🔄 Project Workflow

```text
Raw Excel Dataset (.xlsx)
        │
        ▼
Data Cleaning (Python)
- Missing Value Treatment
- Duplicate Check
- Data Type Conversion
        │
        ▼
cleaned_customer_churn.csv
        │
        ▼
Exploratory Data Analysis (EDA)
- Customer Analysis
- Churn Analysis
- Revenue Analysis
        │
        ▼
Feature Engineering
- Churn Flag
- Tenure Group
- Monthly Charge Band
- Customer Value Segment
- Revenue at Risk
- Risk Score
- Risk Category
        │
        ▼
cleaned_customer_churn_final.csv
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights & KPI Reporting
```

---

## 🧹 Data Cleaning

The raw telecom dataset was cleaned using **Python (Pandas)** to ensure data quality before analysis.

### Cleaning Steps

- Checked for missing values
- Handled null values
- Removed duplicate records
- Converted data types
- Standardized categorical values
- Exported the cleaned dataset for further analysis

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand customer behavior and identify factors influencing churn.

### Analysis Performed

- Customer Demographics Analysis
- Churn Distribution
- Contract Type Analysis
- Internet Service Analysis
- Payment Method Analysis
- Monthly Charges Distribution
- Total Charges Analysis
- Customer Tenure Analysis
- Revenue Analysis

---

## ⚙️ Feature Engineering

To improve business analysis, several new features were created.

### Engineered Features

- Churn Flag
- Tenure Group
- Monthly Charge Band
- Customer Value Segment
- Revenue at Risk
- Risk Score
- Risk Category

These engineered features enabled deeper customer segmentation and risk analysis in the Power BI dashboard.

---

## 📈 Power BI Dashboard

An interactive Power BI dashboard was developed using the final processed dataset to monitor customer churn, revenue, customer demographics, and risk segmentation.

### Dashboard Highlights

- Executive KPI Overview
- Customer Demographics Analysis
- Churn Analysis
- Revenue Analysis
- Contract Type Analysis
- Payment Method Analysis
- Customer Risk Segmentation
- Customer Value Segmentation
- Interactive Filters & Slicers


---

## 💡 Key Business Insights

The analysis revealed several important business insights:

- Customers with **Month-to-Month contracts** have the highest churn rate.
- **Fiber Optic** internet users are more likely to churn than DSL users.
- Customers using **Electronic Check** as their payment method show higher churn.
- Customers with **shorter tenure** are more likely to leave.
- High monthly charges are associated with increased churn.
- Revenue at Risk analysis helps identify potential monthly revenue loss from churning customers.
- Risk segmentation enables businesses to prioritize customer retention strategies.

---

 

## 🚀 Future Enhancements

- Deploy the dashboard to Power BI Service.
- Integrate SQL for advanced analytical queries.
- Build an automated ETL pipeline using Azure Data Factory.
- Store processed data in Azure SQL Database.
- Develop a machine learning model for churn prediction.
- Schedule automatic dashboard refreshes.



Author : Ketan dubey
