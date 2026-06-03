import pandas as pd
from sqlalchemy import create_engine

# Create SQLite DB
engine = create_engine(
    'sqlite:///data/bluestock_mf.db'
)

# Load cleaned file
nav = pd.read_csv(
    'data/processed/nav_history_cleaned.csv'
)

# Save into database
nav.to_sql(
    'fact_nav',
    engine,
    if_exists='replace',
    index=False
)

print("SQLite DB Created Successfully!")