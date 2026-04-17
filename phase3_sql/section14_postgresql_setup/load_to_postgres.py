import pandas as pd
import glob
import os
from sqlalchemy import create_engine

# CONFIG
INPUT_PATTERN = "phase3_sql/section14_postgresql_setup/data/*.csv"

# connect to database
engine = create_engine("postgresql://qdull:@localhost:5432/ecommerce_db")

# find all CSV files
files = glob.glob(INPUT_PATTERN)

# loop and loard 
for file in files:
    df = pd.read_csv(file)
    table_name = os.path.basename(file).replace(".csv","")
    df.to_sql(table_name, engine, if_exists="replace",index=False)
    print(f"Loaded: {table_name}")
