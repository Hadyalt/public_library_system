class Person:
   def __init__(self,username, password):
     self.username = username
     self.password = password

class Member(Person):
     def __init__(self,username,password):
        Person.__init__(username,password)

class Admin(Person):
   def __init__(self):
    Person.__init__(self,"admin","admin123")


x = Admin()
print(x.password)