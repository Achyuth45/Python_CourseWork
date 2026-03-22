pwd = input("enter a strong password:")
if len(pwd) >= 8:
    s = set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digits")   
        else:
            s.add("special_char")
    if len(s)==4:
        print(f"Your password {pwd}  is validated and its a strong password>>>>")
    else:
        print("your Password is too weak")
else:
    print("...password should contain atleast 8 charecters...")


        
