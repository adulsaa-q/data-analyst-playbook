import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# Product catalog: name -> (min_price, max_price)
products = {
    "MacBook Pro":         (45000, 89000),
    "iPhone 15":           (32000, 45000),
    "iPad Air":            (18000, 28000),
    "AirPods Pro":         (7500,  9500),
    "Apple Watch":         (12000, 19000),
    "Samsung TV 55":       (18000, 35000),
    "Sony Headphones":     (4500,  8500),
    "Logitech Mouse":      (1200,  2500),
    "Mechanical Keyboard": (2500,  5500),
    "USB-C Hub":           (800,   1800),
}

start_date = datetime(2024, 1, 1)
end_date   = datetime(2024, 12, 31)

rows = []
order_id = 1000

for _ in range(500):
    day_offset = np.random.randint(0, (end_date - start_date).days + 1)
    order_date = start_date + timedelta(days=int(day_offset))

    # Q4 (Nov-Dec) gets more orders to simulate holiday season
    num_orders = random.randint(2, 4) if order_date.month in [11, 12] else 1

    for _ in range(num_orders):
        product = random.choice(list(products.keys()))
        price = round(random.uniform(*products[product]), -2)
        qty = random.choices([1, 2, 3], weights=[0.7, 0.2, 0.1])[0]

        rows.append({
            "order_id":   order_id,
            "customer_id": f"C{random.randint(100, 300):03d}",
            "product":    product,
            "qty":        qty,
            "price":      price,
            "revenue":    price * qty,
            "order_date": order_date.strftime("%Y-%m-%d"),
        })
        order_id += 1

df = pd.DataFrame(rows)
df = df.sort_values("order_date").reset_index(drop=True)
df.to_csv("data/orders_clean_p2.csv", index=False)

print(f"Generated {len(df)} rows across 12 months")
print(df.groupby(df["order_date"].str[:7])["revenue"].sum())