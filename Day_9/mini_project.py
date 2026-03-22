num_students=int(input("enter the number of students:"))
names=[]
cgpas=[]
for i in range(1,num_students+1):
    name=input("enter the name:")
    cgpa=float(input("enter the cgpa:"))
    names.append(name)
    cgpas.append(cgpa)

print("Names".ljust(10),"cgpa")
print("\n")
for i in range(len(names)): 
    print(names[i].ljust(10),cgpas[i])
max_cgpa=max(cgpas)
min_cgpa=min(cgpas)


print("")


        