import pandas as pd
import matplotlib.pyplot as plt

# load dataset and parse order_date as datetime
df = pd.read_csv(
    "data/orders_clean_p2.csv",
    parse_dates=["order_date"]
)

# validate required columns exist
assert "order_date" in df.columns
assert "revenue" in df.columns

# create month column (YYYY-MM format)
df["month"] = df["order_date"].dt.to_period("M")

# group by month and calculate total revenue
monthly_revenue = (
    df.groupby("month")
    .agg(total_revenue=("revenue", "sum"))
    .sort_index()       # keep timeline order
    .reset_index()      # convert index back to column
)

# create figure
fig, ax = plt.subplots()

# plot line chart
ax.plot(
    monthly_revenue["month"].astype(str),   # x = month
    monthly_revenue["total_revenue"],       # y = revenue
    marker="o"                              # show point markers
)

# set chart labels
ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")

# find row with highest and lowest revenue
max_row = monthly_revenue.loc[monthly_revenue["total_revenue"].idxmax()]
min_row = monthly_revenue.loc[monthly_revenue["total_revenue"].idxmin()]

# highlight highest point (optional but helps visibility)
ax.scatter(
    str(max_row["month"]),
    max_row["total_revenue"],
    color="red",
    zorder=3
)

# annotate highest point
ax.annotate(
    "Highest",
    xy=(str(max_row["month"]), max_row["total_revenue"]),  # exact point
    xytext=(0, 10),                                       # move text up
    textcoords="offset points",                           # use pixel offset
    ha="center"
)

# annotate lowest point
ax.annotate(
    "Lowest",
    xy=(str(min_row["month"]), min_row["total_revenue"]),
    xytext=(0, -15),                                      # move text down
    textcoords="offset points",                           # fixed: must be 'points'
    ha="center"
)

# rotate x labels for better readability
plt.xticks(rotation=45)

# adjust layout to prevent overlap
plt.tight_layout()

plt.savefig("charts/revenue_trend.png", dpi=150)
plt.show()