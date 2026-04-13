import pandas as pd 

df = pd.read_csv("data/orders_clean.csv")
stats = df[["price", "revenue"]].describe()

Q1 = df["revenue"].quantile(0.25)
Q3 = df["revenue"].quantile(0.75)
IQR = Q3 - Q1

lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

outliers = df[(df["revenue"] < lower_fence) | (df["revenue"] > upper_fence)]

print(f"outliers: {len(outliers)} orders (IDs: {outliers['order_id'].tolist()})")
print(f"Total orders: {len(df)}")
print(f"Outlier %: {len(outliers)/len(df)*100:.1f}%")

print("\nRevenue Stats:")
print(f"mean:   {df['revenue'].mean():,.0f}")
print(f"median: {df['revenue'].median():,.0f}")
print(f"std:    {df['revenue'].std():,.0f}")