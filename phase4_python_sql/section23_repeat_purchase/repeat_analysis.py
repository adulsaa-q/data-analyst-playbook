import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://qdull:@localhost:5432/ecommerce_db"
engine = create_engine(DB_URL)

with open("phase4_python_sql/section23_repeat_purchase/repeat_customers.sql") as f:
    query = f.read()

df = pd.read_sql(query,engine)

def calculate_repeat_rate(df):
    # count order by customer > 1 
    order_counts = df.groupby("customer_id").size()
    # filter buy > 1 
    repeat_customers = order_counts[order_counts > 1]

    repeat_rate = len(repeat_customers) / len(order_counts)

    return repeat_rate

print(calculate_repeat_rate(df))