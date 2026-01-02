f=open("text.txt","r")

print(f.read())
f.close()
s="My name is Abhay Kuamr"
f=open("text.txt","w")
f.write(s)
f.close()
with open("text.txt","r") as file: # automatically closes the file after the block
    content=file.read() # reads the entire file
    print(content) # prints the content of the file
with open("text.txt","a") as file: # append mode
    file.write("\nI am learning Python file handling.")
with open("text.txt","r") as file:
    content=file.read()
    print(content)