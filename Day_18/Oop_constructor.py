class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)

s1 = Student("Rahul", 21, "Python")
s2 = Student("Anita", 20, "Data Science")

print("Student 1 Details")
s1.display()

print("Student 2 Details")
s2.display()