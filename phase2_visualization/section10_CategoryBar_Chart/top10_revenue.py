import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# load data and parse order_date as datetime
df = pd.read_csv(
    "data/orders_all.csv",
    parse_dates=['order_date']
)

# check required columns exist in the dataset
required_cols = ['revenue', 'order_date', 'product']
assert all(col in df.columns for col in required_cols)

# group by product and calculate total revenue
# then get top 10 products and sort for better display
top10_products = (
    df.groupby("product")["revenue"]
    .sum()
    .nlargest(10)
    .sort_values()   # sort ascending for horizontal bar chart
)

# normalize values to map them into color range
norm = plt.Normalize(top10_products.min(), top10_products.max())

# use viridis colormap to create gradient colors
colors = cm.viridis(norm(top10_products.values))

# create figure and axis
fig, ax = plt.subplots()

# plot horizontal bar chart
bars = ax.barh(
    y=top10_products.index,      # product names
    width=top10_products.values, # revenue values
    color=colors                # color gradient based on value
)

# add value labels at the end of each bar
for i, v in enumerate(top10_products.values):
    ax.text(v, i, f"{v:,.0f}", va="center")

# set labels and title
ax.set_xlabel("Revenue")
ax.set_ylabel("Product")
ax.set_title("Top 10 Products by Revenue")

# adjust layout to prevent overlap
plt.tight_layout()

# save chart as image file
plt.savefig("charts/top_products.png", dpi=150)

# show plot
plt.show()