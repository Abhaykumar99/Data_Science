name="Abhay"
age=20
print("My name is {} and I am {} years old.".format(name,age))
print(f"My name is {name} and I am {age} years old.")  #using f-strings
print(f"My age is {age:.2f} years.")  #formatted to 2 decimal places
print(f"{name:<10} is left aligned.")  #left aligned within 10 spaces
print(f"{name:>10} is right aligned.")  #right aligned within 10 spaces
print(f"{name:^10} is center aligned.")  #center aligned within 10 spaces
