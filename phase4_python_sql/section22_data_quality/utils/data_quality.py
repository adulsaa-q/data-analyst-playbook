import pandas as pd

# load raw datasets
order_items = pd.read_csv("phase3_sql/data/shopee_order_items_thailand.csv", encoding="utf-8-sig")
orders = pd.read_csv("phase3_sql/data/shopee_orders_thailand.csv", encoding="utf-8-sig")

# enrich order_items with order_date
df = pd.merge(order_items, orders[["order_id", "order_date"]], on="order_id")

def check_quality(df):
    results = {}
    
    # count exact duplicate rows
    results["duplicate_rows"] = df.duplicated().sum()
    
    # percentage of missing values per column
    results["null_pct"] = df.isnull().mean() * 100

    # flag negative values in price or quantity (invalid business logic)
    condition1 = df["unit_price"] < 0
    condition2 = df["quantity"] < 0
    results["negative_values"] = (condition1 | condition2).sum()

    # check data coverage (date range)
    results["date_range"] = {
        "min_date": df["order_date"].min(),
        "max_date": df["order_date"].max()
    }

    # detect outliers using IQR method
    Q1 = df["line_total"].quantile(0.25)
    Q3 = df["line_total"].quantile(0.75)
    IQR = Q3 - Q1 
    
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR

    condition = (df["line_total"] < lower_fence) | (df["line_total"] > upper_fence)
    results["outliers"] = condition.sum()

    return results

result = check_quality(df)

print("=== Data Quality Report ===")
print(f"Duplicate rows : {result['duplicate_rows']}")
print(f"Negative values: {result['negative_values']}")
print(f"Outliers       : {result['outliers']}")
print(f"Date range     : {result['date_range']['min_date']} → {result['date_range']['max_date']}")

# highlight columns with high missing values
print("\n⚠️  Columns with null > 5%:")

high_null = {col: pct for col, pct in result["null_pct"].items() if pct > 5}

if high_null:
    for col, pct in sorted(high_null.items(), key=lambda x: x[1], reverse=True):
        print(f"{col}: {pct:.2f}%")
else:
    print("None")