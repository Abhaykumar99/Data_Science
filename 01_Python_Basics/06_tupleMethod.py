t=(1,2,3,'Abhay','Kumar')
print(t)
print(type(t))
t1=()
l=[]
print(type(t1))
print(type(l))
print(t[1:3])
data=('Abhay',20,'Mirzapur')
name,Age,Village=data
print(name)
print(Age)
person1 = (
    ("Alice", 25, "Engineer"),
    ("Abhay", 25, "Engineer"),
    ("Ayush", 25, "Engineer")
)
for name, _, _ in person1:
    print(name)
for name, Age, Village in person1:
    print(name,Age,Village)


