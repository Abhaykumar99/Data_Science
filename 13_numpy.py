# pyhon Zip Explained
l1 = [1, 2, 3, 4, 5]
l2 = [5, 3, 2, 1]
print(list(zip(l1, l2)))

#using python list
import time
size=1_000_000_0

l1=list(range(size))
l2=list(range(size))
start=time.time()
add=[x+y for x,y in zip(l1,l2)]
end=time.time()
print(end-start)
print(add[0:11])

#using the numpy
import numpy as np
l1=np.array(list(range(size)))
l2=np.array(list(range(size)))
start1=time.time()
add1=l1+l2
end1=time.time()
print(end1-start1)
print(add[0:11])


#np.array
arr=np.array([1,2,3,4,"Abhay"])
print(type(arr))