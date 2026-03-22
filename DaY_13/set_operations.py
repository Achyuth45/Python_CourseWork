set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1")
print(set1)

print("Set2")
print(set2)

set1.add(9)
set1.remove(1)
set1.discard(10)

print("After add remove discard")
print(set1)

print("Union")
print(set1.union(set2))

print("Intersection")
print(set1.intersection(set2))

print("Difference")
print(set1.difference(set2))

print("Symmetric Difference")
print(set1.symmetric_difference(set2))

set1.update(set2)

print("After update")
print(set1)

print("Length")
print(len(set1))