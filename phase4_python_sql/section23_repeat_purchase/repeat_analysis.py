import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://qdull:@localhost:5432/ecommerce_db"
engine = create_engine(DB_URL)

with open("phase4_python_sql/section23_repeat_purchase/repeat_customers.sql") as f:
    query = f.read()

df = pd.read_sql(query, engine)

def calculate_repeat_rate(df):
    total_customers = len(df)
    repeat_customers = len(df[df["total_order"] > 1])
    repeat_rate = repeat_customers / total_customers * 100
    return round(repeat_rate, 2)

def compare_revenue(df):
    one_time = df[df["total_order"] == 1]["total_amount"].mean()
    repeat = df[df["total_order"] > 1]["total_amount"].mean()
    return round(one_time, 2), round(repeat, 2)

if __name__ == "__main__":
    print(f"Repeat Rate: {calculate_repeat_rate(df)}%")
    one_time, repeat = compare_revenue(df)
    print(f"Avg Revenue - One-time: {one_time:,.2f} | Repeat: {repeat:,.2f}")