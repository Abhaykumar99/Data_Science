import pandas as pd
s1=pd.Series([23,45,67,89,98])
print(s1)
s2=pd.Series([23,45,67,89,98],index=["Ayush","Prakash","MS","Abhay","Ashish"])
print(s2)
print(s2["Abhay"])

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
df.index=["A","B","C"]
print(df)
print(df.index)
print(df.columns)
print(df.dtypes)
print(type(df))