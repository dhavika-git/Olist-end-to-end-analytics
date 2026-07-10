# Olist End-to-End E-Commerce Analytics

## Overview

This project is an end-to-end data analytics case study built using the Olist Brazilian E-Commerce dataset. The main goal of this project is to understand the complete analytics workflow, starting from raw data cleaning and feature engineering to SQL analysis and Power BI dashboard creation. Through this project, I explored different business problems and converted raw data into meaningful insights that can help support business decisions.

---

## Business Problem

Olist is a Brazilian e-commerce marketplace that connects customers with sellers. The company wants to better understand its business performance by answering questions such as:

- Which product categories generate the highest revenue?
- Which customers and sellers contribute the most to sales?
- Does delivery delay affect customer satisfaction?
- Which payment methods are most popular among customers?
- Which regions need improvements in delivery and logistics?

---

## Tech Stack

- Python
- Pandas
- NumPy
- MySQL
- Power BI
- Git
- GitHub

---

## Dataset

This project uses the **Olist Brazilian E-Commerce Dataset** available on Kaggle.

The analysis is performed using multiple related datasets, including:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Order Payments
- Order Reviews
- Product Category Translation
- Geolocation

---

## Project Workflow

```text
Raw CSV Files
      ↓
Python (Data Cleaning)
      ↓
Feature Engineering
      ↓
Cleaned CSV Files
      ↓
MySQL (SQL Analysis)
      ↓
Power BI (Interactive Dashboard)
      ↓
Business Insights & Recommendations
```

---

## Data Cleaning & Feature Engineering

The project started by cleaning the raw datasets using Python. During this process, I checked for duplicate records, handled missing values, corrected data types, and converted date columns into the appropriate format. After cleaning, I created several new features such as delivery days, delivery delay, purchase month, weekend orders, installment indicators, product volume, freight percentage, and review categories. These additional features helped in performing more meaningful business analysis.

---

## Business Questions Explored

Some of the key business questions explored in this project include:

- Which months generated the highest revenue?
- Which states have the highest number of customers?
- Which product categories contribute the most revenue?
- Which sellers perform the best based on sales and customer ratings?
- Are delayed deliveries associated with lower review scores?
- Which payment methods are used most frequently by customers?

More business questions covering customer analysis, sales, products, sellers, logistics, payments, and customer satisfaction are included in the SQL and Python analysis files.

---

## Power BI Dashboard

The Power BI dashboard is currently under development and will provide an interactive view of the business performance. It will include dashboards for sales, customers, products, sellers, delivery performance, and payment analysis. Screenshots will be added after the dashboard is completed.

---

## Key Insights

This section will be updated after completing the Power BI dashboard. It will include important findings from the analysis, such as sales trends, customer behavior, product performance, seller performance, delivery analysis, and customer satisfaction.

---

## Recommendations

The recommendations will be based on the insights generated from the final analysis. They will focus on improving logistics, increasing customer satisfaction, promoting high-performing product categories, supporting top sellers, and improving overall business performance.

---

## Repository Structure

```text
olist-end-to-end-analytics/
│
├── python/
│   ├── data_cleaning.py
│   └── feature_engineering.py
│
├── sql/
│   ├── business_queries.sql
│   ├── stored_procedures.sql
│   └── views.sql
│
├── powerbi/
│   └── Olist_Analytics_Dashboard.pbix
│
├── images/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

## How to Run

1. Download the Olist Brazilian E-Commerce dataset.
2. Run the Python scripts to clean the data and create additional features.
3. Import the cleaned datasets into MySQL.
4. Execute the SQL scripts to perform business analysis.
5. Open the Power BI dashboard to explore the interactive reports and insights.

---

## Future Improvements

- Complete the interactive Power BI dashboard.
- Add more advanced KPIs and DAX measures.
- Automate the data pipeline for scheduled data refresh.
- Extend the project with predictive analytics and forecasting.

---

## Author

**Dhavika Sharma**

Aspiring Data Analyst | Python | SQL | Power BI

- LinkedIn: *www.linkedin.com/in/dhavika-sharma*
- GitHub: *(Add your GitHub profile here)*
