#Reshape a 1D array of size 9 into a 3×3 matrix.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr)
arr=arr.reshape(3,3)
print(arr)