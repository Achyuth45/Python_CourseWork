class Parent:
    def show_parent(self):
        print("This is parent class")

class Child(Parent):
    def show_child(self):
        print("This is child class")

obj = Child()

obj.show_parent()
obj.show_child()

print("Single inheritance example")
print("Program finished")