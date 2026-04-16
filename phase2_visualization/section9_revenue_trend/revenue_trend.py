import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/orders_clean_p2.csv",
    parse_dates=["order_date"]
)

# validate
assert "order_date" in df.columns
assert "revenue" in df.columns

df["month"] = df["order_date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("month")
    .agg(total_revenue=("revenue", "sum"))
    .sort_index()
    .reset_index()
)

fig, ax = plt.subplots()

ax.plot(
    monthly_revenue["month"].astype(str),
    monthly_revenue["total_revenue"],
    marker="o"
)

ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")

# find max row and min
max_row = monthly_revenue.loc[monthly_revenue["total_revenue"].idxmax()]
min_row = monthly_revenue.loc[monthly_revenue["total_revenue"].idxmin()]

# annotate max
ax.annotate(
    "Highest",
    xy=(str(max_row["month"]),max_row["total_revenue"]),
    xytext=(0,10),
    textcoords=("offset points"),
    ha= "center"
)

# annotate min
ax.annotate(
    "Lowest",
    xy=(str(min_row["month"]),min_row["total_revenue"]),
    xytext=(0,-15),
    textcoords=("offset point"),
    ha="center"
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/revenue_trend.png",dpi=150)
plt.show()