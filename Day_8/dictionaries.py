student = {"name": "Ravi", "age": 21, "course": "Python"}

print("Dictionary")
print(student)

print("Keys")
print(student.keys())

print("Values")
print(student.values())

print("Items")
print(student.items())

student.update({"age": 22})
student["city"] = "Hyderabad"

print("Updated Dictionary")
print(student)

student.pop("course")
print("Final Dictionary")
print(student)