numbers = [3, 7, 10, 15, 20, 25, 30]
count = 0
print("Processing numbers")

for n in numbers:
    if n == 10:
        print("Skip 10")
        continue
    if n == 25:
        print("Stop at 25")
        break
    if n == 15:
        pass
    print("Number:", n)
    count = count + 1

print("Processed count")
print(count)
print("Program finished")