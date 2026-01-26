import pandas as pd
df=pd.read_csv("sample_dataset.csv")
print(df)
df=df.sort_values("Marks")
print(df)
df=df.sort_values("Marks",ascending=False)
print(df)
df=df.sort_values(["Marks","Name"])
print(df)
