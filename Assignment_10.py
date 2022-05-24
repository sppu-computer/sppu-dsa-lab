import os
import pickle
import sys
dict = {}
def write_in_file():
    file=open("samplefile.dat","ab")
    #a-append,b-binary
    no=int(input("Enter Number of student"))
    for i in range(no):
     print("enter student details",i+1)
     dict["rollno"]=int(input("enter roll number: "))
     dict["name"]=input("enter name: ")
     dict["div"]=input("Enter Division: ")
     dict["Address"]=input("Enter address: ")
     pickle.dump(dict,file)
     #dump-To write in data file
    file.close()

def display():
     # read from file and display
     file = open("samplefile.dat", "rb")
     # r-read b-binary
     try:
         while True:
             stud = pickle.load(file)
     # write the file
             print(stud)
     except EOFError:
         pass
     file.close()


def search():

    file = open("samplefile.dat", "rb")
    r = int(input("Enter roll number of student to search"))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data["rollno"]==r:
                print("the roll no ",r,"record found")
                print(data)
                found=1
                break

    except EOFError:
        pass
        if found == 0:
            print("the roll no ", r, "record is not found")
        file.close()

def delete():
    file = open("samplefile.dat", "rb+")
    t = []
    r = int(input("Enter roll number of student to search"))
    try:
        while True:
            data = pickle.load(file)
            if data["rollno"] != r:
                t.append(data)
    except EOFError:
        print("completed deleting details")
    file.seek(0)
    file.truncate()
    for i in range(len(t)):
        pickle.dump(t[i], file)
    else:
        file.close()



while True:
    print("MENU\n 1-Write in a file \n 2-Display \n 3-search \n 4-delete \n 5-exit")
    ch=int(input("enter ur choice"))

    if ch==1:
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        delete()
    if ch==5:
       print("thank you")
       sys.exit()