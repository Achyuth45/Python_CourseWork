file=open("example.txt","r+")

w=file.write("this is an empty text file")
r=file.read()
print(r)
file.close()