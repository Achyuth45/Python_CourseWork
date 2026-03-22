# Integer conversions
a = 10
print("int to float:", float(a))
print("int to string:", str(a))
print("int to complex:", complex(a))

#  Float conversions
b = 12.5
print("\nfloat to int:", int(b))
print("float to string:", str(b))
print("float to complex:", complex(b))

#  String conversions
c = "20"
print("\nstring to int:", int(c))
print("string to float:", float(c))
print("string to complex:", complex(c))

# Boolean conversions
d = True
print("\nboolean to int:", int(d))
print("boolean to float:", float(d))
print("boolean to string:", str(d))

# List conversions
lst = [1, 2, 3]
print("\nlist to tuple:", tuple(lst))
print("list to set:", set(lst))
print("list to string:", str(lst))

# Tuple conversions
tup = (4, 5, 6)
print("\ntuple to list:", list(tup))
print("tuple to set:", set(tup))
print("tuple to string:", str(tup))

# Set conversions
st = {7, 8, 9}
print("\nset to list:", list(st))
print("set to tuple:", tuple(st))
print("set to string:", str(st))

# Dictionary conversions
dic = {1: "A", 2: "B"}
print("\ndictionary to list:", list(dic))
print("dictionary to tuple:", tuple(dic))
print("dictionary to set:", set(dic))
print("dictionary to string:", str(dic))

# Complex number conversions
e = 3 + 4j
print("\ncomplex to string:", str(e))

# Input type conversion
num = "50"
num = int(num)
print("\nstring input converted to int:", num)
