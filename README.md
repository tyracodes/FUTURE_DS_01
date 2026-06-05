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

- Python
- Streamlit
- GitHub

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
https://futureds01-87ucfb8bx6fcag4egrtuwb.streamlit.app/
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
