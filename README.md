# 📊 Data Analyst Playbook

> A collection of 30 Python × SQL projects designed to build real-world data analyst skills.  
> Tech stack: Python · pandas · matplotlib · seaborn · PostgreSQL

---

## 🎯 Objective

This playbook is designed to simulate real-world data analyst workflows,
covering data cleaning, analysis, visualization, and database integration.

---

## 🚀 Progress

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

---

### Phase 2 — Data Visualization
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 9 | Revenue Trend (Line Chart) | 🟢 Easy | ✅ Done |
| 10 | Category Distribution (Bar Chart) | 🟢 Easy | ✅ Done |
| 11 | Sales Heatmap | 🟡 Medium | ✅ Done |
| 12 | Price vs Quantity (Scatter Plot) | 🟡 Medium | ✅ Done |
| 13 | Multi-panel Dashboard | 🟡 Medium | ✅ Done |

---

### Phase 3 — SQL
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 14 | PostgreSQL Setup & Data Loading | 🟢 Easy | ✅ Done |
| 15 | Basic Aggregation Queries | 🟢 Easy | ⬜ Pending |
| 16 | Running Total (Window Functions) | 🟡 Medium | ⬜ Pending |
| 17 | Product Ranking | 🟡 Medium | ⬜ Pending |
| 18 | Month-over-Month Growth (MoM) | 🟡 Medium | ⬜ Pending |
| 19 | Cohort Analysis | 🔴 Hard | ⬜ Pending |

---

### Phase 4 — Python + SQL Integration
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 20–24 | End-to-End Python + SQL Projects | 🟡–🔴 | ⬜ Pending |

---

### Phase 5 — Portfolio Projects
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 25–30 | Portfolio-ready Case Studies | 🔴 Hard | ⬜ Pending |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **pandas** — data manipulation & analysis  
- **matplotlib / seaborn** — data visualization  
- **openpyxl** — Excel report generation  
- **sqlalchemy / psycopg2** — PostgreSQL integration  
- **PostgreSQL 16** — used from Phase 3 onward  

---

## 📁 Project Structure

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
│   └── section14_postgresql_setup/
│       ├── data/        # ignored via .gitignore
│       ├── sql/
│       └── load_to_postgres.py
│
├── charts/
├── reports/
├── .gitignore
└── README.md

---

## ⚙️ How to Run

```bash
# install dependencies
pip install pandas matplotlib seaborn openpyxl sqlalchemy psycopg2-binary

# run a project
python phase1_python_basics/section1_sales_summary/analysis.py

# load data into PostgreSQL (Phase 3)
python phase3_sql/section14_postgresql_setup/load_to_postgres.py