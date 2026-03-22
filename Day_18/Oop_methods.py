class Student:

    school = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def show_school(cls):
        print("School:", cls.school)

    @staticmethod
    def message():
        print("This is a static method example")

s1 = Student("Rahul", 85)

print("Instance Method")
s1.show()

print("Class Method")
Student.show_school()

print("Static Method")
Student.message()