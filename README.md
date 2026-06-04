# Business Sales Performance Analytics

## Future Interns Task 1

This project analyzes Superstore sales data to identify:

- Revenue trends
- Top-selling products
- Most profitable categories
- Regional performance
- Business growth opportunities

## Dataset

Dataset: Superstore Sales Dataset

Source:
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

## Tools Used

- Microsoft Excel
- Power BI
- GitHub

## Project Structure

FUTURE_DS_01
│
├── data
├── dashboard
├── images
├── report
└── README.md

## Project Status

Data cleaning in progress.
## Data Cleaning Process

The dataset was cleaned using Python (Pandas in Google Colab).

### Steps Performed:
- Removed duplicate records
- Converted Order Date and Ship Date to datetime format
- Created new analysis columns:
  - Order Year
  - Order Month
  - Month-Year
  - Profit Margin
- Handled missing and infinite values
- Exported cleaned dataset for analysis
## Key Features Created

- Order Year extracted from Order Date
- Month-Year for trend analysis
- Profit Margin calculated for business insights

##  Live Dashboard

This project is deployed using Streamlit Cloud.

Live App Link for the dashboard for task 1:
https://futureds01-ymfqdedaarwcvhnpx8t2ky.streamlit.app/
## Business Insights

After analyzing the Superstore dataset, the following key insights were discovered:

###  1. Best Performing Category
- Technology is the highest revenue-generating category.
- It also contributes significantly to overall profit.
- This indicates strong customer demand for tech-related products.

###  2. Weak / Low Performing Category
- Furniture shows lower profit margins compared to other categories.
- Some furniture products even generate losses due to high discounts or costs.
- This category needs pricing or cost optimization.

###  3. Regional Performance
- The West region performs the best in terms of both sales and profit.
- The South region underperforms compared to others.
- This suggests an opportunity for targeted marketing in weaker regions.

###  4. Product Performance
- A small number of products generate the majority of sales (Pareto principle).
- Several products contribute very low or negative profit.
- These products should be reviewed or discontinued.

###  5. Sales Trends
- Sales fluctuate across months, showing seasonal patterns.
- Certain months show higher demand, indicating peak business periods.

---

##  Recommendations

Based on the analysis, the following actions are recommended:

- Focus marketing and investment on the Technology category.
- Review pricing strategy for Furniture products to improve profitability.
- Strengthen sales strategy in the South region.
- Reduce discounts on loss-making products.
- Increase stock availability during high-demand months.
- 
#  Customer Retention & Churn Analysis Dashboard (task 2)

##  Live Dashboard
Click here to view the interactive dashboard:  
https://futureds01-dwqbshck6yhwf5vmglp7p4.streamlit.app/

---

##  Project Overview

This project analyzes customer churn behavior for a subscription-based telecom company.  
The goal is to understand why customers leave, identify retention drivers, and measure customer lifetime value (CLV).

The insights are presented through an interactive Streamlit dashboard.

---

##  Objectives

- Identify overall churn rate
- Understand churn patterns across customer segments
- Analyze retention based on tenure and contract type
- Measure customer lifetime value (CLV)
- Provide actionable business recommendations

---

##  Dataset

Telco Customer Churn Dataset  
Source: Kaggle

The dataset includes:
- Customer demographics
- Subscription details
- Contract type
- Payment method
- Monthly charges
- Tenure
- Churn status

---

##  Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

---

## Key Insights

- Overall churn rate is ~26.58%
- Month-to-month customers are most likely to churn
- Electronic check users have the highest churn rate
- Customers with long tenure are highly retained
- Average Customer Lifetime Value is ~$2,283

---

##  Business Recommendations

- Encourage customers to switch from month-to-month to yearly contracts
- Improve onboarding experience during the first 12 months
- Target high-risk payment methods with retention offers
- Introduce loyalty rewards for long-term customers

---

##  Author

Built as part of Data Science & Analytics Task 2 (Future Interns)
