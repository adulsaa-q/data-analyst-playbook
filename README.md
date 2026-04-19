# 📊 Data Analyst Playbook

> 30 Python × SQL projects — built to practice real analyst workflows from scratch.  
> Stack: Python · pandas · matplotlib · seaborn · PostgreSQL

---

## Why I built this

Wanted a structured way to go from "I know pandas a bit" to actually being able to handle data end-to-end — cleaning, analysis, visualization, SQL, and pipelines. Each project is small enough to finish in one sitting but covers something real.

---

## Progress

### Phase 1 — Python Fundamentals

| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 1 | Sales Summary Script | 🟢 Easy | ✅ Done |
| 2 | Data Cleaning Script | 🟢 Easy | ✅ Done |
| 3 | Date-based Sales Analysis | 🟢 Easy | ✅ Done |
| 4 | Top Product Report | 🟢 Easy | ✅ Done |
| 5 | Price Distribution Analysis | 🟢 Easy | ✅ Done |
| 6 | CSV Merger | 🟢 Easy | ✅ Done |
| 7 | Duplicate Order Detector | 🟢 Easy | ✅ Done |
| 8 | Automated Report Generator | 🟡 Medium | ✅ Done |

### Phase 2 — Data Visualization

| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 9 | Revenue Trend (Line Chart) | 🟢 Easy | ✅ Done |
| 10 | Category Distribution (Bar Chart) | 🟢 Easy | ✅ Done |
| 11 | Sales Heatmap | 🟡 Medium | ✅ Done |
| 12 | Price vs Quantity (Scatter Plot) | 🟡 Medium | ✅ Done |
| 13 | Multi-panel Dashboard | 🟡 Medium | ✅ Done |

### Phase 3 — SQL

| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 14 | PostgreSQL Setup & Data Loading | 🟢 Easy | ✅ Done |
| 15 | Basic Aggregation Queries | 🟢 Easy | ✅ Done |
| 16 | Running Total (Window Functions) | 🟡 Medium | ✅ Done |
| 17 | Product Ranking | 🟡 Medium | ✅ Done |
| 18 | Month-over-Month Growth (MoM) | 🟡 Medium | ✅ Done |
| 19 | Cohort Analysis | 🔴 Hard | ✅ Done |

### Phase 4 — Python + SQL Integration

| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 20 | Python Reads from PostgreSQL | 🟡 Medium | ⬜ Pending |
| 21 | ETL Pipeline Script | 🟡 Medium | ⬜ Pending |
| 22 | Data Quality Checker | 🟡 Medium | ⬜ Pending |
| 23 | Repeat Purchase Analysis | 🟡 Medium | ⬜ Pending |
| 24 | A/B Test Analysis | 🔴 Hard | ⬜ Pending |

### Phase 5 — Portfolio Projects

| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 25 | Customer Cohort Retention Heatmap | 🔴 Hard | ⬜ Pending |
| 26 | RFM Customer Segmentation | 🔴 Hard | ⬜ Pending |
| 27 | Sales Forecasting (Moving Average) | 🔴 Hard | ⬜ Pending |
| 28 | Marketing Attribution Report | 🔴 Hard | ⬜ Pending |
| 29 | Inventory Restock Alert System | 🔴 Hard | ⬜ Pending |
| 30 | End-to-end Pipeline + GitHub Publish | 🔴 Hard | ⬜ Pending |

---

## Tech Stack

- **Python 3.x**
- **pandas** — data manipulation
- **matplotlib / seaborn** — visualization
- **openpyxl** — Excel output
- **sqlalchemy / psycopg2** — PostgreSQL connection
- **PostgreSQL 16** — used from Phase 3 onward

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
│
├── phase2_visualization/
│   ├── section9_revenue_trend/
│   ├── section10_category_bar_chart/
│   ├── section11_sales_heatmap/
│   ├── section12_price_qty_scatter/
│   └── section13_dashboard/
│
├── phase3_sql/
│   ├── section14_postgresql_setup/
│   ├── section15_aggregation/
│   ├── section16_running_total/
│   ├── section17_product_ranking/
│   ├── section18_mom_growth/
│   └── section19_cohort_analysis/
│
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
python phase1_python_basics/section1_sales_summary/analysis.py

# load data into PostgreSQL (required for Phase 3+)
python phase3_sql/section14_postgresql_setup/load_to_postgres.py
```