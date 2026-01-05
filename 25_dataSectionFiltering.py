import pandas as pd
df = pd.read_csv("student_dataset.csv")
print(df)
print(df["Name"] )       # Single column (as Series)
print(df[["Name", "Course"]] )    # Multiple columns (as DataFrame)

print(df.loc[0])                # First row (by label)
print(df.iloc[0])               # First row (by position)

print(df.loc[4,'Course'])
print(df.iloc[4,4])

print(df.loc[0:2,["Name","Course","Final_Result"]])
print(df.iloc[0:2,0:3])

print(df.at[1,"Name"])
print(df.iat[1,1])