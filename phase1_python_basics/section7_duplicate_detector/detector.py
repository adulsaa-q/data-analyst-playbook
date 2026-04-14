import pandas as pd


df = pd.read_csv("data/orders_with_dupes.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

# sort before diff
df = df.sort_values(["customer_id", "product", "order_date"])

# use order_date for diff
df["date_diff"] = df.groupby(["customer_id", "product"])["order_date"].diff()

dupl_rows = df[df.duplicated()].copy()
soft_dupes = df[
    (df["date_diff"].notna()) &
    (df["date_diff"] <= pd.Timedelta(days=1))
].copy()

# remove exact duplicates
df = df.drop_duplicates()

# --- add type ---
dupl_rows["dupe_type"] = "exact"
soft_dupes["dupe_type"] = "soft"

# --- combine and export ---
all_dupes = pd.concat([dupl_rows, soft_dupes], ignore_index=True)
all_dupes.to_csv("data/duplicate_flags.csv", encoding='utf-8', index=False)

# save cleaned data
df.to_csv("data/orders_with_dupes.csv", encoding='utf-8', index=False)

print(f"duplicates: {len(all_dupes)} | clean rows: {len(df)}")