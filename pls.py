class Person:
   def __init__(self,username, password):
     self.username = username
     self.password = password

   def login():
       #print("Please give your username") 
       #username = input()
       pass

class Member(Person):
     def __init__(self,username,password):
        Person.__init__(username,password)

class Admin(Person):
   def __init__(self):
    Person.__init__(self,"admin","admin123")

    def AddMember():
        pass

x = Admin()
print(x.password)