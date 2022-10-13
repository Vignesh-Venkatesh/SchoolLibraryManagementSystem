"""
Created on Tue Jul 28 16:10:47 2020

@author: vignu
"""
import mysql.connector
import time
from datetime import timedelta
from datetime import datetime
from datetime import date



#====== initializing database ===============================
db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="root",
                             database="schoolproject",
                             buffered=True)
#============================================================

# Creating mySQL cursors for later use
cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
cursor4 = db.cursor()
cursor5 = db.cursor()
cursor6 = db.cursor()
cursor7 = db.cursor()

class Getdata:
    
    global ctr
    ctr = 0
    
    def __init__(self):
        self.passwd = ''
        
    def getInfo(self): # Used for getting the admission number of the student
        global ad_no
        ad_no = (input("\nEnter Admission Number:"))
        ad_no = str(ad_no)
        Getdata.verifyAdno(self)
    
    def verifyAdno(self): # Verifies if the admission number exists in the database
        command = "SELECT admission_no FROM student"
        cursor1.execute(command)
        count = False
        for i in cursor1: # This for loop checks if the admission number that the user provided exists in the database
            i = i[0]
            i = str(i)
            if ad_no==i:
                count = True
                Getdata.getPassword(self)
            
        if count==False: # If the admission number does not exist then it gives the following message
            print("\n===========================================")
            print("\tINVALID ADMISSION NUMBER\t")
            print("\t        TRY AGAIN\t")
            print("===========================================")
            Getdata.getInfo(self)
        
    def getPassword(self): # This function is used for getting the password from the user
        self.passwd = input("\nEnter password:")
        Getdata.verifyPassword(self)
        
    
    
    def verifyPassword(self): # This function verifies if the password typed matches for the admission number given
        command = "SELECT password FROM student WHERE admission_no="+ad_no
        cursor1.execute(command)

        for i in cursor1:
            i = ''.join(i)
        
        command2 = "SELECT first_name FROM student WHERE admission_no="+ad_no
        command3 = "SELECT last_name FROM student WHERE admission_no="+ad_no
        cursor2.execute(command2)
        cursor3.execute(command3)

        if self.passwd == i: # If the password is correct
            for j in cursor2:
                j = ''.join(j)
            for k in cursor3:
                k = ''.join(k)

            name = j+" "+k   
            print("\n")
            print("Welcome",name)
            Student.studentChoice(self)
        else: # If the password is wrong
            print("\n===============================")
            print("\tINVALID PASSWORD\t")
            print("\t   TRY AGAIN\t")
            print("===============================")
            global ctr
            ctr = ctr+1
            if ctr==5: # Checks if the user has inputted the wrong password for 5 times
                print('\n')
                print("=====================================")
                print("\tMAXIMUM TRIES REACHED\t")
                print("\tPLEASE TRY AGAIN LATER\t")
                print("=====================================")
                
                time.sleep(3) # Closes the program after 3 seconds
            
            else:
                Getdata.getPassword(self)


class Student:
    
    global ctr
    ctr = 0
    
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.student_email = ''
        self.username = ''
        self.password = ''
        self.choice = ''
        
    def studentChoice(self): # Gives students various options to choose
        print("\n")
        print("=============================================")
        print("|              STUDENT OPTIONS              |")
        print("=============================================")
        print("|       ENTER 1 TO CHECK YOUR PROFILE       |")
        print("|       ENTER 2 FOR BOOK OPTIONS            |")
        print("|       ENTER 3 FOR FIND OPTIONS            |")
        print("|       ENTER 4 TO ISSUE A BOOK             |")
        print("|       ENTER E TO EXIT                     |")
        print("=============================================")
        print('\n')

        self.choice = input("ENTER YOUR CHOICE: ")
        self.choice = self.choice.lower()

        if self.choice == '1': # Redirects to my profile option
            Student.myProfileOption(self)
        elif self.choice =='2': # Redirects to books option
            Student.bookOption(self)
        elif self.choice == '3': # Redirects to find options
            Books.find(self)
        elif self.choice == '4': # Redirects to issue options
            Issue.issueBook(self)
        elif self.choice == 'e': # Exits the program
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else: # For wrong inputs, it shows the following message
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Student.studentChoice(self)

    def myProfileOption(self): # Gives student various " My Profile " options
        print("\n")
        print("===============================================")
        print("|                 MY PROFILE                  |")
        print("===============================================")
        print("|       ENTER 1 TO CHANGE YOUR PASSWORD       |")
        print("|       ENTER 2 TO CHECK FINES                |")
        print("|       ENTER 3 TO CHECK BOOKS ISSUED         |")
        print("|       ENTER B TO GO BACK                    |")
        print("|       ENTER E TO EXIT                       |")
        print("===============================================")
        print('\n')

        self.choice = input("Enter choice: ")
        self.choice = self.choice.lower()

        if self.choice == '1': # Redirects to change password
            Student.changePassword(self)
        elif self.choice == '2': # Redirects to check fines
            Issue.checkFine(self)
        elif self.choice == '3': # Redirects to check issued books
            Issue.checkIssuedBooks(self)
        elif self.choice == 'b': # Redirects to Student options
            Student.studentChoice(self)
        elif self.choice == 'e': # Exits the program
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else: # For invald inputs, the following message is printed
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Student.myProfileOption(self)

    def bookOption(self): # Gives student various " Book Options "
        print("\n")
        print("===================================")
        print("|          BOOK OPTIONS           |")
        print("===================================")
        print("|    ENTER 1 TO SEE ALL BOOKS     |")
        print("|    ENTER 2 TO CHECK GENRES      |")
        print("|    ENTER 3 TO READ OVERVIEWS    |")
        print("|    ENTER B TO GO BACK           |")
        print("|    ENTER E TO EXIT              |")
        print("===================================")

        print("\n")

        self.choice = input("Enter Choice: ")

        if self.choice == '1': # Redirects to show books
            Books.showBooksStudent(self)
        elif self.choice == '2': # Redirects to show genres
            Books.showGenre(self)
        elif self.choice == '3': # Redirects to read overviews of books
            Issue.readOverviews(self)
        elif self.choice == 'b': # Redirects to go back
            Student.studentChoice(self)
        elif self.choice == 'e': # Exits the program
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else: # For invalid inputs the following message is printed
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Student.bookOption(self)
        
    def changePassword(self): # Used to change the student's password
      
        self.password = input("Enter old password: ")

        command = "SELECT password FROM student WHERE admission_no="+str(ad_no)
        cursor1.execute(command)
        
        for i in cursor1:
            i = ''.join(i)
            
        if i == self.password:
            # Asking for new password
            inp = input("Enter new password: ") 
            # Asking confirmation as to whether to change password
            check = input("ARE YOU SURE YOU WANT TO CHANGE YOUR PASSWORD TO "+inp+" [Y/N]: ") 
            check = check.upper()
            
            if check == 'Y': # If users says "Y" the password is changed
                inp = "'"+inp+"'"
                command = "UPDATE student SET password ="+inp+"WHERE admission_no="+str(ad_no)
                cursor1.execute(command)
                db.commit()
                print("===================================")
                print("|  PASSWORD CHANGED SUCCESSFULLY  |")
                print("===================================")
                Student.myProfileOption(self)
            elif check == 'N': # If user says "N", it redirects it to " My Profile "
                Student.myProfileOption(self)
            else: # For wrong inputs, it prints the following message
                print("\n")
                print("=====================")
                print("|   INVALID INPUT   |")
                print("=====================")
                Student.changePassword(self)
        else: # For the wrong password inputted, it prints the following message
            print("=========================")
            print("|    INVALID PASSWORD   |")
            print("|       TRY AGAIN       |")
            print("=========================")
            global ctr
            ctr = ctr+1
            if ctr==5: # Checks if the user has inputted the wrong password for 5 times
                print('\n')
                print("==============================")
                print("\tMAXIMUM TRIES REACHED\t")
                print("\tPLEASE TRY AGAIN LATER\t")
                print("==============================")
                
                time.sleep(3) # Closes the program after 3 seconds
            
            else:
                Student.changePassword(self)

            
class Books(Student):
    
    def __init__(self): # Initialization
        self.book_id = 0
        self.book_name = ''
        self.book_genre = ''
        self.book_author = ''
        self.quantity = 0
        self.choice = ''
        self.genreChoice = ''
        self.book_id = ''

    def writeOverviews(self):
        command = "SELECT book_name,book_id FROM BOOKS"
        cursor1.execute(command)

        print("\n")
        equalto = "="*120
        print(equalto)
        space = 49*' '
        space2 = 45*' '
        print('|'+space+"MISSING BOOK OVERVIEWS"+space2+"  |")
        print(equalto)
        for k in cursor1:
            j = k[1]
            j = str(j)
            i = k[0]
            i = ''.join(i)
            f_name = 'Overviews/'+i+'.txt'
            try:
                f = open(f_name)
                l = f.readlines()
                f.close()
            except:
                if len(i)<65:
                    difference = 70-len(i)
                    space = difference*' '
                    i = i+space
                if len(j)<5:
                    difference = 10-len(j)
                    space = difference*' '
                    j = j+space
                print('          ',j,i," DOES NOT EXIST")
                
            else:
                if len(l)==0:
                    if len(i)<65:
                        difference = 70-len(i)
                        space = difference*' '
                        i = i+space
                    if len(j)<5:
                        difference = 10-len(j)
                        space = difference*' '
                        j = j+space
                    print('          ',j,i," DOES NOT CONTAIN CONTENT")
                    
        print(equalto)
    
        print("\n")
        book_id = input("Enter book id of the book you want to write the overview about. To go back enter (B): ")
        book_id = book_id.lower()

        if book_id == 'b':
            Admin.bookOption(self)
        else:
            pass
            

        command = "SELECT book_id FROM books"
        cursor1.execute(command)

        check = False
            
        
        for i in cursor1:
            i = i[0]
            i = str(i)
            if i == book_id:
                check = True
                break
            
        if check == False:
            print('\n')
            print("==========================")
            print("| BOOK ID DOES NOT EXIST |")
            print("==========================")
            Admin.bookOption(self)
            

        
        command = "SELECT book_name FROM books WHERE book_id="+book_id
        cursor2.execute(command)

        for i in cursor2:
            book_name = ''.join(i)

        overview = []

        for i in range(1,100):
            print('\n')
            ask = "Enter Overview For '"+book_name+"' : "
            ask = input(ask)
            print('\n')
            inp = input("DO YO WISH TO WRITE FURTHER? [Y/N] : ")
            inp = inp.lower()
            if inp=='y':
                overview = overview+ask.split()
                continue
            elif inp =='n':
                overview = overview+ask.split()
                break
            else:
                print('\n')
                print("==============================")
                print("|        INVALID INPUT       |")
                print("|        OVERVIEW LOST       |")
                print("|       PLEASE TRY AGAIN     |")
                print("==============================")
                Books.writeOverviews(self)
            

        command = "SELECT book_name FROM books WHERE book_id="+book_id
        cursor2.execute(command)

        for i in cursor2:
            i = ''.join(i)
            side_space = 10*' '
            name = "|"+side_space+"OVERVIEW OF : "+i+side_space+"|"

        dashed_line = "="*len(name)

        write1 = dashed_line+'\n'
        write1 = write1+name+'\n'
        write1 = write1+dashed_line+'\n'

        req_length = len(dashed_line)
        write2 = "| "
        length = req_length-4
        req_length = length

        for i in overview:
            if len(i)<length:
                write2 = write2+i+' '
                length = length-len(i)-1
                if length<=len(i):
                    space = (length+1)*' '
                    space = space+"|"
                    write2 = write2+space+"\n"
                    write2 = write2+"| "
                    length = req_length
            elif len(i)>=length:
                space = (length+1)*" "
                space = space+"|"
                write2 = write2+space+"\n"
                write2 = write2+"| "+i+" "
                length = req_length
                length = length-len(i)-1

        space = (length+1)*' '
        write2 = write2+space+"|"+"\n"
        write2 = write2+dashed_line+"\n"
        overview = write1+write2

        command = "SELECT book_name FROM books WHERE book_id="+book_id
        cursor3.execute(command)

        for k in cursor3:
            i = k[0]
            i = ''.join(i)
            name = "Overviews/"+i+".txt"
            f = open(name,"w")
            f.writelines(overview)
            f.close()
        print('\n')
        print("===================================")
        print("| OVERVIEW PUBLISHED SUCCESSFULLY |")
        print("===================================")
            
        Admin.bookOption(self)

    def getMissingOverviews(self):
        
        command = "SELECT book_name,book_id FROM BOOKS"
        cursor1.execute(command)

        print("\n")
        equalto = "="*120
        print(equalto)
        space = 49*' '
        space2 = 45*' '
        print('|'+space+"MISSING BOOK OVERVIEWS"+space2+"  |")
        print(equalto)
        for k in cursor1:
            j = k[1]
            j = str(j)
            i = k[0]
            i = ''.join(i)
            f_name = 'Overviews/'+i+'.txt'
            try:
                f = open(f_name)
                l = f.readlines()
                f.close()
            except:
                if len(i)<65:
                    difference = 70-len(i)
                    space = difference*' '
                    i = i+space
                if len(j)<5:
                    difference = 10-len(j)
                    space = difference*' '
                    j = j+space
                print('          ',j,i," DOES NOT EXIST")
                
            else:
                if len(l)==0:
                    if len(i)<65:
                        difference = 70-len(i)
                        space = difference*' '
                        i = i+space
                    if len(j)<5:
                        difference = 10-len(j)
                        space = difference*' '
                        j = j+space
                    print('          ',j,i," DOES NOT CONTAIN CONTENT")
                    
        print(equalto)
        Admin.bookOption(self)
        

        
    def addBooks(self): # Used for adding books into the table
        
        l=[]
        print('\n')

        command = "SELECT book_id FROM books"
        cursor1.execute(command)

        for i in cursor1:
            i = i[0]
            l.append(i)
        
        # Checks for missing book id's
        empty_list=[]
        end = l[-1]+1

        for i in range(0,len(l)):
            for j in range(1,end): # start,stop+1
                if j not in l and j not in empty_list :
                    empty_list.append(j)
        
        print("===========================")
        print("|    MISSING BOOK ID's    |")
        print("===========================")
        for i in empty_list:
            print("           ",i)
        print("===========================")
        print('\n')

        # Shows the final book id so that the admin knows which was the final book id
        print('==========================')
        print("  FINAL BOOK ID : ",l[-1],)
        print("==========================")
        print('\n')
        self.book_id = int(input("Enter Book ID: "))

        # Checking if the book id already exists or not
        command = "SELECT book_id FROM books"
        cursor1.execute(command)
        for i in cursor1:
            i = i[0]
            
            if i==self.book_id:
                print('\n')
                print('==========================')
                print('| BOOK ID ALREADY EXISTS |')
                print('==========================')
                time.sleep(1)
                Books.addBooks(self)
            
        self.book_name = input("Enter Book Name: ")
        name = self.book_name.lower()

        command = "SELECT book_name FROM books"
        cursor1.execute(command)

        for i in cursor1:
            i = ''.join(i)
            i = i.lower()
            if i==name:
                print('\n')
                print("=======================")
                print("| BOOK ALREADY EXISTS |")
                print("=======================")
                time.sleep(1)
                Admin.bookOption(self)
            
        self.author = input("Enter Author Name: ")
        print('\n')
        command = "SELECT DISTINCT genre FROM books"
        cursor1.execute(command)
        
        print("\n")
        print("=======================================")
        print("|          GENRES AVAILABLE           |")
        print("=======================================")
        
        for i in cursor1:
            i = ''.join(i)
            print('\t      ',i)
            
        print("=======================================")
        print('\n')
        time.sleep(1)
        self.genre = input("Enter Book's Genre: ")        
        self.quantity = int(input("Enter Quantity: "))
        # Conversion of int to str for joining later
        self.book_id = str(self.book_id)
        self.quantity = str(self.quantity)
        # Command
        command = "INSERT INTO books VALUES("+self.book_id+',"'+self.book_name+'","'+self.genre+'","'+self.author+'",'+self.quantity+")"
        # Executing the command and inserting the values into the table
        cursor1.execute(command)
        db.commit()
        print('\n')
        print('==============================================')
        print('|          BOOK SUCCESSFULLY ADDED           |')
        print('==============================================')
        time.sleep(1)
        Admin.bookOption(self)

    def find(self): # Find options
        print("\n")
        print("======================================")
        print("|            FIND OPTIONS            |")
        print("======================================")
        print("|  ENTER 1 TO FIND USING BOOK NAME   |")
        print("|  ENTER 2 TO FIND USING AUTHOR      |")
        print("|  ENTER B TO GO BACK                |")
        print("|  ENTER E TO EXIT                   |")
        print("======================================")

        self.choice = input("Enter choice: ")
        self.choice = self.choice.lower()

        if self.choice == '1': # Used for searching a particular book
            Books.searchBooks(self)
        elif self.choice == '2': # Used for searching a particular author
            Books.searchAuthor(self)
        elif self.choice == 'b': # Used for going back to student options
            Student.studentChoice(self)
        elif self.choice == 'e': # Used tp exit the program
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else: # For invalid inputs, the following message is printed
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Books.find(self)
    
    def searchAuthor(self): # Used for searching a particular author
        print("\n")
        self.author = input("Enter Author Name: ")

        # Command
        command1 = "SELECT book_id FROM books WHERE quantity!=0 AND author LIKE"+"'%"+self.author+"%' ORDER BY author"
        command2 = "SELECT book_name FROM books WHERE quantity!=0 AND author LIKE"+"'%"+self.author+"%' ORDER BY author"
        command3 = "SELECT author FROM books WHERE quantity!=0 AND author LIKE"+"'%"+self.author+"%' ORDER BY author"
        command4 = "SELECT genre FROM books WHERE quantity!=0 AND author LIKE"+"'%"+self.author+"%' ORDER BY author"
        command5 = "SELECT quantity FROM books WHERE quantity!=0 AND author LIKE"+"'%"+self.author+"%' ORDER BY author"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        
        equalto = '='*170
        print("\n")
        print(equalto)
        print(" BOOK ID \t BOOK NAME \t\t\t\t\t\t\t      AUTHOR \t\t\t                  GENRE                      QUANTITY")
        print(equalto)
        for i in cursor1:            
            for j in cursor2:            
                for k in cursor3:                    
                    for l in cursor4:
                        for m in cursor5:
                            m = m[0]
                            m = str(m)
                            m = ''.join(m)
                            break
                        l = ''.join(l)
                        if len(l)<30:
                            difference = 30-len(l)
                            space = difference*' '
                            l = l+space 
                        break
                    k = ''.join(k)
                    if len(k)<65:
                        difference = 45-len(k)
                        space = difference*' '
                        k = k+space  
                    break
                j = ''.join(j)
                if len(j)<65:
                    difference = 65-len(j)
                    space = difference*' '
                    j = j+space 
                break
            i = i[0]
            i = str(i)
            i = ''.join(i)
            if len(i)<5:
                i = i+'\t\t'
            
            print('   ',i,j,k,l,m)
        print(equalto)
        time.sleep(1)

        self.choice = input("Do you wish to issue any book? [Y/N] : ")
        self.choice = self.choice.lower()

        if self.choice == 'y':
            Issue.issueBook(self)
        elif self.choice == 'n':
            Books.find(self)
        else:
            print("=================")
            print("| INVALID INPUT |")
            print("=================")
            time.sleep(1)
            Books.searchAuthor(self)
        
    def searchBooks(self): # Used for searching books
        print("\n")
        self.book_name = input("Enter Book Name: ")

        # Command
        command1 = "SELECT book_id FROM books WHERE quantity!=0 AND book_name LIKE"+"'%"+self.book_name+"%' ORDER BY book_id"
        command2 = "SELECT book_name FROM books WHERE quantity!=0 AND book_name LIKE"+"'%"+self.book_name+"%' ORDER BY book_id"
        command3 = "SELECT author FROM books WHERE quantity!=0 AND book_name LIKE"+"'%"+self.book_name+"%' ORDER BY book_id"
        command4 = "SELECT genre FROM books WHERE quantity!=0 AND book_name LIKE"+"'%"+self.book_name+"%' ORDER BY book_id"
        command5 = "SELECT quantity FROM books WHERE quantity!=0 AND book_name LIKE"+"'%"+self.book_name+"%' ORDER BY book_id"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        
        equalto = '='*170
        print("\n")
        print(equalto)
        print(" BOOK ID \t BOOK NAME \t\t\t\t\t\t\t      AUTHOR \t\t\t                  GENRE                      QUANTITY")
        print(equalto)
        for i in cursor1:            
            for j in cursor2:            
                for k in cursor3:                    
                    for l in cursor4:
                        for m in cursor5:
                            m = m[0]
                            m = str(m)
                            m = ''.join(m)
                            break
                        l = ''.join(l)
                        if len(l)<30:
                            difference = 30-len(l)
                            space = difference*' '
                            l = l+space 
                        break
                    k = ''.join(k)
                    if len(k)<65:
                        difference = 45-len(k)
                        space = difference*' '
                        k = k+space  
                    break
                j = ''.join(j)
                if len(j)<65:
                    difference = 65-len(j)
                    space = difference*' '
                    j = j+space 
                break
            i = i[0]
            i = str(i)
            i = ''.join(i)
            if len(i)<5:
                i = i+'\t\t'
            
            print('   ',i,j,k,l,m)
        print(equalto)
        time.sleep(1)
        

        self.choice = input("Do you wish to issue any book? [Y/N] : ")
        self.choice = self.choice.lower()

        if self.choice == 'y':
            Issue.issueBook(self)
        elif self.choice == 'n':
            Books.find(self)
        else:
            print("=================")
            print("| INVALID INPUT |")
            print("=================")
            time.sleep(1)
            Books.searchBooks(self)
        
        
    def showBooksStudent(self): #This function is to show books to student
        # Command
        command1 = "SELECT book_id FROM books WHERE quantity!=0"
        command2 = "SELECT book_name FROM books WHERE quantity!=0"
        command3 = "SELECT author FROM books WHERE quantity!=0"
        command4 = "SELECT genre FROM books WHERE quantity!=0"
        command5 = "SELECT quantity FROM books WHERE quantity!=0"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        
        equalto = '='*170
        print("\n")
        print(equalto)
        print(" BOOK ID \t BOOK NAME \t\t\t\t\t\t\t      AUTHOR \t\t\t                  GENRE                      QUANTITY")
        print(equalto)
        for i in cursor1:            
            for j in cursor2:            
                for k in cursor3:                    
                    for l in cursor4:
                        for m in cursor5:
                            m = m[0]
                            m = str(m)
                            m = ''.join(m)
                            break
                        l = ''.join(l)
                        if len(l)<30:
                            difference = 30-len(l)
                            space = difference*' '
                            l = l+space 
                        break
                    k = ''.join(k)
                    if len(k)<65:
                        difference = 45-len(k)
                        space = difference*' '
                        k = k+space  
                    break
                j = ''.join(j)
                if len(j)<65:
                    difference = 65-len(j)
                    space = difference*' '
                    j = j+space 
                break
            i = i[0]
            i = str(i)
            i = ''.join(i)
            if len(i)<5:
                i = i+'\t\t'
            
            print('   ',i,j,k,l,m)
        print(equalto)
        time.sleep(1)
        
        self.choice = input("Do you wish to issue any book? [Y/N] : ")
        self.choice = self.choice.lower()

        if self.choice == 'y':
            Issue.issueBook(self)
        elif self.choice == 'n':
            Student.bookOption(self)
        else:
            print("=================")
            print("| INVALID INPUT |")
            print("=================")
            time.sleep(1)
            Books.showBooksStudent(self)
        
    def showBooksAdmin(self): #This function is to show books to admin
        # Command
        command1 = "SELECT book_id FROM books"
        command2 = "SELECT book_name FROM books"
        command3 = "SELECT author FROM books"
        command4 = "SELECT genre FROM books"
        command5 = "SELECT quantity FROM books"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        
        equalto = "="*170
        print("\n")
        print(equalto)
        print(" BOOK ID \t BOOK NAME \t\t\t\t\t\t\t      AUTHOR \t\t\t                  GENRE                      QUANTITY")
        print(equalto)
        for i in cursor1:            
            for j in cursor2:            
                for k in cursor3:                    
                    for l in cursor4:
                        for m in cursor5:
                            m = m[0]
                            m = str(m)
                            m = ''.join(m)
                            break
                        l = ''.join(l)
                        if len(l)<30:
                            difference = 30-len(l)
                            space = difference*' '
                            l = l+space 
                        break
                    k = ''.join(k)
                    if len(k)<65:
                        difference = 45-len(k)
                        space = difference*' '
                        k = k+space  
                    break
                j = ''.join(j)
                if len(j)<65:
                    difference = 65-len(j)
                    space = difference*' '
                    j = j+space 
                break
            i = i[0]
            i = str(i)
            i = ''.join(i)
            if len(i)<5:
                i = i+'\t\t'
            
            print('   ',i,j,k,l,m)

        print(equalto)
        Admin.bookOption(self)
            
    def showGenre(self): # Used for showing genres
        command = "SELECT DISTINCT genre FROM books ORDER BY genre"
        cursor1.execute(command)
        
        print("\n")
        print("=======================================")
        print("\t   GENRES AVAILABLE \t\t")
        print("=======================================")
        
        for i in cursor1:
            i = ''.join(i)
            print('\t      ',i)
            
        print("=======================================")

        self.choice = input("\nDO YOU WANT TO SELECT A PARTICULAR GENRE? [Y/N] :")        
        self.choice = self.choice.upper()
        if self.choice == 'Y':
            Books.selectGenre(self)
        elif self.choice == 'N':
            Student.studentChoice(self)
        else:
            print("\n=============================")
            print("\tINVALID INPUT\t")
            print("\t  TRY AGAIN\t")
            print("=============================")
            Books.showGenre(self)

    def selectGenre(self): # Used for selecting a particular genre
        self.genreChoice = input("\nEnter The Name Of The Genre You Want To Explore: ")
        self.genreChoice = self.genreChoice.lower()
        command = "SELECT genre FROM books"
        cursor1.execute(command)
        check = False
        for i in cursor1:
            i = ''.join(i)
            i = i.lower()
            if i == self.genreChoice:
                check = True
                command1 = "SELECT book_id FROM books WHERE genre LIKE "+"'"+self.genreChoice+"'"+" AND quantity!=0"
                command2 = "SELECT book_name FROM books WHERE genre LIKE "+"'"+self.genreChoice+"'"+" AND quantity!=0"
                command3 = "SELECT author FROM books WHERE genre LIKE "+"'"+self.genreChoice+"'"+" AND quantity!=0"
                command4 = "SELECT genre FROM books WHERE genre LIKE "+"'"+self.genreChoice+"'"+" AND quantity!=0"

                cursor1.execute(command1)
                cursor2.execute(command2)
                cursor3.execute(command3)
                cursor4.execute(command4)

                print('\n')
                equalto = '='*146
                print(equalto)
                print("  BOOK ID\t    BOOK NAME \t\t\t\t\t\t\t\t AUTHOR \t\t\t\t   GENRE")
                print(equalto)
                for i in cursor1:
                    for j in cursor2:
                        for k in cursor3:
                            for l in cursor4:
                                l = ''.join(l)
                                break
                            k = ''.join(k)
                            if len(k)<65:
                                difference = 45-len(k)
                                space = difference*' '
                                k = k+space 
                            break
                        j = ''.join(j)
                        if len(j)<65:
                            difference = 65-len(j)
                            space = difference*' '
                            j = j+space 
                        break
                    i = i[0]
                    i = str(i)
                    i = i + '            '
                    print('   ',i,j,k,l)
                print(equalto)

                print("\n")

                self.choice = input("Do you wish to issue any book? [Y/N] : ")
                self.choice = self.choice.lower()

                if self.choice == 'y':
                    Issue.issueBook(self)
                elif self.choice == 'n':
                    Student.bookOption(self)
                else:
                    print("=================")
                    print("| INVALID INPUT |")
                    print("=================")
                    time.sleep(1)
                    Books.selectGenre(self)

        if check == False:
            print('\n============================')
            print("    NO SUCH GENRE EXISTS")
            print('============================')
            time.sleep(2)
            Books.showGenre(self)
    
    def updateBookName(self): # Used by admin to change a book's name
        check = False
        print("\n")
        print("=================================")
        print('        UPDATE BOOK NAME         ')
        print("=================================")
        self.book_id = input("Enter Book ID: ")

        command1 = "SELECT book_id FROM books" # Collecting book ids from the database
        cursor1.execute(command1)

        for i in cursor1: # Checks if user entered book id exists in the database or not
            i = i[0]
            i = str(i)
            if i == self.book_id: # If book id exists the program lets the user to continue
                check = True
                break
        
        if check == False: # If book id does not exist in database it prints the message and redirects back to the start
            print('\n')
            print("==========================")
            print("  BOOK ID DOES NOT EXIST  ")
            print("==========================")
            time.sleep(1)
            Books.updateBookName(self)

        self.book_name = input("Enter New Book Name: ")
        command = "SELECT book_name FROM books WHERE book_id="+self.book_id
        cursor1.execute(command)
        for i in cursor1:
            i = ''.join(i)
        ask = "ARE YOU SURE YOU WANT TO CHANGE THE BOOK NAME FROM '"+i+"' TO '"+self.book_name+"'? [Y/N] :"
        inp = input(ask)
        inp = inp.lower()
        if inp == 'y':
            command2 = "UPDATE books SET book_name ="+"'"+self.book_name+"'"+"WHERE book_id ="+"'"+self.book_id+"'"
            cursor2.execute(command2)
            db.commit()
            print('\n')
            print("==================================")
            print("| BOOK NAME SUCCESSFULLY CHANGED |")
            print("==================================")
            Admin.bookOption(self)
        elif inp == 'n':
            Admin.bookOption(self)
        else:
            print('\n')
            print("===================")
            print("|  INVALID INPUT  |")
            print("===================")
            Books.updateBookName(self)
            

    def updateBookAuthor(self): # Used by admin to change a book's author
        check = False
        print("\n")
        print("=================================")
        print('      UPDATE BOOK AUTHOR         ')
        print("=================================")
        self.book_id = input("Enter Book ID: ")

        command1 = "SELECT book_id FROM books" # Collecting book ids from the database
        cursor1.execute(command1)

        for i in cursor1: # Checks if user entered book id exists in the database or not
            i = i[0]
            i = str(i)
            if i == self.book_id: # If book id exists the program lets the user to continue
                check = True
                break
        
        if check == False: # If book id does not exist in database it prints the message and redirects back to the start
            print('\n')
            print("==========================")
            print("  BOOK ID DOES NOT EXIST  ")
            print("==========================")
            time.sleep(1)
            Books.updateBookAuthor(self)

        self.book_author = input("Enter New Book Author: ")
        command = "SELECT author FROM books WHERE book_id="+self.book_id
        cursor1.execute(command)
        for i in cursor1:
            i = ''.join(i)
        ask = "ARE YOU SURE YOU WANT TO CHANGE THE BOOK AUTHOR FROM '"+i+"' TO '"+self.book_author+"'? [Y/N] :"
        inp = input(ask)
        inp = inp.lower()
        if inp == 'y':
            command2 = "UPDATE books SET author ="+"'"+self.book_author+"'"+"WHERE book_id ="+"'"+self.book_id+"'"
            cursor2.execute(command2)
            db.commit()
            print('\n')
            print("====================================")
            print("| BOOK AUTHOR SUCCESSFULLY CHANGED |")
            print("====================================")
            Admin.bookOption(self)
        elif inp == 'n':
            Admin.bookOption(self)
        else:
            print('\n')
            print("===================")
            print("|  INVALID INPUT  |")
            print("===================")
            Books.updateBookAuthor(self)

    def updateBookQuantity(self): #Used by admin to change a book's quantity
        check = False
        print("\n")
        print("=====================================")
        print('        UPDATE BOOK QUANTITY         ')
        print("=====================================")
        self.book_id = input("Enter Book ID: ")

        command1 = "SELECT book_id FROM books" # Collecting book ids from the database
        cursor1.execute(command1)

        for i in cursor1: # Checks if user entered book id exists in the database or not
            i = i[0]
            i = str(i)
            if i == self.book_id: # If book id exists the program lets the user to continue
                check = True
                break
        
        if check == False: # If book id does not exist in database it prints the message and redirects back to the start
            print('\n')
            print("==========================")
            print("  BOOK ID DOES NOT EXIST  ")
            print("==========================")
            time.sleep(1)
            Books.updateBookQuantity(self)

        self.quantity = input("Enter New Book Quantity: ")
        
        command2 = "UPDATE books SET quantity ="+"'"+self.quantity+"'"+"WHERE book_id ="+"'"+self.book_id+"'"
        cursor2.execute(command2)
        db.commit()
        print('\n')
        print("======================================")
        print("| BOOK QUANTITY SUCCESSFULLY CHANGED |")
        print("======================================")
        Admin.bookOption(self)

    def removeRow(self):
        check = False
        print("\n")
        print("===========================")
        print('        REMOVE ROW         ')
        print("===========================")
        self.book_id = input("Enter Book ID: ")

        command1 = "SELECT book_id FROM books" # Collecting book ids from the database
        cursor1.execute(command1)

        for i in cursor1: # Checks if user entered book id exists in the database or not
            i = i[0]
            i = str(i)
            if i == self.book_id: # If book id exists the program lets the user to continue
                check = True
                break
        
        if check == False: # If book id does not exist in database it prints the message and redirects back to the start
            print('\n')
            print("==========================")
            print("  BOOK ID DOES NOT EXIST  ")
            print("==========================")
            time.sleep(1)
            Books.removeRow(self)
        
        command1 = "SELECT book_name from books WHERE book_id ="+self.book_id
        command2 = "SELECT author from books WHERE book_id="+self.book_id
        cursor1.execute(command1)
        cursor2.execute(command2)

        for i in cursor1:
            book_name = ''.join(i)
        for j in cursor2:
            author = ''.join(j)
        
        print("\n")
        ask = "Are you sure you want to remove '"+book_name+"' by "+author+"? [Y/N]: "
        self.choice = input(ask)
        self.choice = self.choice.lower()

        if self.choice == 'y':
            command = "DELETE FROM books WHERE book_id="+self.book_id
            cursor1.execute(command)
            db.commit()
            print("=============================")
            print("| BOOK SUCCESSFULLY DELETED |")
            print("=============================")
            Admin.bookOption(self)
        elif self.choice == 'n':
            Admin.bookOption(self)
        else:
            print("=================")
            print("| INVALID INPUT |")
            print('=================')
            Books.removeRow(self)

        

        

class Issue(Books):
    

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.student_email = ''
        self.password = ''
        self.book_id = ''
        self.book_name = ''
        self.author = ''
        self.doi = ''              # Date of issue
        self.dor = ''              # Date of return
        self.grade = ''
        self.section = ''
        self.reviews = []
        self.review_book_name = ''
        self.come = False

    def checkIssuedBooks(self):
        
        command1 = "SELECT book_name FROM issue WHERE ad_no="+str(ad_no)
        command2 = "SELECT author FROM issue WHERE ad_no="+str(ad_no)
        command3 = "SELECT doi FROM issue WHERE ad_no="+str(ad_no)
        command4 = "SELECT dor FROM issue WHERE ad_no="+str(ad_no)
        command5 = "SELECT fine_issued FROM issue WHERE ad_no="+str(ad_no)

        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)

        print('\n')
        equalto = '='*185
        print(equalto)
        print("                BOOK NAME                                               AUTHOR                              DATE OF ISSUE                  DATE OF RETURN                 FINE ISSUED")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            m = ''.join(m)
                            m = '  '+m
                            break
                        l = ''.join(l)
                        l = l+(' '*20)
                        break
                    k = ''.join(k)
                    k = k+(' '*20)
                    break
                j = ''.join(j)
                if len(j)<40:
                    difference = 40 - len(j)
                    space = difference*' '
                    j = j+space
                break
            i = ''.join(i)
            if len(i)<65:
                difference = 65 - len(i)
                space = difference*' '
                i = i+space
            print('  ',i,j,k,l,m)
        print(equalto)
        Student.myProfileOption(self)
    
    def issueBook(self):
        check = False
        print("\n")
        print("===============================")
        print("|         ISSUE BOOK          |")
        print("===============================")
        print("|      ENTER 1 TO ISSUE       |")
        print("|      ENTER B TO GO BACK     |")
        print("|      ENTER E TO EXIT        |")
        print("===============================")

        self.choice = input("Enter choice: ")

        if self.choice == '1':
            print('\n')
            self.book_id = input("Enter Book ID Of The Book You Want To Issue: ")

            command = "SELECT book_id FROM books"
            cursor1.execute(command)
            for i in cursor1:
                i = i[0]
                i = str(i)
                if i == self.book_id:
                    check = True
                    break
            if check == False:
                print('\n')
                print("============================")
                print("|  BOOK ID DOES NOT EXIST  |")
                print("============================")
                Issue.issueBook(self)

            command3 = "SELECT book_id FROM issue WHERE ad_no="+str(ad_no)
            cursor3.execute(command3)

            check = False

            for i in cursor3:
                i = i[0]
                i = str(i)
                if i == self.book_id:
                    check = True
                    print("============================")
                    print("| SORRY, BUT IT SEEMS LIKE |")
                    print("| YOU HAVE ALREADY ISSUED  |")
                    print("|        THIS BOOK         |")
                    print("============================")
                    time.sleep(2)
                    Issue.issueBook(self)
            
            command1 = "SELECT book_name FROM books WHERE book_id="+self.book_id
            command2 = "SELECT author FROM books WHERE book_id="+self.book_id
            cursor1.execute(command1)
            cursor2.execute(command2)

            for i in cursor1:
                self.book_name = ''.join(i)
            for j in cursor2:
                self.author = ''.join(j)

            if check != True:
                print("\n")
                ask = "Are you sure you want to issue '"+self.book_name+"' by '"+self.author+"' ? [Y/N] : "
                self.choice = input(ask)
                self.choice = self.choice.lower()

                if self.choice == 'y':
                    command = "UPDATE books SET quantity = quantity-1 WHERE book_id="+self.book_id
                    cursor7.execute(command)
                    db.commit()
                    Issue.issueBill(self)
                elif self.choice == 'n':
                    Issue.issueBook(self)
                else:
                    print("\n")
                    print("======================")
                    print("|    INVALID INPUT   |")
                    print("======================")
                    time.sleep(1)
                    Issue.issueBook(self)
        
        elif self.choice == 'b':
            Student.studentChoice(self)

        elif self.choice == 'e':
            print('\n')
            print("===================")
            print("|    THANK YOU    |")
            print("===================")
            time.sleep(1)
            exit()
            
        
        else:
            print("\n")
            print("======================")
            print("|    INVALID INPUT   |")
            print("======================")
            time.sleep(1)
            Issue.issueBook(self)
        
    def issueBill(self): # Issues a bill containing the details of the book purchased for the student

        l = []
        

        first_name = 'SELECT first_name FROM student where admission_no='+ad_no
        last_name = 'SELECT last_name FROM student where admission_no='+ad_no
        email = 'SELECT email FROM student where admission_no='+ad_no
        grade = 'SELECT grade FROM student where admission_no='+ad_no
        section = 'SELECT section FROM student where admission_no='+ad_no
        cursor1.execute(first_name)
        cursor2.execute(last_name)
        cursor3.execute(email)
        cursor4.execute(grade)
        cursor5.execute(section) 
        
        
        for i in cursor1:
            self.first_name = ''.join(i)
            self.first_name = self.first_name.capitalize()
        for i in cursor2:
            self.last_name = ''.join(i)
            self.last_name = self.last_name.capitalize()
        for i in cursor3:       
            self.student_email = ''.join(i)          
        for i in cursor4:
            self.grade = ''.join(i)
        for i in cursor5:
            self.section = ''.join(i)
        
        self.doi = datetime.now()
        self.dor = self.doi + timedelta(10)
        self.doi = self.doi.strftime("%Y-%m-%d")
        self.dor = self.dor.strftime("%Y-%m-%d")
        book_name = ''
        
        if len(self.book_name)>=27:
            ctr = 0
            for i in self.book_name:
                if ctr>15 and i==' ':
                    space = 22*' '
                    book_name = book_name+'\n'+space
                    ctr = 0
                else:
                    book_name = book_name+i
                    ctr = ctr+1

        else:
            book_name = self.book_name

        print("\n")
        print("====================================================")
        print("                    ISSUE BILL")
        print("====================================================")
        print(" ADMISSION NUMBER :  ",ad_no)
        print(" FIRST NAME:         ",self.first_name)
        print(" LAST NAME:          ",self.last_name)
        print(" EMAIL:              ",self.student_email)
        print(" GRADE:              ",self.grade)
        print(" SECTION:            ",self.section)
        print(" BOOK NAME:          ",book_name)
        print(" BOOK AUTHOR:        ",self.author)
        print(" ISSUE DATE:         ",self.doi)
        print(" DUE DATE:           ",self.dor)
        print("====================================================")
        
        command3 = "SELECT s_no FROM issue ORDER BY s_no"
        cursor3.execute(command3)

        for i in cursor3:
            i = i[0]
            l.append(i)
        
        if len(l)!=0:
            final = l[-1]
            s_no = final+1
        elif len(l) == 0:
            s_no = 1



        command1 = "INSERT INTO issue VALUES("+ad_no+',"'+self.first_name+'","'+self.last_name+'","'+self.book_name+'","'+self.author+'","'
        command2 = self.doi+'","'+self.dor+'","'+'NO",'+str(s_no)+","+self.book_id+')'
        command = command1+command2
        
        cursor1.execute(command)
        db.commit()
        Student.studentChoice(self)

    def checkFine(self):
        command1 = "SELECT book_name FROM issue WHERE ad_no="+str(ad_no)+" AND fine_issued LIKE 'YES'"
        command2 = "SELECT author FROM issue WHERE ad_no="+str(ad_no)+" AND fine_issued LIKE 'YES'"
        command3 = "SELECT doi FROM issue WHERE ad_no="+str(ad_no)+" AND fine_issued LIKE 'YES'"
        command4 = "SELECT dor FROM issue WHERE ad_no="+str(ad_no)+" AND fine_issued LIKE 'YES'"
        command5 = "SELECT fine_issued FROM issue WHERE ad_no="+str(ad_no)+" AND fine_issued LIKE 'YES'"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)

        print('\n')
        equalto = '='*185
        print(equalto)
        print("\t\tBOOK NAME\t\t\t\t\t        AUTHOR\t\t\t\t    DATE OF ISSUE\t\t   DATE OF RETURN\t\t  FINE ISSUED")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            m = ''.join(m)
                            m = '  '+m
                            break
                        l = ''.join(l)
                        l = l+(' '*20)
                        break
                    k = ''.join(k)
                    k = k+(' '*20)
                    break
                j = ''.join(j)
                if len(j)<40:
                    difference = 40 - len(j)
                    space = difference*' '
                    j = j+space
                break
            i = ''.join(i)
            if len(i)<65:
                difference = 65 - len(i)
                space = difference*' '
                i = i+space
            print('  ',i,j,k,l,m)
        print(equalto)
        Student.myProfileOption(self)
    
    def issueFine(self): # This runs at the start of the program to ensure that the fines are properly issued
        curdate = datetime.now()
        curdate = curdate.strftime("%Y-%m-%d") # Current date's 
        cy = int(curdate[:4]) # Current date's year
        cm = int(curdate[5:7]) # Current date's month
        cd = int(curdate[8:]) # Current date's day

        d1 = date(cy,cm,cd)

        command1 = "SELECT dor FROM issue"
        command2 = "SELECT s_no FROM issue"

        cursor1.execute(command1) 
        cursor2.execute(command2)

        d = []
        s_no = []

        for i in cursor2:
            i = i[0]
            s_no.append(i)
            
        for j in cursor1:
            j = ''.join(j)
            d.append(j)

        new_date = []
        new_s_no = []



        for i in s_no:
            for j in d:
                x = j
                sy = int(j[:4])
                sm = int(j[5:7])
                sd = int(j[8:])
                d2 = date(sy,sm,sd)
                delta = d2-d1
                if delta.days<0:
                    new_date.append(x)
                    new_s_no.append(i)
                                
                del d[0]
                break
            

        for i in new_s_no:
            i = str(i)
            command = "UPDATE issue SET fine_issued = 'YES' WHERE s_no="+i
            cursor1.execute(command)
            db.commit()
        
        Start.start(self)
    
    def returnBook(self):
        print('\n')
        print("============================")
        print("|        RETURN BOOK       |")
        print("============================")
        print('\n')
        ad_no1 = input("Enter admission number: ")
        command1 = "SELECT book_name FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command2 = "SELECT author FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command3 = "SELECT doi FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command4 = "SELECT dor FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command5 = "SELECT fine_issued FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command6 = "SELECT book_id FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)
        

        print('\n')
        equalto = '='*200
        print(equalto)
        print(" BOOK ID\t\tBOOK NAME\t\t\t\t\t\t        AUTHOR\t\t\t\t     DATE OF ISSUE\t\t   DATE OF RETURN\t\t FINE ISSUED")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                n = n[0]
                                n = str(n)
                                if len(n)<3:
                                    difference = 15-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            m = '  '+m
                            break
                        l = ''.join(l)
                        l = l+(' '*20)
                        break
                    k = ''.join(k)
                    k = k+(' '*20)
                    break
                j = ''.join(j)
                if len(j)<40:
                    difference = 40 - len(j)
                    space = difference*' '
                    j = j+space
                break
            i = ''.join(i)
            if len(i)<65:
                difference = 65 - len(i)
                space = difference*' '
                i = i+space
            print('  ',n,i,j,k,l,m)
        print(equalto)
        
        self.choice = input("Enter book_id of the book you want to return: ")

        command = "SELECT book_id FROM issue WHERE ad_no="+ad_no1
        cursor1.execute(command)

        check = False

        for i in cursor1:
            i = i[0]
            i = str(i)
            if self.choice==i:
                command = "UPDATE books SET quantity = quantity+1 WHERE book_id="+self.choice
                cursor2.execute(command)
                db.commit()
                check = True
                break
        
        if check==False:
            print("\n")
            print("===========================")
            print("|     INVALID BOOK ID     |")
            print("===========================")
            Admin.issueOption(self)
        
        command = "DELETE FROM issue WHERE book_id="+self.choice
        cursor1.execute(command)
        db.commit()
    
        if check == True:    
            print("\n")
            print("===============================")
            print("| BOOK SUCCEESSFULLY RETURNED |")
            print("===============================")
        
        Admin.issueOption(self)

    def checkIssuedBook(self):
        
        print('\n')
        ad_no1 = input("Enter admission number: ")

        
        
        command1 = "SELECT book_name FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command2 = "SELECT author FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command3 = "SELECT doi FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command4 = "SELECT dor FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command5 = "SELECT fine_issued FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        command6 = "SELECT book_id FROM issue WHERE ad_no="+ad_no1+" ORDER BY book_id"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)
        

        print('\n')
        equalto = '='*200
        print(equalto)
        print(" BOOK ID\t\tBOOK NAME\t\t\t\t\t\t        AUTHOR\t\t\t\t     DATE OF ISSUE\t\t   DATE OF RETURN\t\t FINE ISSUED")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                n = n[0]
                                n = str(n)
                                if len(n)<3:
                                    difference = 15-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            m = '  '+m
                            break
                        l = ''.join(l)
                        l = l+(' '*20)
                        break
                    k = ''.join(k)
                    k = k+(' '*20)
                    break
                j = ''.join(j)
                if len(j)<40:
                    difference = 40 - len(j)
                    space = difference*' '
                    j = j+space
                break
            i = ''.join(i)
            if len(i)<65:
                difference = 65 - len(i)
                space = difference*' '
                i = i+space
            print('  ',n,i,j,k,l,m)
        print(equalto)
        time.sleep(1)
        Admin.issueOption(self)

    def readOverviews(self):
        print("\n")
        print("=======================================")
        print("|            READ OVERVIEW            |")
        print("=======================================")
        print('\n')
        
        self.choice = input("Enter Book ID: ")
        
        command = "SELECT book_id FROM books"
        cursor1.execute(command)

        check = False

        for i in cursor1:
            i = i[0]
            i = str(i)
            if i == self.choice:
                check = True
                break
        
        if check == False:
            print("==========================")
            print("| BOOK ID DOES NOT EXIST |")
            print("==========================")
            Issue.readOverviews(self)

        command1 = "SELECT book_name FROM books WHERE book_id="+self.choice
        cursor1.execute(command1)

        for i in cursor1:
            i = ''.join(i)
            f_name = "Overviews/"+i+'.txt'
            try:
                f = open(f_name,'r')
                overview = f.read()
            except:
                print("\n")
                print("=====================================================================================")
                print("|        THE FILE FOR THE OVERVIEWS HAS NOT BEEN CREATED FOR THIS BOOK YET          |")
                print("=====================================================================================")
                time.sleep(2)
                Student.bookOption(self)
            else:
                print("\n")
                print(overview)
                Issue.ask(self)

    def ask(self):
        print('\n')
        print("==========================================")
        print("|   ENTER D WHEN YOU ARE DONE READING    |")
        print("==========================================")
        self.choice = input()
        self.choice = self.choice.lower()

        if self.choice == 'd':
            Student.bookOption(self)
        else:
            print("=====================")
            print("|   INVALID INPUT   |")
            print("=====================")
            time.sleep(1)
            Issue.ask(self)

    def checkFineAdmin(self): # Allows admin to check if fines are paid or not
        command1 = "SELECT book_name FROM issue"
        command2 = "SELECT author FROM issue"
        command3 = "SELECT doi FROM issue"
        command4 = "SELECT dor FROM issue"
        command5 = "SELECT fine_issued FROM issue"
        command6 = "SELECT ad_no FROM issue"
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)

        print('\n')
        equalto = '='*197
        print(equalto)
        print("  AD NO\t      BOOK NAME\t\t\t\t\t\t\t          AUTHOR\t\t\t       DATE OF ISSUE\t\t      DATE OF RETURN\t\t     FINE ISSUED")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                n = n[0]
                                n = str(n)
                                if len(n)<6:
                                    difference = 10-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            m = '  '+m
                            break
                        l = ''.join(l)
                        l = l+(' '*20)
                        break
                    k = ''.join(k)
                    k = k+(' '*20)
                    break
                j = ''.join(j)
                if len(j)<40:
                    difference = 40 - len(j)
                    space = difference*' '
                    j = j+space
                break
            i = ''.join(i)
            if len(i)<65:
                difference = 65 - len(i)
                space = difference*' '
                i = i+space
            print('  ',n,i,j,k,l,m)
        print(equalto)
        time.sleep(1)
        Admin.issueOption(self)


       
class Admin:

    def __init__(self):
        self.admin_choice = ''
        self.choice = ''
        self.grade = ''
        self.section = ''

    def adminChoice(self): # Lets admin choose what option he likes
        print('\n')
        print('============================================')
        print('|              ADMIN OPTIONS               |')
        print('============================================')
        print('|   ENTER 1 FOR CHECKING BOOKS OPTION      |')
        print('|   ENTER 2 FOR CHECKING STUDENT OPTIONS   |')
        print('|   ENTER 3 FOR CHECKING ISSUE OPTIONS     |')
        print('|   ENTER E TO EXIT                        |')
        print('============================================')
        print('\n')

        self.admin_choice = input("Enter choice: ")
        self.admin_choice = self.admin_choice.lower()

        if self.admin_choice == '1':
            Admin.bookOption(self)
        elif self.admin_choice == '2':
            Admin.studentOption(self)
        elif self.admin_choice == '3':
            Admin.issueOption(self)
        elif self.admin_choice == 'e':
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else:
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Admin.adminChoice(self)


    def bookOption(self): # Lets admin choose what option he likes under the BOOKS category
        print('\n')
        print('====================================================')
        print("|                   BOOKS CATEGORY                 |")
        print('====================================================')   
        print("|      ENTER 1 TO SEE BOOKS                        |")
        print("|      ENTER 2 TO ADD BOOKS                        |")
        print("|      ENTER 3 TO CHANGE BOOK NAME                 |")
        print("|      ENTER 4 TO CHANGE BOOK AUTHOR               |")
        print("|      ENTER 5 TO CHANGE BOOK QUANTITY             |")
        print("|      ENTER 6 TO REMOVE A ROW                     |")
        print("|      ENTER 7 TO WRITE OVERVIEWS                  |")
        print("|      ENTER 8 TO CHECK FOR MISSING OVERVIEWS      |")
        print("|      ENTER B TO GO BACK                          |")
        print("|      ENTER E TO EXIT                             |")
        print("====================================================")
        print('\n')

        self.admin_choice = input("Enter choice: ")
        self.admin_choice = self.admin_choice.lower()

        if self.admin_choice == '1':
            Books.showBooksAdmin(self)
        elif self.admin_choice == '2':
            Books.addBooks(self)
        elif self.admin_choice == '3':
            Books.updateBookName(self)
        elif self.admin_choice == 'b':
            Admin.adminChoice(self)
        elif self.admin_choice == '4':
            Books.updateBookAuthor(self)
        elif self.admin_choice == '5':
            Books.updateBookQuantity(self)
        elif self.admin_choice == '6':
            Books.removeRow(self)
        elif self.admin_choice == '7':
            Books.writeOverviews(self)
        elif self.admin_choice == '8':
            Books.getMissingOverviews(self)    
        elif self.admin_choice == 'e':
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else:
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Admin.bookOption(self)

    def issueOption(self):
        print("\n")
        print("==========================================================")
        print("|                     ISSUE CATEGORY                     |")
        print("==========================================================")
        print("|       ENTER 1 FOR 'RETURN BOOK'                        |")
        print("|       ENTER 2 TO CHECK STUDENTS FINES                  |")
        print("|       ENTER 3 TO GET INDIVIDUAL STUDENT ISSUE DETAIL   |")
        print("|       ENTER B TO GO BACK                               |")
        print("|       ENTER E TO EXIT                                  |")
        print("==========================================================")

        self.admin_choice = input("Enter choice: ")
        self.admin_choice = self.admin_choice.lower()

        if self.admin_choice == '1':
            Issue.returnBook(self)
        elif self.admin_choice == '2':
            Issue.checkFineAdmin(self)
        elif self.admin_choice == '3':
            Issue.checkIssuedBook(self)
        elif self.admin_choice == 'b':
            Admin.adminChoice(self)
        elif self.admin_choice == 'e':
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else:
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Admin.issueOption(self)

    def studentOption(self):
        print('\n')
        print('==========================================')
        print('|            STUDENT CATEGORY            |')
        print("==========================================")
        print("|   ENTER 1 TO SEE LIST OF STUDENTS      |")
        print("|   ENTER 2 TO SEARCH FOR STUDENTS       |")
        print("|   ENTER 3 TO SEARCH FOR A GRADE        |")
        print("|   ENTER B TO GO BACK                   |")
        print("|   ENTER E TO EXIT                      |")
        print('==========================================')

        self.admin_choice = input("Enter choice: ")
        self.admin_choice = self.admin_choice.lower()

        if self.admin_choice == '1':
            Admin.showStudents(self)
        elif self.admin_choice == 'b':
            Admin.adminChoice(self)
        elif self.admin_choice == '2':
            Admin.searchStudent(self)
        elif self.admin_choice == '3':
            Admin.searchGrade(self)
        elif self.admin_choice == 'e':
            print("\n")
            print("===========================")
            print("|       THANK YOU         |")
            print("===========================")
            time.sleep(1)
            exit()
        else:
            print('\n')
            print('===================')
            print('|  INVALID INPUT  |')
            print("===================")
            time.sleep(1)
            Admin.studentOption(self)

    def searchGrade(self):

        check = False

        print("\n")
        print("========================")
        print("|     SEARCH GRADE     |")
        print("========================")

        self.grade = input("Enter Grade: ")

        command = "SELECT grade FROM student"
        cursor1.execute(command)

        for i in cursor1:
            i = ''.join(i)
            if i == self.grade:
                check = True
                break
        
        if check == False:
            print("=====================")
            print("|   INVALID GRADE   |")
            print("=====================")
            Admin.searchGrade(self)

        check = False

        self.section = input("Enter section [IF YOU WANT TO SEE EVERY SECTION, TYPE 1]:")
        self.section = self.section.upper()
        command = "SELECT DISTINCT section FROM student"
        cursor1.execute(command)

        for i in cursor1:
            i = ''.join(i)
            if i == self.section:
                check = True
                break
        
        if self.section == '1':
            command1 = "SELECT admission_no FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command2 = "SELECT first_name FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command3 = "SELECT last_name FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command4 = "SELECT grade FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command5 = "SELECT section FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command6 = "SELECT email FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            command7 = "SELECT password FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" ORDER BY first_name"
            check = True

        if check == False:
            print("=================================")
            print("|  THIS SECTION DOES NOT EXIST  |")
            print("=================================")
            Admin.searchGrade(self)

        elif self.section != '1':
            command1 = "SELECT admission_no FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command2 = "SELECT first_name FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command3 = "SELECT last_name FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command4 = "SELECT grade FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command5 = "SELECT section FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command6 = "SELECT email FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"
            command7 = "SELECT password FROM student WHERE grade LIKE "+"'"+self.grade+"'"+" AND SECTION LIKE "+"'"+self.section+"'"+" ORDER BY first_name"

        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)
        cursor7.execute(command7)

        print('\n')
        equalto = "="*204
        print(equalto)
        print("  ROLL NO\t\t FIRST NAME\t\t\t LAST NAME\t\t       GRADE\t\t\t   SECTION\t\t\tEMAIL\t\t\t\t\t     PASSWORD")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                for o in cursor7:
                                    o = ''.join(o) 
                                    break
                                n = ''.join(n)
                                if len(n)<40:
                                    difference = 50-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            if len(m)<3:
                                difference = 20-len(m)
                                space = difference*' '
                                m = (space)+m+(space)
                            break
                        l = ''.join(l)
                        if len(l)<5:
                            difference = 10-len(l)
                            space = difference*' '
                            l = l+space
                        break
                    k = ''.join(k)
                    if len(k)<=20:
                        difference = 30-len(k)
                        space = difference*' '
                        k = k+space
                    break
                j = ''.join(j)
                if len(j)<=20:
                    difference = 30-len(j)
                    space = difference*' '
                    j = j+space
                break
            i = i[0]
            i = str(i)
            if len(i)<6:
                difference = 20-len(i)
                space = difference*' '
                i = i+space
            print('    ',i,j,k,l,m,n,o)

        print(equalto)
        time.sleep(1)

        Admin.studentOption(self)

    def showStudents(self): # Allows admins to see students of the library
        command1 = "SELECT admission_no FROM student"
        command2 = "SELECT first_name FROM student"
        command3 = "SELECT last_name FROM student"
        command4 = "SELECT grade FROM student"
        command5 = "SELECT section FROM student"
        command6 = "SELECT email FROM student"
        command7 = "SELECT password FROM student"

        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)
        cursor7.execute(command7)

        print('\n')
        equalto = "="*204
        print(equalto)
        print("  ROLL NO\t\t FIRST NAME\t\t\t LAST NAME\t\t       GRADE\t\t\t   SECTION\t\t\tEMAIL\t\t\t\t\t     PASSWORD")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                for o in cursor7:
                                    o = ''.join(o) 
                                    break
                                n = ''.join(n)
                                if len(n)<40:
                                    difference = 50-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            if len(m)<3:
                                difference = 20-len(m)
                                space = difference*' '
                                m = (space)+m+(space)
                            break
                        l = ''.join(l)
                        if len(l)<5:
                            difference = 10-len(l)
                            space = difference*' '
                            l = l+space
                        break
                    k = ''.join(k)
                    if len(k)<=20:
                        difference = 30-len(k)
                        space = difference*' '
                        k = k+space
                    break
                j = ''.join(j)
                if len(j)<=20:
                    difference = 30-len(j)
                    space = difference*' '
                    j = j+space
                break
            i = i[0]
            i = str(i)
            if len(i)<6:
                difference = 20-len(i)
                space = difference*' '
                i = i+space
            print('    ',i,j,k,l,m,n,o)

        print(equalto)
        time.sleep(1)

        Admin.studentOption(self)
    
    def searchStudent(self): # Aloows admin to search for a student
        
        print('\n')
        print("=================================")
        print("|        SEARCH STUDENT         |")
        print("=================================")

        self.choice = input("Enter Student Name")

        command1 = "SELECT admission_no FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command2 = "SELECT first_name FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command3 = "SELECT last_name FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command4 = "SELECT grade FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command5 = "SELECT section FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command6 = "SELECT email FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"
        command7 = "SELECT password FROM student WHERE first_name LIKE "+"'%"+self.choice+"%'"+" ORDER BY first_name"

        
        cursor1.execute(command1)
        cursor2.execute(command2)
        cursor3.execute(command3)
        cursor4.execute(command4)
        cursor5.execute(command5)
        cursor6.execute(command6)
        cursor7.execute(command7)

        print('\n')
        equalto = "="*204
        print(equalto)
        print("  ROLL NO\t\t FIRST NAME\t\t\t LAST NAME\t\t       GRADE\t\t\t   SECTION\t\t\tEMAIL\t\t\t\t\t     PASSWORD")
        print(equalto)
        for i in cursor1:
            for j in cursor2:
                for k in cursor3:
                    for l in cursor4:
                        for m in cursor5:
                            for n in cursor6:
                                for o in cursor7:
                                    o = ''.join(o) 
                                    break
                                n = ''.join(n)
                                if len(n)<40:
                                    difference = 50-len(n)
                                    space = difference*' '
                                    n = n+space
                                break
                            m = ''.join(m)
                            if len(m)<3:
                                difference = 20-len(m)
                                space = difference*' '
                                m = (space)+m+(space)
                            break
                        l = ''.join(l)
                        if len(l)<5:
                            difference = 10-len(l)
                            space = difference*' '
                            l = l+space
                        break
                    k = ''.join(k)
                    if len(k)<=20:
                        difference = 30-len(k)
                        space = difference*' '
                        k = k+space
                    break
                j = ''.join(j)
                if len(j)<=20:
                    difference = 30-len(j)
                    space = difference*' '
                    j = j+space
                break
            i = i[0]
            i = str(i)
            if len(i)<6:
                difference = 20-len(i)
                space = difference*' '
                i = i+space
            print('    ',i,j,k,l,m,n,o)

        print(equalto)
        time.sleep(1)

        Admin.studentOption(self)

class Start:

    def __init__(self):
        self.choice = ''
        self.username = ''
        self.password = ''
        self.come = True

    def start(self): # Welcome 

        if self.come == False:
            print("   ==============================================")
            print("   |                 WELCOME TO                 |")
            print("   |       SCHOOL LIBRARY MANAGEMENT SYSTEM     |")
            print("   ==============================================")
            print("   |            BY : VIGNESH VENKATESH          |")
            print("   |                CLASS : XII B               |")
            print("   ==============================================")
            print('\n')

        self.come = True
        
        print('\n')
        print("==========================")
        print("|   ENTER 1 FOR ADMIN    |")
        print("|   ENTER 2 FOR STUDENT  |")
        print("|   ENTER E TO EXIT      |")
        print("==========================")
        print('\n')
        self.choice = input("Enter choice: ")
        self.choice = self.choice.lower()

        if self.choice == '1':
            print('\n')
            self.username = input("Enter Admin Username: ")
            self.password = input("Enter Admin Password: ")

            if self.username == 'vignesh' and self.password == '123456':
                Admin.adminChoice(self)
            else: 
                print('\n')
                print("=================================")
                print("|        INVALID INPUT          |")
                print("|          TRY AGAIN            |")
                print("=================================")
                global ctr
                ctr = ctr+1
                if ctr==5: # Checks if the user has inputted the wrong password for 5 times
                    print('\n')
                    print("======================================")
                    print("|       MAXIMUM TRIES REACHED        |")
                    print("|       PLEASE TRY AGAIN LATER       |")
                    print("======================================")
                    
                    time.sleep(3) # Closes the program after 3 seconds

                Start.start(self)
        
        elif self.choice == '2':
            Getdata.getInfo(self)
        
        elif self.choice == 'e':
            print("============================")
            print("|        THANK YOU         |")
            print("============================")
            time.sleep(1)
            exit()
        
        else:
            print('\n')
            print("===============================")
            print("|       INVALID INPUT         |")
            print("|         TRY AGAIN           |")
            print("===============================")
            Start.start(self)


i = Issue()
i.issueFine()
