class hashTable:
    
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table : "))
     
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0

 
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    def hashFunction(self, element):
        return element % self.size

    def insert(self, element):
      
        if self.isFull():
            print("Hash Table Full")
            return False

            isStored = False

        position = self.hashFunction(element)

       
        if self.table[position] == 0:
            self.table[position] = element
            print("Element " + str(element) + " at position " + str(position))
            isStored = True
            self.elementCount += 1

       
        else:
            print("Collision has occured for element " + str(element) + " at position " + str(
                position) + " finding new Position.")
            while self.table[position] != 0:
                position += 1
                if position >= self.size:
                    position = 0

            self.table[position] = element
            isStored = True
            self.elementCount += 1
        return isStored

    def search(self, element):
        found = False

        position = self.hashFunction(element)
        self.comparisons += 1

        if (self.table[position] == element):
            return position
            isFound = True

    
        else:
            temp = position - 1
            
            while position < self.size:
                if self.table[position] != element:
                    position += 1
                    self.comparisons += 1
                else:
                    return position

           
            position = temp
            while position >= 0:
                if self.table[position] != element:
                    position -= 1
                    self.comparisons += 1
                else:
                    return position

        if not found:
            print("Element not found")
            return False

 
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
        return

  
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("The number of element is the Table are : " + str(self.elementCount))



table1 = hashTable()

table1.insert(12)
table1.insert(23)
table1.insert(11)
table1.insert(17)
table1.insert(99)
table1.insert(9)
table1.insert(78)
table1.insert(40)
table1.insert(7) 

table1.display()
print()

print("The position of element 31 is : " + str(table1.search(23)))
print("The position of element 28 is : " + str(table1.search(12)))
print("The position of element 90 is : " + str(table1.search(99)))
print("The position of element 77 is : " + str(table1.search(77)))
print("The position of element 1 is : " + str(table1.search(1)))
print("\nTotal number of comaprisons done for searching = " + str(table1.comparisons))
print()

table1.remove(99)
table1.remove(12)

table1.display()


#
# class hashTable:
#
#     def __init__(self):
#         self.size = int(input("Enter the size of the table: "))
#         self.table = list(0 for i in range(self.size))
#         self.elementCount = 0
#         self.comparison = 0
#
#     def isFull(self):
#         if self.elementCount == self.size:
#             return True
#         else:
#             return False
#
#     def hashFunction(self,element):
#         return element % self.size
#
#     def Insert(self, element):
#         # checking if the table is full
#         if self.isFull():
#             print("Hash Table Full")
#             return False
#
#             isStored = False
#
#         position = self.hashFunction(element)
#
#         # checking if the position is empty
#         if self.table[position] == 0:
#             self.table[position] = element
#             print("Element " + str(element) + " at position " + str(position))
#             isStored = True
#             self.elementCount += 1
#
#         # collision occured hence we do linear probing
#         else:
#             print("Collision has occured for element " + str(element) + " at position " + str(
#                 position) + " finding new Position.")
#             while self.table[position] != 0:
#                 position += 1
#                 if position >= self.size:
#                     position = 0
#
#             self.table[position] = element
#             isStored = True
#             self.elementCount += 1
#         return isStored
#
#
#
#     def display(self):
#         for i in range(self.size):
#             print(str(i)+" = "+str(self.table[i]))
#
#         print("The element count is ",self.elementCount)
#
#
#     def remove(self,element):
#         position = element % self.size
#         if position is not False:
#             self.table[position] = 0
#             self.elementCount -= 1
#
#         else:
#             print("Element is not found")
#
# obj = hashTable()
# obj.Insert(10)
# obj.Insert(23)
# obj.Insert(56)
# obj.Insert(47)
# obj.Insert(41)
# obj.Insert(3)
# obj.Insert(78)
# obj.Insert(11)
# obj.Insert(99)
#
# obj.display()
# obj.remove(47)
# obj.remove(2)
#
# obj.display()
