import pandas as pd

df = pd.read_csv("data/orders.csv")

summary = (
    df.groupby("product")
    .agg(
        total_revenue=("revenue", "sum"),
        total_qty=("qty", "count")
    )
    .sort_values(by="total_revenue", ascending=False)
)

# format ตัวเลข (comma)
summary["total_revenue"] = summary["total_revenue"].map(lambda x: f"{x:,}")

print(summary)