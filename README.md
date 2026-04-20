# Data Analyst Playbook

30 Python + SQL projects I built to practice data analyst workflows from scratch.  
Stack: Python · pandas · matplotlib · seaborn · PostgreSQL

---

## Why I built this

I got tired of tutorials that stop at "here's how groupby works" and never show you what to actually do with it.

So I made this — a set of small projects that each solve one real problem. Cleaning messy data, writing SQL that doesn't fall apart, building charts that make sense, connecting everything into a pipeline. The kind of stuff that comes up in actual analyst work.

Nothing here is perfect. Some things I figured out the hard way. But that's kind of the point.

---

## Projects

### Phase 1 — Python Basics

| # | Project | What I built |
|---|---------|--------------|
| 1 | Sales Summary Script | Load CSV, group by product, sum revenue. Simple, but writing it as a proper script (not a notebook) was the point. |
| 2 | Data Cleaning Script | Null handling, duplicates, type fixes. Wrote it as a reusable script so I could run it on any messy file. |
| 3 | Date-based Sales Analysis | Broke revenue down by month and week. Found out which periods actually performed well vs which just looked fine. |
| 4 | Top Product Report | Ranked products and calculated % contribution. Basically a Pareto analysis — 20% of products usually drive most of the revenue. |
| 5 | Price Distribution Analysis | Descriptive stats + IQR outlier detection. Learned pretty quickly that averages alone are misleading in e-commerce data. |
| 6 | CSV Merger | Automated combining multiple monthly files with column validation. Saves a lot of manual copy-paste work. |
| 7 | Duplicate Order Detector | Catches both exact duplicates and "soft" ones — same customer, same product, ordered within a day. Exports a flagged report. |
| 8 | Automated Report Generator | Outputs a multi-sheet Excel file with formatted headers. Run it once, get a clean report. |

---

### Phase 2 — Visualization

| # | Project | What I built |
|---|---------|--------------|
| 9 | Revenue Trend | Monthly revenue line chart with annotations on the best and worst month. |
| 10 | Category Bar Chart | Top 10 products as a horizontal bar chart with gradient colors and value labels. |
| 11 | Sales Heatmap | Revenue by day of week × week number. Good for spotting which days consistently do better. |
| 12 | Price vs Quantity Scatter | Scatter plot per product with a trend line and correlation in the title. |
| 13 | Multi-panel Dashboard | Four charts in one figure — revenue trend, top products, monthly bars, and a histogram. |

---

### Phase 3 — SQL

| # | Project | What I built |
|---|---------|--------------|
| 14 | PostgreSQL Setup | Loaded 11 Shopee Thailand tables into a local PostgreSQL database using Python. |
| 15 | Aggregation Queries | GROUP BY, HAVING, ORDER BY against real data. Revenue by product, monthly counts, average quantities. |
| 16 | Running Total | SUM() OVER to calculate cumulative revenue without collapsing rows. |
| 17 | Product Ranking | Compared RANK, DENSE_RANK, and ROW_NUMBER side by side. They behave differently with ties. |
| 18 | Month-over-Month Growth | LAG() to pull last month's revenue and calculate growth %. Added a trend label (UP / DOWN / FLAT). |
| 19 | Cohort Analysis | Grouped customers by first purchase month, tracked how many came back each month after. One of the harder SQL problems I've worked through. |

---

### Phase 4 — Python + SQL Together

| # | Project | What I built |
|---|---------|--------------|
| 20 | Python Reads from PostgreSQL | Connected Python to PostgreSQL with SQLAlchemy, ran a query, got a DataFrame back. |
| 21 | ETL Pipeline | Extract → Transform → Load across multiple files. Handles duplicates and logs each step. |
| 22 | Data Quality Checker | Runs 5 checks on any DataFrame: nulls, duplicates, negative values, date range, outliers. Found that 97.85% of order items have no campaign ID — that came from real Shopee data. |
| 23 | Repeat Purchase Analysis | ⬜ Coming soon |
| 24 | A/B Test Analysis | ⬜ Coming soon |

---

### Phase 5 — Portfolio Projects

| # | Project | Status |
|---|---------|--------|
| 25 | Customer Cohort Retention Heatmap | ⬜ Coming soon |
| 26 | RFM Customer Segmentation | ⬜ Coming soon |
| 27 | Sales Forecasting (Moving Average) | ⬜ Coming soon |
| 28 | Marketing Attribution Report | ⬜ Coming soon |
| 29 | Inventory Restock Alert System | ⬜ Coming soon |
| 30 | End-to-end Pipeline + GitHub Publish | ⬜ Coming soon |

---

## Stack

- Python 3.x
- pandas, matplotlib, seaborn, openpyxl
- SQLAlchemy + psycopg2
- PostgreSQL 16

---

## How to run

```bash
pip install pandas matplotlib seaborn openpyxl sqlalchemy psycopg2-binary

# run any project
python3 phase1_python_basics/section1_sales_summary/analysis.py

# load data into PostgreSQL first (needed for Phase 3+)
python3 phase3_sql/section14_postgresql_setup/load_to_postgres.py
```

---

## Structure

```
data-analyst-playbook/
├── phase1_python_basics/
├── phase2_visualization/
├── phase3_sql/
├── phase4_python_sql/
├── charts/
├── reports/
├── .gitignore
└── README.md
```