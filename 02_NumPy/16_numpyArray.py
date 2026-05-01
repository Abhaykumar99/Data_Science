import numpy as np
arr=np.zeros((3,4))
print(arr)
arr=np.ones((4,5))
print(arr)
arr=np.full((5,6),2)
print(arr)
arr=np.eye(4)
print(arr)
arr=np.arange(0,101,2)
print(f"All Even Number between 0 to 100 : {arr}")

arr=np.linspace(1,100,10)
print(arr)

arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Shape:", arr.shape)   # (2, 3) → 2 rows, 3 columns
print("Size:", arr.size)     # 6 → total elements
print("Dimensions:", arr.ndim) # 2 → 2D array
print("Data type:", arr.dtype) # int64 (or int32 on Windows)


arr = np.array([1, 2, 3], dtype=np.float32)  # Explicit type
print(arr.dtype)  # float32
arr = np.array([1, 2, 3], dtype=np.float64)  # Explicit type
print(arr.dtype)  # float64
print(arr)

arr_int = arr.astype(np.int32)  # Convert float to int
print(arr_int)  # [1 2 3]
print(arr_int.dtype)