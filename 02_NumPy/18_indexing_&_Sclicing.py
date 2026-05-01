import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr)
flat=arr.flatten()
print(flat)
print(flat[:len(flat)])
print(flat[3])
print(flat[2:])
print(flat[3:6])
print(flat[0:3])

b=flat[1:5]
print(b)
b[1]=9
print(b)
print(flat)

c=flat[4:9].copy()
print(c)
c[0]=123
print(c)
print(flat)

arr=np.array([1,12,13,123,43,53])
ind=[1,3,5]
print(arr[ind])
print(arr[[0, 2, 3]])

print(arr[arr>10])