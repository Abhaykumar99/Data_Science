import numpy as np

arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

print(arr)
print(arr[0])
print(arr[1])
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print(arr[1,2])
print(arr[0:1,1:3])
print(arr[0:,0:])
print(arr[0][1])

arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

# Output of arr3D.shape is → (depth, rows, columns)
print(arr3D.shape)  # Output: (2, 2, 3) 
print(arr3D[0,1,2])
print(arr3D[1,0,1])
print(arr3D[:,1,:])
arr3D[:,0,:]=0
print(arr3D)