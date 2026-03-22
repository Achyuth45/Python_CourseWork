data={
    "achyuth@gmail.com":"ghhgh45",
    "karthikeya@gmail.com":"tuuey89",
    "sandeep@gmail.com":"tuuyty79",
    "sai@gmail.com":"tuuey89",
    "arun@gmai.com":"567ey89"
    
}
print("---------------LOGIN----------------")
print("\n")
print("---------------SIGNUP----------------")
action=input("enter your action: ")
if action.lower() == "signup":
    create_email=input("create uinque email: ")
    create_password=input("create a new password: ")
    if create_email not in data:
        data[create_email] = create_password
    else:
        print("Your email or password already exist Try again.....")
else:
    email=input("enter your  email: ")
    password=input("Enter your password: ")
    if email in data and data[email]==password:
        print("Login sucessful....")
    else:
        print("Wrong password or email....")


