data={
    "sathvik":{"status":True,"python":100,"mysql":None,"softskills": 98},
    "Achyuth":{"status":True,"python":100,"mysql":98,"softskills": 98},
    "karthikeya":{"status":True,"python":100,"mysql":42,"softskills": 98}

}
user=input("enter the name of user: ")
if user in data:
    if data[user]["status"]:
       sum= data[user]["python"]+data[user]["mysql"]+data[user]["softskills"]
       avg=sum/3
       if avg > 80:
           print(f"congrats {user} you have done a great job..")
       elif avg > 60:
           print(f"good")
       elif avg > 40:
           print("needs to improve")
       else:
           print("you are fail in the all exams")
    else:
        print("user not found...")
            