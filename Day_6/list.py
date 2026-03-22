numbers = [10, 20, 30, 40, 50]

print("Original List")
print(numbers)

numbers.append(60)
numbers.insert(2, 25)
numbers.remove(40)

print("Updated List")
print(numbers)

print("Length")
print(len(numbers))

print("Index of 30")
print(numbers.index(30))

numbers.sort()
print("Sorted List")
print(numbers)