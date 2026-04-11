import pandas as pd

df = pd.read_csv("data/orders_clean.csv")

# aggregate total revenue by product (desc)
product_revenue = (
    df.groupby("product")
    .agg(total_revenue=("revenue", "sum"))
    .sort_values(by="total_revenue", ascending=False)
)

# total revenue overall
total_revenue = product_revenue["total_revenue"].sum()

# add contribution metrics
product_revenue["revenue_pct"] = (
    product_revenue["total_revenue"] / total_revenue * 100
)

product_revenue["cumulative_pct"] = (
    product_revenue["revenue_pct"].cumsum()
)

# top 5 products
top5 = product_revenue.nlargest(5, "total_revenue")

print(product_revenue)
print(f"\nTotal revenue: {total_revenue:,.0f} THB")

print("\nTop 5 Products:")
print(top5.to_string(float_format="{:,.1f}".format))