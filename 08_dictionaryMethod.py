d={}
print(type(d))

# Dictionary with key-value pairs
student = {
    "name": "Abhay",
    "age": 20,
    "grade": "A"
}
print(student)
print(student['age'])
print(student.items())
print(student.keys())
print(student.values())
student.update({"name":"Ayush","village":"Mirzapur"})
print(student)
print(student.get("name1"))
print(student.get("name"))
student.setdefault("priority","High")
print(student)