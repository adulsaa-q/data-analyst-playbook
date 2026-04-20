import pandas as pd
import numpy as np
from pathlib import Path

data_path = Path("phase4_python_sql/section21_etl_pipeline/data")


# extract report_date from file header (hidden in top rows of csv)
def extract_report_date(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        lines = [next(f) for _ in range(6)]

        raw_date = lines[5]
        date_str = raw_date.split(",")[1].split(" ")[0].strip()

        return pd.to_datetime(date_str, format="%d/%m/%Y").date()


# load raw csv (skip non-data header rows)
def load_data(file_path):
    return pd.read_csv(file_path, skiprows=7, encoding="utf-8-sig")


# clean + transform dataset into usable format
def transform(df, report_date):
    # trim column names (avoid hidden spaces issues)
    df.columns = df.columns.str.strip()

    # replace "-" with NaN (proper missing value)
    df = df.replace("-", np.nan)

    # rename columns (Thai → English standard schema)
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

    # add metadata columns
    df["platform"] = "Shopee"
    df["report_date"] = report_date

    # keep only required columns (remove noise)
    return df[
        ["report_date","platform","ad_name","ad_type",
        "clicks","orders","ad_spend","revenue"]
    ]


# loop through all csv files in folder
all_file = []
seen_dates = set()


for file in data_path.glob("*.csv"):
    try:
        # extract report date first
        report_date = extract_report_date(file)

        # skip if date already processed (avoid duplicates)
        if report_date in seen_dates:
            print(f"Skip {file.name} — date {report_date} already loaded")
            continue

        seen_dates.add(report_date)

        # load and transform
        df = load_data(file)
        df = transform(df, report_date)

        all_file.append(df)

    except Exception as e:
        # prevent pipeline from breaking on single file error
        print(f"error in {file}: {e}")


# combine all dataframes into final dataset
final_df = pd.concat(all_file, ignore_index=True)
# export clean dataset
output_path = f"phase4_python_sql/section21_etl_pipeline/data_clean/shopee_ads_clean_{pd.Timestamp.today().date()}.csv"
final_df.to_csv(output_path, index=False)
# final summary
print(f"Done! {len(final_df)} rows, {len(all_file)} files loaded.")