# E-commerce Sales Performance Analytics

This project is an end-to-end analysis of a superstore's sales data, designed to uncover actionable insights into customer behavior, product performance, and sales trends. The goal is to provide data-driven recommendations to guide the company's strategic planning.

### Business Problem
A growing e-commerce company needs to move beyond basic reporting to deeply understand its business. Stakeholders need to identify key customer segments, optimize the product catalog by removing unprofitable items, understand seasonal sales patterns, and discover opportunities for growth.

---

### 🛠️ Technical Stack
*   **Database:** PostgreSQL
*   **Data Processing & Analysis:** Python (Pandas, SQLAlchemy)
*   **Data Visualization:** Tableau

---

### 📋 Project Workflow

1.  **Data Ingestion and Cleaning:** A Python script was developed to read the raw CSV data, clean column names for consistency, convert date fields to the correct data type, and handle initial data quality checks.
2.  **Database Loading:** The cleaned data was loaded into a PostgreSQL database using Python (SQLAlchemy), creating a robust and queryable single source of truth.
3.  **SQL Analysis:** Advanced SQL queries were executed to perform initial analysis, including aggregating sales by month (seasonal trends) and analyzing profitability by product category.
4.  **Advanced Analytics in Python:** Data was pulled from PostgreSQL into a Python environment to perform an RFM (Recency, Frequency, Monetary) analysis, segmenting all customers into actionable groups like 'Champions' and 'At Risk'.
5.  **Interactive Visualization:** The final, enriched dataset was connected to Tableau to build a comprehensive, multi-worksheet dashboard designed for stakeholder exploration.

---

### 📊 Key Insights & Recommendations

*   **Product Profitability Anomaly:** The "Tables" sub-category generates significant sales but operates at a substantial net loss. **Recommendation:** Immediately review the pricing, shipping costs, and supplier costs for all products in this category.
*   **High-Value Customer Segments:** The RFM analysis identified a core group of 167 'Champions' and 163 'Loyal Customers'. **Recommendation:** Launch a loyalty program and exclusive offers to retain and reward these high-value segments.
*   **At-Risk Customer Identification:** The dashboard highlights 146 customers in the 'At Risk' segment who were previously valuable but have not purchased recently. **Recommendation:** Deploy a targeted "win-back" email campaign with a special offer to re-engage this cohort.
*   **Seasonal Sales Peaks:** Sales and profits consistently peak in the final quarter (October-December). **Recommendation:** Plan inventory and marketing campaigns to maximize revenue during this predictable peak season.

---

### 🚀 Live Dashboard

**[➡️ View the Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/abhinav.faldu/viz/E-CommerceSales_17564669089680/Dashboard1)**

*(Replace the above URL with the link to your published Tableau dashboard.)*

---

### 📁 How to Run this Project Locally

1.  **Prerequisites:** Ensure you have Python, PostgreSQL, and Tableau installed.
2.  **Clone Repository:** `git clone https://github.com/Abhinavfaldu082/E-commerce_sales`
3.  **Install Libraries:** `pip install pandas sqlalchemy psycopg2-binary`
4.  **Database Setup:** Create a PostgreSQL database named `ecommerce_db`.
5.  **Load Data:** Update the `db_password` in `load_data.py` and run the script: `python load_data.py`.
6.  **Run Analysis:** Update the `db_password` in `analyze.py` and run the script: `python analyze.py`. This will generate the `superstore_with_rfm.csv` file.
7.  **Visualize:** Open the generated CSV file in Tableau and use it as the data source to build the dashboard.