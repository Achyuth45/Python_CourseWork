class Snapchat:
    def __init__(self,username,password,friends):
        self.username=username
        self.__password=password
        self._friends=friends


    def getpassword(self):
        return self.__password
    
    def setpassword(self,new_password):
        self.__password = new_password

    @property
    def showfriends(self):
        return self._friends
    @showfriends.setter
    def showfriends(self,new_friend):
        self._friends.append(new_friend)

s = Snapchat("Achyuth",12345,["harish,sandeep,karthikeya"])
print(f"Name before modification: {s._friends}")
s.username = "harish"
print(s.getpassword())
s.setpassword("hhy")
print(s.getpassword())
print(s.showfriends)
s.showfriends = "anil"
print(s.showfriends)

        