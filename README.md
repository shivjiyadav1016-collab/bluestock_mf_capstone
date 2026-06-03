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