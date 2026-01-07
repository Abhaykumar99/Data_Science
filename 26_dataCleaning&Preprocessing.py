import pandas as pd
df=pd.read_csv("data_cleaning_sample.csv")
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.drop_duplicates())

print(df.dropna())
print(df.dropna(axis=1))

print(df.fillna(0))
print(df["Age"].fillna(df["Age"].mean()))
print(df.ffill())
print(df.bfill())