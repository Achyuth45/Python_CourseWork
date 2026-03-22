class Father:
    def father_method(self):
        print("Father class method")

class Mother:
    def mother_method(self):
        print("Mother class method")

class Child(Father, Mother):
    def child_method(self):
        print("Child class method")

obj = Child()

obj.father_method()
obj.mother_method()
obj.child_method()
print("Multiple inheritance example")