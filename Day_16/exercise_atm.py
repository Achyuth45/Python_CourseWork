def Value_error_case():
    balance=19999
    try:
        amt=int(input("enter the amout to withdraw:"))
        tr=balance-amt

    except ValueError:
        print("cant withdraw str amount please enter greater than zero...")

def Zero_Division_error():
    try:
        transactions=[]
        avg_transactions=sum(transactions)/len(transactions)
    except ZeroDivisionError:
        print("transactions are empty so make a transaction..")

def Type_error_case():
    balance=10000
    try:
        amt=input("enter a amount:")
        balance-=amt
    except TypeError:
        print("cant add string amount to balance...")

data={234:56,67:78}

def Key_error_case(details):
    try:
        acc=int(input("enter account num:"))
        print(details[acc])
    except KeyError:
        print("invalid details acc not exist...")
def File_Not_Found_error_case():
    try:
        file = open("yuyi.txt""r")
        file.read
    except FileNotFoundError():
        print("the transactions  file doesnt exist  ")

def index_error_case():
    try:
        transactions=["500 deposited"]
        print(transactions[6])
    except IndexError:
        print("transactions not noted or transaction is not happen")


data={1234:565,4556:567}

print("------ATM Simulation Menu------")
print("1. Check Average Transaction (ZeroDisionError)")
print("2. Withdraw With Invalid Input (ValueError)")
print("3. Deposit With Invalid Data Type (TypeError)")
print("4. Access Invalid Transaction History (IndexError)")
print("5. Access Non_Existent Account (KeyError)")
print("6. Read Missing Transaction Log File (FileNotFoundError)")
print("7. Exit")




while True:
    select_option=input("Enter the any number B/W (1-7):")
    if select_option=="1":
        Zero_Division_error()
    elif select_option == "2":
        Value_error_case()
    elif select_option == "3":
        Type_error_case()
    elif select_option == "4":
        index_error_case()
    elif select_option == "5":
        Key_error_case(data)
    elif select_option == "6":
        File_Not_Found_error_case()
    else:
        print("Thank you have a nice day.....")
        break





