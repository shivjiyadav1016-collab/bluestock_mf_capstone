fund = pd.read_csv(
'data/raw/fund_master.csv'
)

print("\nUNIQUE FUND HOUSES:")
print(
fund['fund_house'].unique()
)

print("\nCATEGORIES:")
print(
fund['category'].unique()
)

print("\nSUB-CATEGORIES:")
print(
fund['sub_category'].unique()
)

print("\nRISK GRADES:")
print(
fund['risk_grade'].unique()
)