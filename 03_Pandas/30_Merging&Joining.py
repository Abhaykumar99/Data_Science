import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})

print(pd.merge(employees,departments,on="DeptID"))

print(pd.merge(employees,departments,on="DeptID",how="left"))  #left join
print(pd.merge(employees,departments,on="DeptID",how="right"))  #right join
print(pd.merge(employees,departments,on="DeptID",how="outer"))  #outer join

df1 = pd.DataFrame({"Name": ["Alice", "Bob"],"Score":[232,343]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"],"Age":[18,20]})

print(pd.concat([df1, df2]))
print(pd.concat([df1, df2],axis=1))
