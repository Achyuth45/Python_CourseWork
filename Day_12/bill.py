data={
    1:{"product":"Rice","price":60},
    2:{"product":"Tea_powder","price":80},
    3:{"product":"Sugar","price":40},
    4:{"product":"Milk","price":90},
    5:{"product":"Bread","price":40},
    6:{"product":"Cooking_oil","price":120},
    7:{"product":"fruits","price":150},
    8:{"product":"salt","price":25},
    9:{"product":"Wheat","price":70},
    10:{"product":"soap","price":20}
}

print("Index".ljust(15," "),"product".ljust(20," "),"price".ljust(50," "))
for i in data:
    print(str(i).ljust(15," "),data[i]["product"].ljust(20," "),data[i]["price"])

items = list(map(int,input("enter the items numbers:").split()))



print("bill".center(30,'_'))

print("product".ljust(20," "),"quantity".ljust(30," "),"price")
new_items=list(set(items))
total_bill=0
for i in new_items:
    quantity=items.count(i)

    print(f"{data[i]["product"].ljust(20)} {str(quantity).ljust(30," ")} ${data[i]["price"]*quantity}")
    total_bill+=data[i]["price"]*quantity
print(f"Here is your total bill  {total_bill}\nThank You have a nice day......")