# Day 1 Data Quality Summary

- All CSV datasets loaded successfully.
- Dataset shapes, datatypes and sample rows inspected.
- Fund houses, categories, sub-categories and risk grades explored.
- AMFI code validation completed.
- Missing AMFI codes checked between fund_master and nav_history.
- Live NAV data fetched successfully from mfapi.in API.

## 📊 Day 2 - Data Cleaning & Database Setup

### Tasks Completed:
- Cleaned `nav_history.csv`
  - Converted date column to datetime
  - Removed duplicates
  - Filtered invalid NAV values (> 0)
- Cleaned `investor_transactions.csv` (standardization planned)
- Validated `scheme_performance.csv`
- Created SQLite database `bluestock_mf.db`
- Designed and implemented star schema structure
- Loaded cleaned data into SQLite using SQLAlchemy
- Wrote analytical SQL queries for insights
- Created database schema documentation (`schema.sql`)
- Verified data integrity using Python SQL queries

### Key Outputs:
- Cleaned dataset saved in `data/processed/`
- SQLite database created successfully
- Fact table: `fact_nav`
- Schema definition: `sql/schema.sql`
- Query file: `sql/queries.sql`

### Skills Used:
Python, Pandas, SQL, SQLite, SQLAlchemy, Data Cleaning, ETL Pipeline

## 📊 Day 3 – Exploratory Data Analysis (EDA) 

📌 Tasks Completed:
NAV history data analyzed for trend patterns.
Fund-wise performance comparison performed.
Category-wise analysis (Equity, Debt, Hybrid) completed.
AMC-wise AUM distribution evaluated.
Risk-return relationship explored using visualization.
SIP inflow trends analyzed over time.

## 📊 Key Outputs:
NAV trend line chart created for multiple funds.
Category-wise performance comparison charts developed.
AMC-wise AUM distribution visualized.
Clear identification of high-performing fund categories.
Market trend patterns observed from historical NAV data.
## 🛠 Skills Used:

Python, Pandas, Matplotlib, Seaborn, Data Visualization, EDA Techniques

## 📊 Day 4 – Performance Analytics
📌 Tasks Completed:
Calculated key performance metrics:
CAGR
Sharpe Ratio
Sortino Ratio
Alpha
Beta
Maximum Drawdown
Risk-return relationship analyzed using scatter plots.
Fund ranking system developed using composite scoring.
Top performing funds identified based on risk-adjusted returns.
## 📊 Key Outputs:
Risk vs Return scatter plot generated.
Fund scorecard created for ranking funds.
Top 10 performing funds identified.
Performance comparison across categories completed.
Investment risk analysis completed.
## 🛠 Skills Used:

Financial Analytics, Python, Pandas, NumPy, Statistical Analysis, Risk Modeling

## 📊 Day 5 – Power BI Dashboard Development
📌 Tasks Completed:
Built interactive Power BI dashboard.
Created 4 dashboard pages:
Industry Overview
Fund Performance Analysis
Investor Analytics
SIP & Market Trends
Added KPI cards for AUM, SIP inflow, folios, and schemes.
Implemented filters and slicers for interactivity.
Created visualizations for NAV, SIP trends, and fund comparison.
## 📊 Key Outputs:
Fully interactive Power BI dashboard (.pbix file).
KPI cards displaying key industry metrics.
Multi-page dashboard with drill-down capability.
SIP vs Market trend visualization completed.
Category-wise inflow heatmap created.
## 🛠 Skills Used:

Power BI, Data Visualization, Dashboard Design, Business Intelligence

## 📊 Day 6 – Advanced Analytics
📌 Tasks Completed:
Implemented Value at Risk (VaR) analysis for fund risk measurement.
Developed rule-based Fund Recommendation Engine.
Built composite fund scoring model using performance metrics.
Analyzed investor risk profiles and fund suitability.
Final insights and investment recommendations generated.
## 📊 Key Outputs:
VaR-based risk analysis completed for funds.
Fund recommendation logic implemented:
Low Risk → Large Cap Funds
Medium Risk → Flexi Cap Funds
High Risk → Mid Cap Funds
Fund scorecard ranking system finalized.
Top recommended funds identified.
Advanced insights for investment decision-making generated.
## 🛠 Skills Used:

Financial Modeling, Risk Analytics, Python, Statistical Analysis, Recommendation Systems

## 🚀 FINAL STATUS SUMMARY
Day 1 → Data Quality & Exploration ✔
Day 2 → Data Cleaning & SQLite Setup ✔
Day 3 → EDA Analysis ✔
Day 4 → Performance Analytics ✔
Day 5 → Power BI Dashboard ✔
Day 6 → Advanced Analytics ✔
## 🏁 RESULT

👉 End-to-end Mutual Fund Analytics Project completed
👉 Data pipeline + analytics + dashboard + insights all done
👉 Industry-ready capstone project