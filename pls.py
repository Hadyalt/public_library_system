from _typeshed import Self
from typing import ItemsView


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


class catalog:
    def __init__ (self,bookList):
        self.bookList = bookList
    
    def addBook(self,bookItem):
        self.bookList += bookItem

    def searchBook(self,searchTerm):
        ansList = []
        for book in self.bookList:
            if searchTerm == book.title:
                ansList.append(book)
            if searchTerm == book.author:
                ansList.appen(book)
     
        return ansList
        
    
    def addBooks(self):
        pass

    def viewbooks(self, books = Self.bookList):
        pass

class Book:
    def __init__(self,auhtor,country,imageLink,language,link,pages,title,ISBN,year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.ISBN = ISBN
        self.year = year
    
class BookItem(Book):

    def __init__(self,amount):
        Book.__init__(self)
        amount = 3
    
    




x = Admin()
print(x.password)