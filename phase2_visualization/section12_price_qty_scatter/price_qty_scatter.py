import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# load CSV file and parse order_date as datetime
df = pd.read_csv("data/orders_clean_p2.csv", encoding='utf-8', parse_dates=['order_date'])

# check that required columns exist
assert "order_date" in df.columns
assert all(col in df.columns for col in ["price", "qty", "product"])

# build figure (canvas) and axis
fig, ax = plt.subplots(figsize=(10, 6))

# get unique product names
products = df['product'].unique()

# generate colors (one color per product)
colors = cm.tab10(np.linspace(0, 1, len(products)))

# loop each product and plot scatter
for i, product in enumerate(products):  # i = index, product = name
    subset = df[df['product'] == product]  # filter data for each product
    
    # plot price (x) vs qty (y)
    ax.scatter(
        subset["price"],
        subset["qty"],
        label=product,      # show product name in legend
        color=colors[i]     # assign color by index
    )

# trend line — fit linear relationship between price and qty
coeffs = np.polyfit(df['price'], df['qty'], deg=1)  # get slope and intercept
trend_line = np.poly1d(coeffs)  # convert to function

# create x values for smooth line
x_range = np.linspace(df['price'].min(), df['price'].max(), 100)

# plot trend line
ax.plot(
    x_range,
    trend_line(x_range),
    color="red",
    linewidth=2,
    label="Trend"
)

# calculate correlation between price and qty
corr = df['price'].corr(df['qty'])

# set labels and title
ax.set_xlabel("Price")
ax.set_ylabel("Quantity")
ax.set_title(f"Price vs Quantity (r = {corr:.2f})")  # show correlation in title

# show legend
ax.legend()

# adjust layout to prevent overlap
plt.tight_layout()
plt.savefig("charts/price_qty_scatter.png", dpi=150, bbox_inches="tight")
plt.show()