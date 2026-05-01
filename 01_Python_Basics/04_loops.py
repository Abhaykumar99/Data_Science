num=[2,4,6,8,12,13,14,16]
for i in num:
    print(i)
print("\n")

for i in range(10):
    print(i)
print("\n")
for i in range(1,11):
    print(i)
print("\n")

i=0
while(i<4):
    print(i)
    i=i+1

print("\n")
print("Using pass statement")
for i in range(10):
    pass # do not anything or ingnore this
print("\n")
print("Using break statement for 5")
for i in range(10):
    if(i==5):
        break # Stop this loop right here
    print(i)
print("\n")
print("Using continue statement for 4")
for i in range(10):
    if(i==4):
        continue  # skip this iteration and continue with next 
    print(i)
