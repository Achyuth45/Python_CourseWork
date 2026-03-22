import json

with open("new.json","w") as f:
    data=[{'id':"1","name":"Achyuth"},
          {'id':"2","name":"Harish"},
          {'id':"3","name":"Karthikeya"},
          {'id':"4","name":"Sandeep"},
          ]
    json.dump(data,f,indent=4)
    print("data transfered sucessfully...")
    