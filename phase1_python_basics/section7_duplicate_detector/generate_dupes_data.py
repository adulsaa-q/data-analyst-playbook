import pandas as pd 
import random 
from datetime import datetime, timedelta
import uuid


products = {
    "Laptop": 35000,
    "Monitor": 7000,
    "Office Chair": 4500,
    "Desk": 6000,
    "USB Flash Drive": 350,
    "External Hard Drive": 2500,
    "Notebook": 120,
    "Backpack": 900,
    "Printer": 3200,
    "Router": 1800
}

start_date = datetime(2024, 1, 1)
customer_ids = [2601, 2602, 2603, 2604, 2605]

data = []

# build rows
for i in range(1, 50):
    order_id = uuid.uuid4().hex[:8]
    selected_customer_id = random.choice(customer_ids)

    product = random.choice(list(products.keys()))
    price = products[product]

    qty = random.randint(1, 5)
    revenue = qty * price

    # random date within 30 days
    order_date = (start_date + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

    data.append({
        'order_id': order_id,
        'customer_id': selected_customer_id,
        'product': product,
        'qty': qty,
        'price': price,
        'revenue': revenue,
        'order_date': order_date
    })

df = pd.DataFrame(data)

# --- exact duplicates (same rows) ---
exact_dupes = df.sample(10).copy()


# --- soft duplicates (like repeat orders) ---
soft_dupes = df.sample(10).copy()

# new order id
soft_dupes['order_id'] = [uuid.uuid4().hex[:8] for _ in range(len(soft_dupes))]

# shift date +1 day
soft_dupes['order_date'] = pd.to_datetime(soft_dupes['order_date']) + pd.Timedelta(days=1)
soft_dupes['order_date'] = soft_dupes['order_date'].dt.strftime("%Y-%m-%d")


# combine all
df = pd.concat([df, exact_dupes, soft_dupes], ignore_index=True)
df.to_csv("data/orders_with_dupes.csv", index=False)
print(f"file created: {len(df)} rows")