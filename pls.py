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

#--------------------------------------------------------------------------
class catalog:
    def __init__ (self,bookList):
        self.bookList = bookList
    
    def addBook(self):
      ans = ""
      while(True):
        print(self.viewBooks())
        print("Input author or [x] to exit")
        ans = input()
        if ans == "x" or ans == "X":
            break
        else:
            author = ans
            print("Input country: ")
            country = input()
            print("Input imageLink: ")
            imageLink = input()
            print("input language: ")
            language = input()
            print("input link: ")
            link = input()
            print("input pages: ")
            pages = input()
            print("input title: ")
            title = input()
            print("Input ISBN: ")
            ISBN = input()
            print("Input year: ")
            year = input()
            
            book_dict = {"author" : author,"country": country,"imageLink": imageLink,"language": language,"link": link,"pages": pages,"title":title,"ISBN": ISBN,"year":year}
            catalog_dicts = [Book.__dict__ for book in self.bookList]
            print(catalog_dicts)
            catalog_dicts.append(book_dict)
            with open("Catalog.json","a") as p:
                json.dump(catalog_dicts,p,indent = 4)
            
            if not (book in self.bookList):
               self.bookList.append(book)
            else:
               print("Book already in " + self.__class__.__name__)
    
    def delBook(self):
     
      ans = ""
      while(ans != "x" and ans != "X"):
        print(self.viewBooks())
        print("Input the number in between the brackets [] to select the book you want to delete")
        print("Input [x] to exit")
        ans = input()       
        try:
            if int(ans) < len(self.bookList) and int(ans) >=0:
                self.bookList.pop(int(ans)) 
                print("Succesfully Deleted")
            else:
                print("That Book is not available, try again")
        except:
            if(ans == "x" or ans  == "X"):
                break
            print("invalid Input, try again")
          
      
  



    def editBook(self):
      ans = ""
      while(ans != "x" and ans != "X"):
        print(self.viewBooks())
        print("Input the number in between the brackets [] to select the book you want to edit")
        print("Input [x] to exit")
        ans = input()       
        try:
            ans = int(ans)
            if ans < len(self.bookList) and ans >=0:
                print("Input the number in between the brackets [] to select what you want to edit")
                print(self.bookList[ans].GetInfo())
                selection = input()
                if selection == "0": 
                  print("edit title to:")
                  edit = input()
                  self.bookList[ans].title = edit
                elif selection == "1":
                  print("edit author to:")
                  edit = input()
                  self.bookList[ans].author = edit
                elif selection == "2":
                  print("edit country of origin to:")
                  edit = input()
                  self.bookList[ans].country = edit
                elif selection == "3":
                  print("edit page amount to:")
                  edit = input()
                  self.bookList[ans].pages = edit
                elif selection == "4":
                  print("edit language to:")
                  edit = input()
                  self.bookList[ans].language = edit
                elif selection == "5":
                  print("edit ISBN to:")
                  edit = input()
                  self.bookList[ans].ISBN = edit
                elif selection == "6":
                  print("edit Link to:")
                  edit = input()
                  self.bookList[ans].link = edit
                elif selection == "7":
                  print("edit Year to:")
                  edit = input()
                  self.bookList[ans].year = edit
                elif selection == "8":
                  print("edit imagelink to:")
                  edit = input()
                  self.bookList[ans].imageLink = edit
                else:
                    print("that option is not available")
            else:
                print("That Book is not available, try again")
        except:
            if(ans == "x" or ans  == "X"):
                break
            print("invalid Input, try again")

    def searchBook(self):    
        ans = ""
        while ans != "x" and ans !="X":
            ansList = []
            option = True
            print("Enter 1 or 2 to choose an option\n")
            print("  [1] search for title")
            print("  [2] search for author\n")
            print("Input anything else to exit")
            ans = input()
            if ans == "1":
                option = True
            elif ans == "2":
                option = False
            else:
               break
            print("input searchterm")
            searchTerm = str.lower(input())# turns searchterm lowercase to avoid not finding books because of capitalization                                      
            for book in self.bookList:
                if searchTerm in str.lower(book.title) and option == True:
                    ansList.append(book)
                elif searchTerm in str.lower(book.author) and option == False:
                    ansList.append(book)     
            print(self.viewBooks(ansList)) # returns a list of books that fit that contain the searchterm.

    
    def addBooks(self,jsonName = "Books.json"):
        self.loadJson()
        books = open(jsonName)      
        bookz = json.load(books)
        books.close()
        bookdiclist = []
        for book in bookz:
            author = book['author'] 
            country = book['country']
            imageLink = book['imageLink']
            language = book['language']
            link = book['link']
            pages = book['pages']
            title = book['title']
            ISBN = book['ISBN']
            year = book['year']
            book1 = Book(author,country,imageLink,language,link,pages,title,ISBN,year)
            for x in self.bookList:
               if x.ISBN == book1.ISBN and x.author == book1.author and x.title == book1.title and x.year == book1.year and book1.country == x.country and x.link == book1.link and x.pages == book1.pages and x.language == book1.language and x.imageLink == book1.imageLink:
                bookdiclist.append(book)
                self.bookList.append(book1) # make them write to catlog json use if(__class__.__name__ == Catalog add books to cat else add bookitems to library json)
        with open("Catalog.json","w") as p:
            json.dump(bookdiclist,p,indent = 4)
        
    def viewBooks(self, books = None):
        if books == None:
            books = self.bookList
        i = 0
        view = "Books in " + self.__class__.__name__ +":\n"
        for book in books:
            view += "["+str(i)+"]" + book.GetBasic()+"\n" 
            i+=1
        if view == "Related books:\n":
            return "---- No books found ----"
        else:
            return view

    def loadJson(self):
       try:
            books = open("Catalog.json")      
            bookz = json.load(books)
            books.close()
            for book in bookz:
                author = book['author'] 
                country = book['country']
                imageLink = book['imageLink']
                language = book['language']
                link = book['link']
                pages = book['pages']
                title = book['title']
                ISBN = book['ISBN']
                year = book['year']
                book1 = Book(author,country,imageLink,language,link,pages,title,ISBN,year)
                check = False
                for x in self.bookList:
                    if x.ISBN == book1.ISBN and x.author == book1.author and x.title == book1.title and x.year == book1.year and book1.country == x.country and x.link == book1.link and x.pages == book1.pages and x.language == book1.language and x.imageLink == book1.imageLink:
                        check = True
                if check == False:
                    self.bookList.append(book1)
       except:
           print("no books found")
    
    def saveJson(self):
       pass

        
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
        return "[0] Title: " + self.title + "\n[1] Written by: " + self.author + "\n[2] country of origin: " + self.country +  "\n[3] Pages: " + str(self.pages) + "\n[4] Written in: " + self.language + "\n[5] ISBN: " + str(self.ISBN) + "\n[6] Link: " + self.link + "[7] Year of publication: " + str(self.year) + "\n[8] imageLink: " + self.imageLink +"\n"
    def GetBasic(self):
        return "|Title: " + self.title + " |Written by: " + self.author
    
class BookItem(Book):
    
    def __init__(self,author,country,imageLink,language,link,pages,title,ISBN,year):
        Book.__init__(self,author,country,imageLink,language,link,pages,title,ISBN,year)
        self.amount = 3

class LoanItem(Book):
    
    def __init__(self,author,country,imageLink,language,link,pages,title,ISBN,year):
        Book.__init__(self,author,country,imageLink,language,link,pages,title,ISBN,year)
        self.loaned = False
        

class Library(catalog):

    def __init__ (self,bookList):
        catalog.__init__(self,bookList)
            
    def viewBooks(self, books = None):
        if books == None:
            books = self.bookList
        i = 0
        view = "BookItems in " + self.__class__.__name__+":\n"
        for bookItem in books:
            view += "["+str(i)+"]" + bookItem.GetBasic() +" | " + str(bookItem.amount) + " |"
            i += 1
            if bookItem.amount > 0:
                view += "available\n"
            else:
                view += "unavailable\n"      
        if view == "Related books:\n":
            return "---- No books found ----"
        else:
            return view

    def loanBook(self,username): # needs user to bind loan item to member also update json library 
     ans = ""
     while(ans != "x" and ans != "X"):
         break




