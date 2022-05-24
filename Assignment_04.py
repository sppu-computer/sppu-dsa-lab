
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert method to create nodes
    def insert(self, data):
        # if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # else:
        #     self.data = data

    def Inorder(self):
        if self.left:
            self.left.Inoder()

        print(self.data,end="")

        if self.right:
            self.right.Inoder()

    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
          if self.right is None:
             return str(lkpval) + " Not Found"
          return self.right.findval(lkpval)
        else:
           return str(lkpval) + " is Found"



root = Node(20)
root.insert(11)
root.insert(7)
root.insert(36)
root.insert(4)
root.insert(63)
root.insert(8)
root.insert(23)
root.insert(10)

root.Inorder()

#
# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y - 20)
#             t.write(node.data, align='center', font=('Arial', 12, 'normal'))
#             draw(node.left, x - dx, y - 60, dx / 2)
#             jumpto(x, y - 20)
#             draw(node.right, x + dx, y - 60, dx / 2)
#
#     import turtle
#     t = turtle.Turtle()
#     t.speed(0);
#     turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30 * h)
#     draw(root, 0, 30 * h, 40 * h)
#     t.hideturtle()
#     turtle.mainloop()
#
# r = int(input("Enter the value of the root node: "))
# x = int(input("Enter how many nodes you want to insert: "))
# root = Node(r)
# for i in range(0,x):
#     data=int(input("Enter the data: "))
#     root.insert(data)
#
# # root.insert(7)
# # root.insert(14)
# # root.insert(3)
# # root.insert(5)
# # print(root.findval(7))
# # print(root.findval(14))
# drawtree(root)
