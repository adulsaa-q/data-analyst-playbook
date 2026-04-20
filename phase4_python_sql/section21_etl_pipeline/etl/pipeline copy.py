import pandas as pd
import numpy as np

df = pd.read_csv("phase4_python_sql/section21_etl_pipeline/data/AdSp2026.3.1.csv",skiprows=7,encoding="utf-8-sig")

# Extract date 
with open("phase4_python_sql/section21_etl_pipeline/data/AdSp2026.3.1.csv",encoding="utf-8-sig") as f:
    lines = [next(f) for _ in range(6)]

raw_date = lines[5]
date_str = raw_date.split(",")[1].split(" ")[0].strip()
report_date = pd.to_datetime(date_str,format="%d/%m/%Y").date()

df["platform"] = "Shopee"
df["report_date"] = report_date
df = df.replace("-", np.nan)
df.columns = df.columns.str.strip()
df = df.rename(columns={
    "ชื่อโฆษณา": "ad_name",
    "ประเภทโฆษณา": "ad_type",
    "การมองเห็น": "impressions",
    "จำนวนคลิก": "clicks",
    "อัตราการคลิก (CTR)": "ctr",
    "การสั่งซื้อ": "orders",
    "ยอดขาย": "revenue",
    "ค่าโฆษณา": "ad_spend",
    "ยอดขาย/รายจ่าย (ROAS)": "roas",
    "ACOS": "acos"
})

df = df[["report_date","platform","ad_name","ad_type","clicks","orders","ad_spend","revenue"]]
print(df.head())
