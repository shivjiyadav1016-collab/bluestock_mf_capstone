import sqlite3
import pandas as pd

# connect database
conn = sqlite3.connect('data/bluestock_mf.db')

# read table
df = pd.read_sql_query("SELECT * FROM fact_nav LIMIT 10", conn)

print(df)

conn.close()