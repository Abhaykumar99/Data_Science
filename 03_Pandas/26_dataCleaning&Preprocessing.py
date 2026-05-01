import pandas as pd
df=pd.read_csv("../Resources/data_cleaning_sample.csv")
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

print(df.duplicated())

print(df["Name"].str.lower())

print(df["City"].str.contains('delhi',case=False))

df2=df.dropna().copy()
df2["Age"]=df2["Age"].astype(int)
print(df2.info())
df2["Join Date"] = pd.to_datetime(df2["Join Date"], errors="coerce")
print(df2)

def isMinor(x):
    return "Adult" if x>=25 else "Minor"
print(df2["Age"].apply(isMinor))

gender_map = {"M": "Male","F":"Female","O":"Other"}
print(df2["Gender"].map(gender_map))

df2["City"]=df2["City"].replace({"Delhi":"New Delhi","Mumbai":"New Mumbai"})
print(df2)