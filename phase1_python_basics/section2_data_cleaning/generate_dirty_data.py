import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Prevent errors if the folder doesn't exist yet.
os.makedirs("data", exist_ok=True)

products = ["Keyboard", "Mouse", "Paper", "Pen", None]  # มี None ปน
start_date = datetime(2024, 1, 1)

data = []

# build 3000 rows first
for i in range(1, 3000):
    product = random.choice(products)
    qty = random.choice([1, 2, 3, 4, 5, None])  # มี null
    price = random.choice([20, 50, 120, 300, 800])

    revenue = qty * price if qty is not None else None

    order_date = (start_date + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

    data.append({
        "Order_ID": i,
        "Product": product,
        "Qty": qty,
        "Price": price,
        "Revenue": revenue,
        "Order_Date": order_date
    })

# change DataFrame
df = pd.DataFrame(data)

# บังคับให้มี null เพิ่ม (เผื่อสุ่มไม่พอ)
for i in random.sample(range(len(df)), 5):
    df.loc[i, "Product"] = None

for i in random.sample(range(len(df)), 5):
    df.loc[i, "Qty"] = None
    df.loc[i, "Revenue"] = None

# build duplicate 20 row
duplicates = df.sample(20, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# save
df.to_csv("data/orders_dirty.csv", index=False)

print(f"สร้างไฟล์แล้ว: {len(df)} แถว")
df.isnull().sum()   # นับ null ต่อ column
df.info()           # overview dtypes + non-null count