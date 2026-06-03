import pandas as pd
import os

# Load all CSV files
path = 'data/Raw'

files = os.listdir(path)

for file in files:

    if file.endswith('.csv'):

        df = pd.read_csv(f'{path}/{file}')

        print("\nFILE:", file)
        print(df.shape)
        print(df.dtypes)
        print(df.head())


# Load main datasets
fund_master = pd.read_csv('data/Raw/01_fund_master.csv')
nav = pd.read_csv('data/Raw/02_nav_history.csv')

# Explore fund master
print("\nUNIQUE FUND HOUSES:")
print(fund_master['fund_house'].unique())

print("\nUNIQUE CATEGORIES:")
print(fund_master['category'].unique())

print("\nUNIQUE SUB-CATEGORIES:")
print(fund_master['sub_category'].unique())

# Show all columns
print("\nALL COLUMNS:")
print(fund_master.columns)

# AMFI Validation
missing_codes = set(fund_master['amfi_code']) - set(nav['amfi_code'])

print("\nMISSING AMFI CODES:")
print(missing_codes)