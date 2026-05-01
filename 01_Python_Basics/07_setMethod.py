s={} # This creates an empty dictionary
print(type(s))
s1=set() # This creates an empty set
print(type(s1))
s2={1,2,3,41,2,3}
print(s2)
s2.update([23,43,45,2])
print(s2)
s2.add(67)
print(s2)
s2.remove(2)
print(s2)
s2.discard(34)
print(s2)
print(s2.pop())
s3=s2.copy()
print(s3)
s2.clear()
print(s2)
a1={1,2,3,4}
a2={3,4,5,6}

print(a1.union(a2))
print(a1.intersection(a2))
sub={1,2}
print(sub.issubset(a1))
print(a1.issuperset(sub))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union – combines all unique elements
print(set1 | set2)            # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))       # same result

# Intersection – common elements
print(set1 & set2)            # {3, 4}
print(set1.intersection(set2))# same result

# Difference – in set1 but not in set2
print(set1 - set2)            # {1, 2}
print(set1.difference(set2))  # same result

# Symmetric Difference – in either set, but not both
print(set1 ^ set2)                     # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))# same result