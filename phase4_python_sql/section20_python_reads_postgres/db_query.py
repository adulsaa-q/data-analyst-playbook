from sqlalchemy import create_engine
import pandas as pd
from config import DB_URL

engine = create_engine(DB_URL)

# read query file 
with open("phase4_python_sql/section20_python_reads_postgres/top10_products.sql") as f:
    query = f.read()

# run query → DataFrame
df = pd.read_sql(query, engine)
print(df)