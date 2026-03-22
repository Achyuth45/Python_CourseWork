class Parent:
    def parent_method(self):
        print("Parent class method")

class Child1(Parent):
    def child1_method(self):
        print("Child1 class method")

class Child2(Parent):
    def child2_method(self):
        print("Child2 class method")

obj1 = Child1()
obj2 = Child2()

obj1.parent_method()
obj1.child1_method()

obj2.parent_method()
obj2.child2_method()
print("Hierarchical inheritance example")