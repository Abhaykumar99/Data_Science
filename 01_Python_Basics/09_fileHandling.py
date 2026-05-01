f=open("../Resources/text.txt","r")

print(f.read())
f.close()
s="My name is Abhay Kuamr"
f=open("../Resources/text.txt","w")
f.write(s)
f.close()
with open("../Resources/text.txt","r") as file: # automatically closes the file after the block
    content=file.read() # reads the entire file
    print(content) # prints the content of the file
with open("../Resources/text.txt","a") as file: # append mode
    file.write("\nI am learning Python file handling.")
with open("../Resources/text.txt","r") as file:
    content=file.read()
    print(content)