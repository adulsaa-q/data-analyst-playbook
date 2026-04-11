import pandas as pd 

date_based = pd.read_csv("data/orders_clean.csv")

# convert order_date to datetime
date_based["order_date"] = pd.to_datetime(date_based["order_date"])

# extract month and week number from order_date
date_based["month"] = date_based["order_date"].dt.month
date_based["week_number"] = date_based["order_date"].dt.isocalendar().week

# group by month and sum revenue
monthly_revenue = (
    date_based.groupby("month")
    .agg(total_revenue=("revenue", "sum"))
)

# find best and worst month
best_month = monthly_revenue["total_revenue"].idxmax()
worst_month = monthly_revenue["total_revenue"].idxmin()

best_revenue = monthly_revenue["total_revenue"].max()
worst_revenue = monthly_revenue["total_revenue"].min()

# count orders per week
weekly_orders = date_based.groupby("week_number")["order_id"].count()

# print results
print(f"Best month:  Month {best_month} — {best_revenue:,.0f} THB")
print(f"Worst month: Month {worst_month} — {worst_revenue:,.0f} THB")
print(f"\nOrders per week:")
print(weekly_orders)