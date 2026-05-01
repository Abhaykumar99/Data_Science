l=[1,2,3,5,6,7]
l[3]=4
print(l)
l.insert(4,5)
print(l)
l.pop(4)
print(l)
l.remove(3)
print(l)
l.append(2)
print(l)
l.extend(["Abhay","Prakash",1,2,3])
print(l)
print(l.count(2))
l.reverse()
print(l)
print(list(reversed(l)))
l2=["Abhay","Kumar"]
print(l+l2)
if 'Abhay' in l2:
    print("Yes")
print(l.clear())
print('Abhay' in l2)
s="Abhay-Ayush-Prakash-MS-Ashish"
print(s.split("-"))

'''
Method	Description	Example
append(x)	        Adds an element x to the end of the list.                       	my_list.append(10)
extend(iterable)	Extends the list by appending all elements from an iterable.	    my_list.extend([6, 7, 8])
insert(index, x)	Inserts x at the specified index.                                  	my_list.insert(2, "Python")
remove(x)	        Removes the first occurrence of x in the list.	                    my_list.remove(3)
pop([index])	    Removes and returns the element at index (last element if index is not provided).	my_list.pop(2)
index(x)	        Returns the index of the first occurrence of x.                 	my_list.index(4)
count(x)	        Returns the number of times x appears in the list.              	my_list.count(2)
sort()          	Sorts the list in ascending order.	                                my_list.sort()
reverse()	        Reverses the order of the list.                                 	my_list.reverse()
copy()	            Returns a shallow copy of the list.	                                new_list = my_list.copy()
clear()         	Removes all elements from the list.                                	my_list.clear()

'''