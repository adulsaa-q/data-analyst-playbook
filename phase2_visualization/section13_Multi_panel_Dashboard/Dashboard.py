import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# load data (order_date → datetime)
df = pd.read_csv(
    "data/orders_clean_p2.csv",
    parse_dates=['order_date']
)

# create canvas (2x2 dashboard)
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# build monthly revenue
df['month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['revenue'].sum()

# --- panel 1: revenue trend (line)
ax[0, 0].plot(
    monthly_revenue.index.astype(str),  # Period → string for plotting
    monthly_revenue.values
)
ax[0, 0].set_title("Revenue Trend")
ax[0, 0].tick_params(axis='x', rotation=45)  # rotate labels a bit

# --- panel 2: top 10 products (horizontal bar)
top10_products = (
    df.groupby('product')['revenue']
    .sum()
    .nlargest(10)   # pick top 10
    .sort_values()  # sort so bars look cleaner
)

ax[0, 1].barh(
    top10_products.index,
    top10_products.values
)
ax[0, 1].set_title("Top 10 Products")

# show revenue in millions (easier to read)
ax[0, 1].xaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"{x/1_000_000:.2f}M")
)

# --- panel 3: monthly revenue (bar)
ax[1, 0].bar(
    monthly_revenue.index.strftime("%b"),  # Jan, Feb, ...
    monthly_revenue.values
)
ax[1, 0].set_title("Revenue")
ax[1, 0].tick_params(axis='x', rotation=45)

# --- panel 4: revenue distribution
ax[1, 1].hist(df["revenue"], bins=30)
ax[1, 1].set_title("Revenue Distribution")
ax[1, 1].set_xlabel("Revenue")
ax[1, 1].set_ylabel("Number of Orders")

# main title
fig.suptitle("Sales Dashboard")
plt.tight_layout()
plt.savefig("charts/dashboard.png", dpi=200, bbox_inches="tight")
plt.show()