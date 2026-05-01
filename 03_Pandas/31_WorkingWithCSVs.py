import pandas as pd
df=pd.read_csv("../Resources/sample_dataset.csv")
print(df)
print(df.dtypes)
print(list(df.columns))
print(df["Marks"].max())

df=df[df["Marks"]>80]
print(df)
df.to_csv("../Resources/updated.csv",index=False)

df1=pd.read_json("../Resources/data.json")
print(df1)
df1=pd.json_normalize(df1)
print(df1)