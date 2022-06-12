import json
import csv
from csv import writer
from typing import List

class Person:
   def __init__(self,Username, Password):
     self.Username = Username
     self.Password = Password

   def login():
       #print("Please give your username") 
       #username = input()
       pass
   
class Member(Person):
    def __init__(self,Number,GivenName,Surname,StreetAddress, ZipCode, City, EmailAddress, Username ,Password, TelephoneNumber):
        Person.__init__(self,Username,Password)
        self.Number = Number
        self.GivenName = GivenName
        self.Surname = Surname
        self.StreetAddress = StreetAddress
        self.ZipCode = ZipCode
        self.City = City
        self.EmailAddress = EmailAddress
        self.TelephoneNumber = TelephoneNumber
        
    def __iter__(self):
        return iter([self.Number, self.GivenName, self.Surname, self.StreetAddress, self.ZipCode, self.City, self.EmailAddress, self.Username, self.Password, self.TelephoneNumber,])
    def infomember(self):
        return "[0] number: " + self.Number + "\n[1] GivenName: " + self.GivenName + "\n[2] Surname: " + self.Surname +  "\n[3] StreetAddress: " + self.StreetAddress + "\n[4] ZipCode: " + self.ZipCode + "\n[5] ZipCode: " + self.City + "\n[6] EmailAddress: " + self.EmailAddress + "\n[7] Username: " + self.Username + "\n[8] Password: " + self.Password +"\n[9] telephonenumber:" +self.TelephoneNumber
class Admin(Person):
   def __init__(self):
    Person.__init__(self,"admin","admin123")
   
   def seememberlist(self):
       with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ";")
            next(csv_reader)
            for member in csv_reader:
                print(member)
   def AddMember(self):
     
        with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            OldList = csv_reader
            tester = 0
            for line in OldList:
                print(line)
                tester +=1
            NewNumber = tester 
            '''
            print("new GivenName:")
            NewGivenName = input()
            print("new Surname:")
            NewSurname = input()
            print("new StreetAddress")
            NewStreetAddress = input()
            print("new ZipCode")
            NewZipCode = input()
            print("new City")
            NewCity = input()
            print("new EmailAddress")
            NewEmailAddress = input()
            print("new Username")
            NewUsername = input()
            print("new Password")
            NewPassword = input()
            print("new TelephoneNumber")
            NewTelephoneNumber = input()
            '''
        print(NewNumber)
        NewGivenName = "hady"
        NewSurname = "Al-tamimi"
        NewStreetAddress = "Klaroen 8"
        NewZipCode = "2907GB"
        NewCity = "Rotterdam"
        NewEmailAddress ="hadyaltamimi03@gmail.com"
        NewUsername = "hady"
        NewPassword = "hady123"
        NewTelephoneNumber = "0612644634"
        newmember = Member(NewNumber, NewGivenName,NewSurname,NewStreetAddress,NewZipCode,NewCity,NewEmailAddress,NewUsername,NewPassword,NewTelephoneNumber)
        # NewMemberList = [NewNumber, NewGivenName,NewSurname,NewStreetAddress,NewZipCode,NewCity,NewEmailAddress,NewUsername,NewPassword,NewTelephoneNumber]
        with open('Members.csv', 'a',newline='') as f_object:
            writer_object = csv.writer(f_object, delimiter = ';')
            writer_object.writerow(newmember)
            
        with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            OldList = csv_reader
            tester = 0
            for line in OldList:
                print(line)
   
   def EditMember(self):
       print("What is the name of whom's account you want to edit")
       PersonChosen = input()
     
       with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            ListOfMembers = csv_reader
            
            for member in ListOfMembers: 
                if member[1] == PersonChosen:
                    print("What do you wich to edit\n")
                    print("1. Number\n2. GivenName\n3. Surname\n4. StreetAddress\n5. ZipCode\n6. City\n7. EmailAddress\n8. Username\n9. Password\n10. TelephoneNumber")
                    ChosenEdit = input()
                    if ChosenEdit == "1":
                        print("what number do you want to give to the user")
                        Newnumber = input()
                        member[0] = Newnumber
           

                    
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
#book = Book("yeet","holland","notfound","Dutch","notfound",150,"super gilles",24039,2001)
#book2 = Book("yeet","holland","notfound","Dutch","notfound",150,"wowzers",24039,2001)

x = Admin()
x.EditMember()