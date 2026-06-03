import pandas as pd
import os

path='data/raw'

files=os.listdir(path)

for file in files:

    if file.endswith('.csv'):

        df=pd.read_csv(f'{path}/{file}')

        print("\nFILE:",file)
        print(df.shape)
        print(df.dtypes)
        print(df.head())
fund_master = pd.read_csv(
'data/Raw/01_fund_master.csv'
)

nav = pd.read_csv(
'data/Raw/02_nav_history.csv'
)

missing_codes = set(
fund_master['amfi_code']
) - set(
nav['amfi_code']
)

print("\nMISSING AMFI CODES:")
print(missing_codes)