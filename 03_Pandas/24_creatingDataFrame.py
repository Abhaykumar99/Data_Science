import pandas as pd
import numpy as np

data=[["Abhay",95],["MS",96],["Prakash",97],["Ashish",99]]
print(data)
d=pd.DataFrame(data, columns=["Name","Marks"])
print(d)
data1={"A":[1,2,3,4],"B":[6,7,8,9]}
print(data1)
df=pd.DataFrame(data1)
print(df)
data2=np.array([[1,2],[2,3],[3,4],[4,5]])
print(data2)
df=pd.DataFrame(data2,columns=["A","B"])
print(df)
d1=pd.read_excel("../Resources/sample_dataset.xlsx")
print(d1)
d2=pd.read_csv("../Resources/sample_dataset.csv")
print(d2)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)