# #
# # class Node:
# #    def __init__(self, data):
# #       self.data = data
# #       self.children = []
# #       self.parent = None
# #    def add_child(self,child):
# #        child.parent = self
# #        self.children.append(child)
# #    def print_tree(self):
# #        print(self.data)
# #        for child in self.children:
# #            child.print_tree()
# #
# # def build_book_tree():
# #     root=Node(" DSA Book")
# #
# #     chapter1=Node("chapter1")
# #     chapter1.add_child(Node("Hashing"))
# #
# #     chapter2 = Node("chapter2")
# #     chapter2.add_child(Node("Trees"))
# #
# #     chapter3 = Node("chapter3")
# #     chapter3.add_child(Node("Graphs"))
# #
# #
# #     root.add_child(chapter1)
# #     root.add_child(chapter2)
# #     root.add_child(chapter3)
# #
# #     return root
# #
# # if __name__=='__main__':
# #     root=build_book_tree()
# #     root.print_tree()
# #     pass
# #
#
#
#
#
# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.children = []
#       self.parent = None
#
#    def add_child(self,child):
#        child.parent = self
#        self.children.append(child)
#
#    def print_tree(self):
#        print(self.data)
#        for child in self.children:
#            child.print_tree()
#
# def build_book_tree():
#     root=Node(input("Enter the root node: "))
#
#     chapter1=Node(input("Enter the child of the root node: "))
#     chapter1.add_child(Node(input("Enter the child node: ")))
#     child1=Node("linear probing")
#     child1.add_child(Node(chapter1))
#
#     chapter2 = Node(input("Enter the child of the root node: "))
#     chapter2.add_child(Node((input("Enter the child node: "))))
#     child2= Node("Binary Tree")
#     child2.add_child(Node(chapter2))
#     #
#     # chapter3 = Node(input("Enter the child of the root node: "))
#     # chapter3.add_child(Node((input("Enter the child node: "))))
#     # child3 = Node("Prims algorithm")
#     # child3.add_child(chapter3)
#
#     root.add_child(chapter1)
#     root.add_child(chapter2)
#     # root.add_child(chapter3)
#     # root.add_child(child1)
#     # root.add_child(child2)
#     # root.add_child(child3)
#     chapter1.add_child(child1)
#     chapter2.add_child(child2)
#     # chapter3.add_child(child3)
#
#     return root
#
# if __name__=='__main__':
#     root=build_book_tree()
#     root.print_tree()
#     pass

# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.children = []
#       self.parent = None
#
#    def add_child(self,child):
#        # child.parent = self
#        self.children.append(child)
#
#    def print_tree(self):
#        print(self.data)
#        for child in self.children:
#            child.print_tree()
#
# def build_book_tree():
#     root=Node(" DSA Book")
#
#     chapter1=Node("1. chapter1")
#     chapter1.add_child(Node(" 1.1 Hashing"))
#     # ch.add_child(chapter1("tree"))
#
#
#     chapter2 = Node("2.chapter2")
#     chapter2.add_child(Node(" 2.1 Trees"))
#
#     chapter3 = Node("3.chapter3")
#     chapter3.add_child(Node(" 3.1Graphs"))
#
#
#     root.add_child(chapter1)
#     root.add_child(chapter2)
#     root.add_child(chapter3)
#
#     return root
#
# if __name__=='__main__':
#     root=build_book_tree()
#     root.print_tree()
#     pass

#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
#
#     def printTree(self):
#         print(self.data)
#         for child in self.children:
#             child.printTree()
#
# def book_Tree():
#     root =Node("DSA")
#
#     ch1 = Node("1.Hashing ")
#     ch1.add_child(Node("  1.1 Hash Table"))
#     ch1.add_child(Node("  1.2 Type of hashing"))
#
#     ch2 = Node("2.Tree")
#     ch2.add_child(Node("  2.1 Tree terminology"))
#     ch2.add_child(Node("  2.1 Tree terminology"))
#
#     ch3 = Node("3.Hashing ")
#     ch3.add_child(Node("  3.1 Hash Table"))
#     ch3.add_child(Node("  3.2 Type of hashing"))
#
#     root.add_child(ch1)
#     root.add_child(ch2)
#     root.add_child(ch3)
#
#     return root
#
# if __name__ == '__main__':
#     Groot = book_Tree()
#     Groot.printTree()
#     pass

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addchild(self,child):
        self.children.append(child)

    def printTree(self):
        print(self.data)
        for child in self.children:
            child.printTree()

def Book_tree():
    root = Node("DSA")

    ch1 = Node("1.Hashing")
    ch1.addchild(Node("  1.1 Hash table"))
    ch1.addchild(Node("  1.2 Collision"))

    ch2 = Node("2.Graph")
    ch2.addchild(Node("  2.1 Directed Graph"))
    ch2.addchild(Node("  2.2 Undirected Graph"))

    ch3 = Node("3.Tree")
    ch3.addchild(Node("  3.1 Root"))
    ch3.addchild(Node("  3.2 Child/Sibling"))

    root.addchild(ch1)
    root.addchild(ch2)
    root.addchild(ch3)

    return root

if __name__=="__main__":
    Groot = Book_tree()
    Groot.printTree()