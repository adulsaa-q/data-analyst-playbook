import pandas as pd
from datetime import datetime 

# inspect null counts before cleaning to understand scope of issues
df = pd.read_csv("data/orders_dirty.csv")

# 1. step 1 delete rows duplicates
df = df.drop_duplicates()

# 2. fill null in qty as well median
median_qty = df["Qty"].median()
df["Qty"] = df["Qty"].fillna(median_qty)

#3. fill data product -> Unknow
df["Product"] = df["Product"].fillna("Unknown")

#4. recalculate revenue from Qty and Price to fix nulls caused by missing Qty
df["Revenue"] = df["Qty"] * df["Price"]

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df.columns = df.columns.str.lower() #change str to lower

print(df.isnull().sum())
print(df)
df.to_csv("data/orders_clean.csv",encoding="utf-8",index=False)