import pandas as pd

nav = pd.read_csv('data/Raw/02_nav_history.csv')

print("Original Shape:")
print(nav.shape)

nav['date'] = pd.to_datetime(
    nav['date'],
    errors='coerce'
)

nav = nav.sort_values(
    by=['amfi_code', 'date']
)

nav = nav.drop_duplicates()

nav = nav[nav['nav'] > 0]

print("\nCleaned Shape:")
print(nav.shape)

nav.to_csv(
    'data/processed/nav_history_cleaned.csv',
    index=False
)

print("\nNAV cleaning completed!")