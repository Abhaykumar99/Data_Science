class Employee:
    company="HP"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdetails(self):
        print(f"The {self.name} company is {self.company}. The Age of {self.name} is {self.age}")
    @staticmethod
    def printtime():
        print(f"The time is now")
    
    @classmethod
    def printclassmethod(cls):
        print(f"The company is {cls.company}")

a=Employee("Abhay",24)
a.printdetails()
a.printtime()
a.printclassmethod()