marks=int(input("Enter the English marks: "))
match marks:
    case marks if 60 <= marks <= 100:
        print("You have passed with First Division")
    case marks if 50 <= marks < 60:            
        print("You have passed with Second Division")
    case marks if 33 <= marks < 50:
        print("You have passed with Third Division")
    case marks if 0 <= marks < 33: 
        print("You have Failed")
    case _:
        print("Invalid Marks Entered")
