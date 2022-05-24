# # Python program to demonstrate
# # Read record in a file
# # Open function to open the file "myfile.txt"
# # it's reference in the variable file1
# file1 = open("myfile.txt")
# # Reading from file
# print(file1.read())
# # Closing file
# file1.close()
#
# # Python program to demonstrate
# # insert record in a file
# # Open function to open the file "myfile.txt"
# # (same directory) in append mode and store
# # it's reference in the variable file1
# file1 = open("myfile.txt", "a")
# # Writing to file
# file1.write("\nWriting to file :)")
# # Closing file
# file1.close()
#
#
# # code to delete a particular
# # data from a file
# # open file in read mode
# with open("myfile.txt", "r") as f:
# # read data line by line
#     data = f.readlines()
# # open file in write mode
#
# with open("myfile.txt", "w") as f:
#     for line in data :
#     # condition for data to be deleted
#         if line.strip("\n") != "Age : 20" :
#             f.write(line)


# file = open("file1.txt")
# # print(file.read())
# file.close()
#
# file = open("file1.txt","a")
# file.write("Hello have a good day")
# file.close()
#
# with open("file1.txt","r") as f:
#     data = f.readlines()
#     print(data)
#
# with open("file1.txt","w") as f:
#     for line in data:
#         if line.strip("\n") != "Age: 20":
#             f.write(line)


# file  = open("file2.txt")
# file.close()
#
# file = open("file2.txt","a")
# file.write("Hello ...... "
#            "have a good day ....!")
# file.close()
#
# with open("file2.txt","r") as f:
#     data  = f.readlines()
#
# with open("file2.txt","w") as f:
#     for line in data:
#         if line.strip("\n") != "Age : 20":
#             f.write(line)


file  = open("f2.txt")
file.close()

file  = open("f2.txt","a")
file.write("Hello have good day")
file.close()

with open("f2.txt","r")as f:
    data = f.readlines()

with open("f2.txt","w")as f:
    for line in data:
        if line.strip("\n") != "Age:20":
            f.write(line)