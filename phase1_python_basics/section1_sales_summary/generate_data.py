import pandas as pd 
import random
from datetime import datetime, timedelta


PRODUCTS = {
    "iPhone 15": 35000,
    "iPhone 14": 30000,
    "iPad Air": 22000,
    "iPad Pro": 35000,
    "MacBook Air": 40000,
    "MacBook Pro": 60000,
    "AirPods Pro": 8000,
    "AirPods 3": 6000,
    "Apple Watch Series 9": 15000,
    "Apple Watch Ultra": 30000,
    "Samsung Galaxy S24": 32000,
    "Samsung Galaxy Tab S9": 28000,
    "Dell XPS 13": 42000,
    "HP Spectre x360": 38000,
    "Logitech Mouse": 1500,
    "Mechanical Keyboard": 3000,
    "Gaming Monitor": 12000,
    "USB-C Hub": 1200,
    "External SSD 1TB": 3500,
    "Power Bank": 1000,
    "Wireless Charger": 900,
    "Bluetooth Speaker": 2500,
    "Smart TV 55 inch": 18000,
    "Tablet Stand": 500,
    "Webcam HD": 1200,
    "Noise Cancelling Headphones": 7000
}

rows = []
for i in range(50):
    product_name = random.choice(list(PRODUCTS.keys()))
    qty = random.randint(1,5)
    price = PRODUCTS[product_name]
    rows.append({
        "order_id": i + 1,
        "product": product_name,
        "qty": qty,
        "price": price,
        "order_date": datetime.now() - timedelta(days=random.randint(0, 30)),
        "revenue": qty * price
    })

df = pd.DataFrame(rows)
print(df)
df.to_csv("sales_summary/orders.csv", index=False)
