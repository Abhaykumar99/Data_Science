import numpy as np
import time

list1=range(1000)
arr1 =np.array(range(1000))

# Python list (loop-based)
start=time.time()
list_squares = [x ** 2 for x in list1]
end=time.time()
print(end-start)
print(list_squares)

# NumPy (vectorized)
start1=time.time()
arr=numpy_squares = arr1 ** 2
end1=time.time()
print(end1-start1)
print(arr)