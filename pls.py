from dbm import ndbm
from fileinput import filename
import json
import csv
from pprint import pprint
import shutil
from datetime import date
import os
from distutils.dir_util import copy_tree
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------- BackEnd -------------------------------------------------------------------------------------------------------------------
#--------------------------------------------- -------------------------------------------------------------------------------------------------------------------
class Person:
   def __init__(self,Username, Password):
     self.Username = Username
     self.Password = Password

   def login(self):
       loggingIn = True
       print("Welcome to the library system, \nPlease login")
       while(loggingIn):
           print("Username: ")
           username = input()
           print("Password: ")
           password = input()
           if username == "admin" and password == "admin123":
               return "admin"

           with open("Members.csv",'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ";")
                next(csv_reader)
                for member in csv_reader:
                    if member != []:
                        if member[7] == username and member[8]== password:
                            user = member
                            loggingIn = False
                if loggingIn:
                    print("Invalid username and/or password, please try again")
       return user;
       
   
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

    def Menu(self):
       catalog = Catalog([])
       catalog.loadJson()
       lib = library([])
       lib.loadJson()
       while(True):
           print("Hello " + self.GivenName +",Welcome to the Public Library System")
           print("   [1] view entire catalog")
           print("   [2] search for books in the catalog\n")
           print("   [3] view entire library")
           print("   [4] search for books in the library\n")
           print("   [5] loan a book")
           print("   [6] return a book\n")
           print("   [7] log out")

           choice = input()

           if choice == "1":
                print(catalog.viewBooks())
                print("\nPress enter to return to homepage")
                input()
           elif choice == "2":
                catalog.searchBook()
           elif choice == "3":
                print(lib.viewBooks())
                print("\nPress enter to return to homepage")
                input()
           elif choice == "4":
                lib.searchBook()
           elif choice == "5":
               pass
           elif choice == "6":
               pass
           elif choice == "7":
               break
           else:
               print(50 * "\n")
               print("Invalid choice. Please pick a valid option")

class Admin(Person):
   def __init__(self):
        Person.__init__(self,"admin","admin123")

   def Menu(self):
       catalog = Catalog([])
       catalog.loadJson()
       lib = library([])
       lib.loadJson()
       while(True):
        print("Public Library System \n\n")
        print("   [1] view entire catalog")
        print("   [2] search for books in the catalog\n")

        print("   [3] Add a book to catalog")
        print("   [4] Add multiple Books to catalog")
        print("   [5] Remove a book from catalog")
        print("   [6] Edit a book in catalog\n")

        print("   [7] view entire library")
        print("   [8] search for books in the library\n")

        print("   [9] Add a book to library")
        print("   [10] Add multiple books to library")
        print("   [11] Remove a book from library")
        print("   [12] Edit a book in library\n")

        print("   [13] View list of members")
        print("   [14] Add a member to the system")
        print("   [15] Add multiple members to system")
        print("   [16] Remove a member from the system")
        print("   [17] Edit a member in the system\n")

        print("   [18] Load previous system state")
        print("   [19] Save current system state\n")

        print("   [20] Logout of Admin")
        
        choice = input()
        if choice == "1":
            print(catalog.viewBooks())
            print("\nPress enter to return to homepage")
            input()
        elif choice == "2":
            catalog.searchBook()
        elif choice == "3":
            catalog.addBook()
        elif choice == "4":
            catalog.addBooks()
        elif choice == "5":
            catalog.delBook()
        elif choice == "6":
            catalog.editBook()
        elif choice == "7":
            print(lib.viewBooks())
            print("\nPress enter to return to homepage")
            input()
        elif choice == "8":
            lib.searchBook()
        elif choice == "9":
            lib.addBook()
        elif choice == "10":
            lib.addBooks()
        elif choice == "11":
            lib.delBook()
        elif choice == "12":
            lib.editBook()
        elif choice =="13":
            self.seememberlist()
            print("\nPress enter to return to homepage")
            input()
        elif choice == "14":
            self.AddMember()
        elif choice == "15":
            self.AddMembers()
        elif choice == "16":
            self.RemoveMember()
        elif choice == "17":
            self.EditMember()
        elif choice == "18":
            self.RestoreBackup()
        elif choice == "19":
            self.CreateBackup()
        elif choice == "20":
            break
        else:
            print(50 * "\n")
            print("Invalid choice. Please pick a valid option")


   def seememberlist(self):
       with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ";")
            next(csv_reader)
            for member in csv_reader:
                if (member != []):
                    print("[" + member[0] + "]", member[1], member[2])
            

   def AddMember(self):
     
        with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            OldList = csv_reader
            tester = 0
            print("Current Members")
            self.seememberlist()
            for line in OldList:
                tester +=1
            NewNumber = tester 
            
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
            
        print("If something is wrong please type 'x' to quit, otherwise just press enter")
        if input() == 'x':
            return
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

   def AddMembers(self):
       print("Please enter the name of the file (like: 'NewList.csv')")
       fileName = input();
       while not(os.path.isfile(fileName) and fileName.endswith(".csv") ):
           if (os.path.isfile(fileName)):
               print("That file isn't a csv file, please try again")
           else:
               print("That file name doesn't exist, please try again")
           fileName = input()
       
       with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            OldList = csv_reader
            tester = 0
            for line in OldList:
                if line != []:
                    tester +=1
      
       with open("Members.csv",'a',newline='') as member_csv:
           writer_object = csv.writer(member_csv, delimiter = ';')
           with open(fileName, 'r') as csv_file:
               csv_reader = csv.reader(csv_file, delimiter = ';')
               next(csv_reader)
               for row in csv_reader:
                   if row != []:
                       row[0] = tester
                       tester += 1
                       writer_object.writerow(row)

   def RemoveMember(self):
       self.seememberlist()
       print("What is the number of the account you want to delete?")
       PersonChosen = input()

       output = list()
       with open("Members.csv", 'r') as csv_file:
           reader = csv.reader(csv_file, delimiter = ';')
           for row in reader:
               if row != []:
                   output.append(row)
                   compare = row[0]
                   if row[0] == PersonChosen:
                      output.remove(row)

       with open("Members.csv", 'w') as csv_file:
           writer = csv.writer(csv_file, delimiter = ';')
           writer.writerows(output)

   def EditMember(self):
       self.seememberlist()
       print("What is the number of the account you want to edit?")
       PersonChosen = input()
       output = list()
     
       with open("Members.csv",'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            ListOfMembers = csv_reader
            
            for member in ListOfMembers: 
                if member != []:
                    if member[0] == PersonChosen:
                        print("What do you wich to edit\n")
                        print("1. Number\n2. GivenName\n3. Surname\n4. StreetAddress\n5. ZipCode\n6. City\n7. EmailAddress\n8. Username\n9. Password\n10. TelephoneNumber")
                        ChosenEdit = input()
                        while not(ChosenEdit in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}):
                            print("Please pick a valid option")
                            ChosenEdit = input()
                        print("What do you want to change it to?")
                        NewValue = input()
                        member[int(ChosenEdit) - 1] = NewValue
                    output.append(member)

            with open("Members.csv", 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter = ';')
                writer.writerows(output)


   def CreateBackup(self):
       today = date.today()
       date_format = today.strftime("%d_%b_%Y_")
       src_file_names = ('Members.csv', 'Catalog.json', 'Books.json')
       madeFolder = False
       serial = 1
       while not madeFolder:
           try:
               os.mkdir("Backups\\" + date_format + str(serial) + '_\\' )
               date_format = date_format + str(serial) + '_'
               madeFolder = True
           except OSError as error:
               serial += 1
               pass
           
       for src_file_name in src_file_names:
           src_dir = ''
           dst_dir = 'Backups\\' + date_format +  '\\'

           src_dir = src_dir+src_file_name
           dst_file_name = src_file_name
           dst_dir = dst_dir+date_format+dst_file_name
                  
           shutil.copy2(src_dir, dst_dir)
  
           print("Backup Successful!")
   
   def RestoreBackup(self):
       i = 0
       backups = os.listdir("Backups")
       for _ in backups:
           print("["+ str(i) +"] " + _)
           i += 1
       print("Please pick a backup to be restored")
       ChosenBackup = input()
       correct = False
       while not correct:
           if ChosenBackup.isnumeric():
               if int(ChosenBackup) < i and int(ChosenBackup) >= 0:
                   correct = True
               else:
                   print("Please pick a vaild option")
                   ChosenBackup = input()
           else:
               print("Please pick a number")
               ChosenBackup = input()

       src_file_names = ('Members.csv', 'Catalog.json', 'Books.json')
       for src_file_name in src_file_names:
           dst_dir = ''
           dst_file_name = src_file_name
           src_file_name = backups[int(ChosenBackup)] + src_file_name
           src_dir = 'Backups\\' + backups[int(ChosenBackup)] + '\\'  + src_file_name
           dst_dir = dst_dir+dst_file_name
                  
           shutil.copy2(src_dir, dst_dir)
  
           print("Restoration Successful!")
           
#--------------------------------------------------------------------------
#TO DO:  
# Save to catalog file json, that is 
# After every save or edit save to json file
# Add ability to loan a bookItem from library 
#
class Catalog:
    def __init__ (self,bookList):
        self.bookList = bookList
    
    def addBook(self):
      
        with open("Catalog.json","r") as cb:
            currentBooks = json.load(cb)
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
            
                if self.__class__.__name__ == "Catalog":
                    book1 = {"author" : author,"country": country,"imageLink": imageLink,"language": language,"link": link,"pages": pages,"title":title,"ISBN": ISBN,"year":year}
                    book2 = Book(author,country,imageLink,language,link,pages,title,ISBN,year)
                else:
                    book1 = {"author" : author,"country": country,"imageLink": imageLink,"language": language,"link": link,"pages": pages,"title":title,"ISBN": ISBN,"year":year, "amount": 5}
                    book2 = BookItem(author,country,imageLink,language,link,pages,title,ISBN,year)

                check = False
                for x in self.bookList:
                   if x.ISBN == book1["ISBN"] and x.author == book1["author"] and x.title == book1["title"] and x.year == book1["year"] and book1.country == x["country"] and x.link == book1["link"] and x.pages == book1["pages"] and x.language == book1["language"] and x.imageLink == book1["imageLink"]:
                       check = True
                if check == False:       
                    currentBooks.append(book1)
                    self.bookList.append(book2)
                else:
                     print("Book already in " + self.__class__.__name__)

                fileName = self.__class__.__name__ + ".json"
                with open(fileName,"w") as p:
                    json.dump(currentBooks, p ,indent = 4)
                cb.close()
    
    def delBook(self, jsonName = "Catalog.json"):
     
      with open(jsonName,"r") as cb:
         currentBooks = json.load(cb)
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
          
      


    def editBook(self, jsonName = "Catalog.json"):
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

        with open("Catalog.json","r") as cb:
            currentBooks = json.load(cb)
       
        books = open(jsonName)      
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
                currentBooks.append(book)
                self.bookList.append(book1) # make them write to catlog json use if(__class__.__name__ == Catalog add books to cat else add bookitems to library json)
        with open("Catalog.json","w") as p:
            json.dump(currentBooks,p,indent = 4)
        cb.close()

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
        return "[0] Title: " + self.title + "\n[1] Written by: " + self.author + "\n[2] country of origin: " + self.country +  "\n[3] Pages: " + str(self.pages) + "\n[4] Written in: " + self.language + "\n[5] ISBN: " + str(self.ISBN) + "\n[6] Link: " + self.link + "\n[7] Year of publication: " + str(self.year) + "\n[8] imageLink: " + self.imageLink +"\n"
    def GetBasic(self):
        return "|Title: " + self.title + " |Written by: " + self.author
    
class BookItem(Book):
    
    def __init__(self,author,country,imageLink,language,link,pages,title,ISBN,year):
        Book.__init__(self,author,country,imageLink,language,link,pages,title,ISBN,year)
        self.amount = 5

class LoanItem(Book):
    
    def __init__(self,author,country,imageLink,language,link,pages,title,ISBN,year):
        Book.__init__(self,author,country,imageLink,language,link,pages,title,ISBN,year)
        self.loaned = False
        

class library(Catalog):

    def __init__ (self,bookList):
        Catalog.__init__(self,bookList)
            
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
    
    def searchBook(self):
        return super().searchBook()

    def addBook(self):
        return super().addBook()

    def addBooks(self,jsonName = "Books.json"):

        with open("Library.json","r") as cb:
            currentBooks = json.load(cb)
       
        books = open(jsonName)      
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
            book['amount'] = 5
            book1 = BookItem(author,country,imageLink,language,link,pages,title,ISBN,year)
            check = False
            for x in self.bookList:
               if x.ISBN == book1.ISBN and x.author == book1.author and x.title == book1.title and x.year == book1.year and book1.country == x.country and x.link == book1.link and x.pages == book1.pages and x.language == book1.language and x.imageLink == book1.imageLink:
                   check = True
            if check == False:       
                currentBooks.append(book)
                self.bookList.append(book1) # make them write to catlog json use if(__class__.__name__ == Catalog add books to cat else add bookitems to library json)
        with open("Library.json","w") as p:
            json.dump(currentBooks,p,indent = 4)
        cb.close()

    def editBook(self):
        return super().editBook("Library.json")

    def delBook(self):
        return super().delBook("Library.json")
    
    def loadJson(self):
       try:
            books = open("Library.json")      
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
                book1 = BookItem(author,country,imageLink,language,link,pages,title,ISBN,year)
                check = False
                for x in self.bookList:
                    if x.ISBN == book1.ISBN and x.author == book1.author and x.title == book1.title and x.year == book1.year and book1.country == x.country and x.link == book1.link and x.pages == book1.pages and x.language == book1.language and x.imageLink == book1.imageLink:
                        check = True
                if check == False:
                    self.bookList.append(book1)
       except:
           print("no books found")

    def loanBook(self,username): # needs user to bind loan item to member also update json library 
     ans = ""
     while(ans != "x" and ans != "X"):
         break


#testing 
#book = Book("yeet","holland","notfound","Dutch","notfound",150,"super gilles",24039,2001)
#book2 = Book("yeet","holland","notfound","Dutch","notfound",150,"wowzers",24039,2001)

#b = BookItem("yeet","holland","notfound","Dutch","notfound",150,"super gilles",24039,2001)
#b1 = BookItem("yeet","holland","notfound","Dutch","notfound",150,"wowzers",24039,2001)
#lib = Library([])
#cat = catalog([])
#cat.loadJson()
#print(cat.viewBooks())
#cat.addBooks()
#print(cat.viewBooks())
#user = Admin()
#user.RestoreBackup()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------- frontEnd -------------------------------------------------------------------------------------------------------------------
#--------------------------------------------- -------------------------------------------------------------------------------------------------------------------
isLoggedIn = False
isAdmin= False
cat = Catalog([])
person = Person("","")
temp = person.login()
if temp == "admin":
    user = Admin()
else:
    user = Member(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8], temp[9])

user.Menu()
#cat.loadJson()
#while(True):
#    print("Welcome To Our Public Library System")
#    print("Input the number in between [] to select an option below:")
    
#    if isLoggedIn == False:
#        print("   [1] Login as member")
#        print("   [2] Login as Library Administrator")

#    if isLoggedIn == True and isAdmin == False:
#        print("   [1] view entire catalog")
#        print("   [2] search for books in the catalog")
#        print("   [3] view entire library")
#        print("   [4] search for books in the catalog")
#        print("   [5] Loan a book")
#        print("   [6] return a loaned book")
#        print("   [7] Logout of account")

#    if isLoggedIn == True and isAdmin == True:
#        print("   [1] view entire catalog")
#        print("   [2] search for books in the catalog\n")

#        print("   [3] Add a book to catalog")
#        print("   [4] Add multiple Books to catalog")
#        print("   [5] Remove a book from catalog")
#        print("   [6] Edit a book in catalog\n")

#        print("   [7] view entire library")
#        print("   [8] search for books in the library\n")

#        print("   [9] Add a book to library")
#        print("   [10] Add multiple books to library")
#        print("   [11] Remove a book from library")
#        print("   [12] Edit a book in library\n")

#        print("   [13] Add a member to the system")
#        print("   [14] Remove a member from the system")
#        print("   [15] Edit a member in the system\n")

#        print("   [16] Load previous system state")
#        print("   [17] Save current system state\n")

#        print("   [18] Logout of Admin")
    
#    ans = input() 
#    if isLoggedIn == False:
#         if ans == "1":
#            person.login()
#         elif ans == "2":
#            person.login()
     
#    elif isLoggedIn == True and isAdmin == False:
#        if ans == "1":
#            cat.viewBooks()
#        elif ans == "2":
#            cat.searchBook()
#    elif isLoggedIn == True and isAdmin == True:
#        if ans == "1":
#            cat.viewBooks()
#        elif ans == "2":
#            cat.searchBook()
#    else:
#         ("Invalid Input or unavailable")

    