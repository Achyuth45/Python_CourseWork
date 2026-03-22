import csv
with open("data.csv","r") as file:
    content=csv.reader(file)
    for i in content:
        print(i)
