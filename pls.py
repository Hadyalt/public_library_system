from _typeshed import Self
from typing import ItemsView
import json
import csv

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

        with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                print(line)

class catalog:
    def __init__ (self,bookList):
        self.bookList = bookList
    
    def addBook(self,book):
        if not (book in self.bookList):
          self.bookList.append(book)
        else:
           return"Book already in " + self.__class__.__name__
    
    def delBook(self):
      print(self.viewBooks())
      print("Input the number in between the brackets [] that you want to delete")
      ans = input()     
      self.bookList.pop(int(ans))



    def editBook(self):
        pass

    def searchBook(self,searchTerm):
        ansList = []
        searchTerm = str.lower(searchTerm) # turns searchterm lowercase to avoid not finding books because of capitalization
        for book in self.bookList:
            if searchTerm in str.lower(book.title):
                ansList.append(book)
            elif searchTerm in str.lower(book.author):
                ansList.append(book)     
        return ansList # returns a list of books that fit that contain the searchterm.
        
    
    def addBooks(self):
        pass
    
    def viewBooks(self, books = None):
        if books == None:
            books = self.bookList
        i = 0
        view = "Books in: " + self.__class__.__name__ +"\n"
        for book in books:
            view += "["+str(i)+"]" + book.GetBasic()+"\n" 
            i+=1
        if view == "Related books:\n":
            return "---- No books found ----"
        else:
            return view

        
class Book:
    def __init__(self,author,country,imageLink,language,link,pages,title,ISBN,year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.ISBN = ISBN
        self.year = year
    
    def GetInfo(self):
        return "Title: " + self.title + "\nWritten by: " + self.author + "\ncountry of origin: " + self.country +  "\nPages: " + str(self.pages) + "\nWritten in: " + self.language + "\nISBN: " + str(self.ISBN) + "\nLink: " + self.link + "\nYear of publication: " + str(self.year) + "\nimageLink: " + self.imageLink +"\n"
    def GetBasic(self):
        return "|Title: " + self.title + " |Written by: " + self.author
    
class bookItem:
    
    def __init__(self,book):
        self.book = book;
        self.amount = 3
    
class Library(catalog):

    def __init__ (self,bookList):
        catalog.__init__(self,bookList)
    
    def searchBook(self,searchTerm):
        ansList = []
        searchTerm = str.lower(searchTerm) # turns searchterm lowercase to avoid not finding books because of capitalization
        for bookItem in self.bookList:
            if searchTerm in str.lower(bookItem.book.title):
                ansList.append(book)
            elif searchTerm in str.lower(bookItem.book.author):
                ansList.append(book)     
        return ansList # returns a list of books that fit that contain the searchterm.
          
    def viewBooks(self, books = None):
        if books == None:
            books = self.bookList
        i = 0
        view = "BookItems in: " + self.__class__.__name__+"\n"
        for bookItem in books:
            view += "["+str(i)+"]" + bookItem.book.GetBasic() +" |" + str(bookItem.amount) + " |"
            i += 1
            if bookItem.amount > 0:
                view += "available\n"
            else:
                view += "unavailable\n"      
        if view == "Related books:\n":
            return "---- No books found ----"
        else:
            return view


# testing 
book = Book("yeet","holland","notfound","Dutch","notfound",150,"super gilles",24039,2001)
book2 = Book("yeet","holland","notfound","Dutch","notfound",150,"wowzers",24039,2001)

x = Admin()
print(x.password)