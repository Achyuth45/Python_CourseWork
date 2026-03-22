
a = 10              
b = 3.14            
c = 2 + 5j           

print("Integer:", a, type(a))
print("Float:", b, type(b))
print("Complex:", c, type(c))


is_python_easy = True
print("\nBoolean:", is_python_easy, type(is_python_easy))



name = "Achyuth"
print("\nString:", name, type(name))


numbers = [1, 2, 3, 4, 5]
print("\nList:", numbers, type(numbers))



coordinates = (10, 20)
print("\nTuple:", coordinates, type(coordinates))



unique_values = {1, 2, 3, 3, 4}
print("\nSet:", unique_values, type(unique_values))



student = {
    "name": "Achyuth",
    "branch": "CSE",
    "year": 4
}
print("\nDictionary:", student, type(student))



result = None
print("\nNoneType:", result, type(result))



data = b"Python"
print("\nBytes:", data, type(data))



mutable_data = bytearray([65, 66, 67])
print("\nBytearray:", mutable_data, type(mutable_data))



r = range(1, 6)
print("\nRange:", list(r), type(r))



fs = frozenset([1, 2, 3, 4])
print("\nFrozenset:", fs, type(fs))
