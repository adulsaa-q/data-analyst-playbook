import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


df = pd.read_csv(
    "data/orders_all.csv",
    encoding="utf-8",
    parse_dates=["order_date"]
)

assert "order_date" in df.columns

df["day_of_week"] = df["order_date"].dt.day_name()
df["week_number"] = df["order_date"].dt.isocalendar().week

pivot = df.pivot_table(
    index= "day_of_week",
    columns="week_number",
    values = "revenue",
    aggfunc = "sum"
)

order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
pivot = pivot.reindex(order)

fig, ax = plt.subplots(figsize=(14, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=",.0f",
    cmap="YlGn",
    ax=ax
)

plt.title("revenue Day of Week")
plt.tight_layout()
plt.savefig("charts/sales_heatmap.png", dpi=150)
plt.show()