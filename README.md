# 📊 Data Analyst Playbook

> 30 Python × SQL projects for building real-world data analyst skills.  
> Stack: Python · pandas · matplotlib · seaborn · PostgreSQL

---

## 🚀 Progress

### Phase 1 — Python Basics
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

### Phase 2 — Visualization
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 9 | Revenue Trend Line Chart | 🟢 Easy | ✅ Done |
| 10 | Category Bar Chart | 🟢 Easy | ✅ Done |
| 11 | Sales Heatmap | 🟡 Medium | ✅ Done |
| 12 | Price vs Quantity Scatter | 🟡 Medium | ⬜ Next |
| 13 | Multi-panel Dashboard Figure | 🟡 Medium | ⬜ |

### Phase 3 — SQL
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 14 | Setup + Load Data to PostgreSQL | 🟢 Easy | ⬜ |
| 15 | Basic Aggregation Queries | 🟢 Easy | ⬜ |
| 16 | Running Total with Window Function | 🟡 Medium | ⬜ |
| 17 | Product Ranking Query | 🟡 Medium | ⬜ |
| 18 | MoM Growth Query | 🟡 Medium | ⬜ |
| 19 | Cohort Analysis in SQL | 🔴 Hard | ⬜ |

### Phase 4 — Python + SQL Combined
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 20–24 | Python + SQL Projects | 🟡–🔴 | ⬜ |

### Phase 5 — Portfolio
| # | Project | Difficulty | Status |
|---|---------|------------|--------|
| 25–30 | Portfolio Projects | 🔴 Hard | ⬜ |

---

## 🛠️ Stack

- **Python** 3.x
- **pandas** — data manipulation & analysis
- **matplotlib / seaborn** — visualization
- **openpyxl** — Excel report generation
- **PostgreSQL 16** — coming in Phase 3

---

## 📁 Structure

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
│   └── section8_ExcelWriter_openpyxl/
├── phase2_visualization/
│   ├── section9_revenue_trend/
│   ├── section10_CategoryBar_Chart/
│   └── section11_sales_heatmap/
├── charts/
├── reports/
├── data/               # .gitignored
└── README.md
```

---

## ⚙️ How to Run

```bash
# Install dependencies
pip install pandas matplotlib seaborn openpyxl

# Run any project
python phase1_python_basics/section1_sales_summary/analysis.py
```