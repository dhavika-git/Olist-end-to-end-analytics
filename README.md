# Olist End-to-End E-Commerce Analytics

## Overview
This project is an end-to-end data analytics case study built using the Olist Brazilian E-Commerce dataset. The main goal of this project is to understand the complete analytics workflow, starting from raw data cleaning and feature engineering to SQL analysis and Power BI dashboard creation. Through this project, I explored different business problems and converted raw data into meaningful insights that can help support business decisions.

## Business Problem
Olist is a Brazilian e-commerce marketplace that connects customers with sellers. The company wants to better understand its business performance by answering questions such as:

- Which product categories generate the highest revenue?
- Which customers and sellers contribute the most to sales?
- Does delivery delay affect customer satisfaction?
- Which payment methods are most popular among customers?
- Which regions need improvements in delivery and logistics?

## Tech Stack
- Python
- Pandas
- NumPy
- MySQL
- Power BI
- Git
- GitHub

## Dataset
This project uses the **Olist Brazilian E-Commerce Dataset** available on Kaggle. The analysis is performed using multiple related datasets, including:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Order Payments
- Order Reviews
- Product Category Translation
- Geolocation

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
Business Insights 
```
## Data Cleaning & Feature Engineering
The project started by cleaning the raw datasets using Python. During this process, I checked for duplicate records, handled missing values, corrected data types, and converted date columns into the appropriate format. After cleaning, I created several new features such as delivery days, delivery delay, purchase month, weekend orders, installment indicators, product volume, freight percentage, and review categories. These additional features helped in performing more meaningful business analysis.

## Power BI Dashboard
The Power BI dashboard brings together the complete analysis in an interactive format. It includes:

- Executive overview with important business KPIs
- Sales analysis to track revenue and order trends
- Customer analysis to understand purchasing behaviour and repeat customers
- Product performance analysis across different categories
- Seller performance analysis based on revenue and ratings
- Delivery & logistics analysis to monitor delivery performance and delays
- Payment & customer satisfaction analysis using payment methods and review scores
- Drill-through pages for detailed Product, Seller, and Customer information
- Interactive filters for Year, Quarter, and Month to explore the data from different perspectives

## Key Insights
Some of the key findings from the analysis are:

- Generated 16.01M in total revenue from nearly 99K orders.
- Credit Card was the most frequently used payment method and contributed the highest revenue.
- Beleza Saude was the top-performing product category in terms of revenue.
- Most customers made only one purchase, indicating an opportunity to improve customer retention.
- Delivery delays were associated with lower customer review scores.
- A small number of sellers contributed a large share of the overall revenue.

## Recommendations
Based on the analysis, the following improvements can be considered:

- Increase customer retention through loyalty programs and personalized offers.
- Improve delivery performance in regions with longer delivery times.
- Focus on improving product categories that generate good sales but receive lower ratings.
- Continue supporting high-performing sellers while helping other sellers improve their performance.
- Use the dashboard to monitor key business metrics and identify trends over time.

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

## How to Run
1. Download the Olist Brazilian E-Commerce dataset.
2. Run the Python scripts to clean the data and create additional features.
3. Import the cleaned datasets into MySQL.
4. Execute the SQL scripts to perform business analysis.
5. Open the Power BI dashboard to explore the interactive reports and insights.

## Author

**Dhavika Sharma**

Aspiring Data Analyst | Python | SQL | Power BI

- LinkedIn: *www.linkedin.com/in/dhavika-sharma*
- GitHub: *(Add your GitHub profile here)*
