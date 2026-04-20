# 📊 Data Analyst Playbook

> 30 Python × SQL projects — focused on building real-world data analyst skills  
> Stack: Python · pandas · matplotlib · seaborn · PostgreSQL

---

## Why I built this

I wanted something more structured than random tutorials.

At some point, just “knowing pandas” isn’t enough — you need to be able to work with data end-to-end: clean it, analyze it, visualize it, and query it properly with SQL.

Most learning resources use small, clean datasets. That’s not how real data looks.  
So I built this playbook to practice workflows that are closer to actual work — a bit messy, a bit repetitive, but useful.

Each project is small enough to finish in one sitting, but focused on something you’ll actually use on the job.

---

## Progress

### Phase 1 — Python Fundamentals

Getting comfortable with pandas and building small but complete analysis scripts.

| # | Project | What it does & why it matters |
|---|---------|-------------------------------|
| 1 | Sales Summary Script | Basic grouping + aggregation from a CSV. Simple, but something you’ll do constantly. Focus was writing clean scripts, not one-off notebook code. |
| 2 | Data Cleaning Script | Real data is messy. Covers null handling, deduplication, type fixes, and column cleanup. Built as a reusable script. |
| 3 | Date-based Sales Analysis | Breaks revenue down by time (month/week). Helps understand trends instead of just totals. |
| 4 | Top Product Report | Ranks products and calculates contribution %. Foundation for Pareto-style analysis. |
| 5 | Price Distribution Analysis | Uses descriptive stats + IQR to understand how values are distributed, not just averages. |
| 6 | CSV Merger | Combines multiple files with basic validation. Saves manual work when dealing with recurring data. |
| 7 | Duplicate Order Detector | Finds both exact and “soft” duplicates. Useful for catching data issues early. |
| 8 | Automated Report Generator | Outputs a formatted Excel report. Goal: one script → ready-to-use output. |

---

### Phase 2 — Data Visualization

Turning raw numbers into something readable.

| # | Project | What it does & why it matters |
|---|---------|-------------------------------|
| 9 | Revenue Trend (Line Chart) | Plots revenue over time with simple annotations. Helps make trends obvious. |
| 10 | Category Distribution (Bar Chart) | Clean bar chart with labels. Focus on readability, not just plotting. |
| 11 | Sales Heatmap | Shows patterns across days/weeks. Useful for spotting consistent behavior. |
| 12 | Price vs Quantity (Scatter Plot) | Explores relationship between variables. Adds basic correlation insight. |
| 13 | Multi-panel Dashboard | Combines multiple charts into one view. Simulates a quick business summary. |

---

### Phase 3 — SQL

Moving from pandas to querying real data in PostgreSQL.

| # | Project | What it does & why it matters |
|---|---------|-------------------------------|
| 14 | PostgreSQL Setup & Data Loading | Sets up database + loads Shopee data using Python. Foundation for SQL work. |
| 15 | Basic Aggregation Queries | GROUP BY, HAVING, ORDER BY — core queries used in almost every task. |
| 16 | Running Total (Window Functions) | Uses SUM() OVER to calculate cumulative values without collapsing rows. |
| 17 | Product Ranking | Compares RANK, DENSE_RANK, ROW_NUMBER. Helps understand differences clearly. |
| 18 | Month-over-Month Growth | Uses LAG() to calculate growth and label trends (UP / DOWN / FLAT). |
| 19 | Cohort Analysis | Tracks customer retention by cohort. One of the more complex SQL tasks. |

---

### Phase 4 — Python + SQL Integration

Combining both tools into simple workflows.

| # | Project | What it does & why it matters |
|---|---------|-------------------------------|
| 20 | Python Reads from PostgreSQL | Runs SQL from Python and loads into pandas. Connects both worlds. |
| 21 | ETL Pipeline Script | Basic Extract → Transform → Load flow. Handles multiple files and logging. |
| 22 | Data Quality Checker | Checks nulls, duplicates, negatives, date range, and outliers. Simple but very useful. |
| 23 | Repeat Purchase Analysis | ⬜ Pending |
| 24 | A/B Test Analysis | ⬜ Pending |

---

### Phase 5 — Portfolio Projects

End-to-end projects combining everything.

| # | Project | What it does & why it matters |
|---|---------|-------------------------------|
| 25 | Customer Cohort Retention Heatmap | ⬜ Pending |
| 26 | RFM Customer Segmentation | ⬜ Pending |
| 27 | Sales Forecasting (Moving Average) | ⬜ Pending |
| 28 | Marketing Attribution Report | ⬜ Pending |
| 29 | Inventory Restock Alert System | ⬜ Pending |
| 30 | End-to-end Pipeline + GitHub Publish | ⬜ Pending |

---

## Tech Stack

- Python 3.x  
- pandas — data manipulation  
- matplotlib / seaborn — visualization  
- openpyxl — Excel reports  
- sqlalchemy / psycopg2 — database connection  
- PostgreSQL — database

---

## Project Structure


```
data-analyst-playbook/
├── phase1_python_basics/
│   ├── section1_sales_summary/
│   ├── section2_data_cleaning/
│   ├── section3_date_analysis/
│   ├── section4_top_product/
│   ├── section5_price_distribution/
│   ├── section6_csv_merger/
│   ├── section7_duplicate_detector/
│   └── section8_excel_writer/
├── phase2_visualization/
│   ├── section9_revenue_trend/
│   ├── section10_category_bar_chart/
│   ├── section11_sales_heatmap/
│   ├── section12_price_qty_scatter/
│   └── section13_dashboard/
├── phase3_sql/
│   ├── section14_postgresql_setup/
│   ├── section15_aggregation/
│   ├── section16_running_total/
│   ├── section17_product_ranking/
│   ├── section18_mom_growth/
│   └── section19_cohort_analysis/
├── phase4_python_sql/
│   ├── section20_python_reads_postgres/
│   ├── section21_etl_pipeline/
│   ├── section22_data_quality/
│   └── ...
├── charts/
├── reports/
├── .gitignore
└── README.md
```

---

## How to Run

```bash
# install dependencies
pip install pandas matplotlib seaborn openpyxl sqlalchemy psycopg2-binary

# run any project
python3 phase1_python_basics/section1_sales_summary/analysis.py

# load data into PostgreSQL (required for Phase 3+)
python3 phase3_sql/section14_postgresql_setup/load_to_postgres.py
```