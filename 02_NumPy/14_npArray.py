import numpy as np
arr=np.array([[1,2,4],[3,4,5]])
print(arr)
print(type(arr))
print(arr.shape)

import sys

list_data = list(range(1000))
numpy_data = np.array(list_data)

print("Python list size:", sys.getsizeof(list_data) * len(list_data), "bytes")
print("NumPy array size:", numpy_data.nbytes, "bytes")