
class newNode:
    def __init__(self, key):
        self.left = self.right = None
        self.key = key
        self.isThreaded = None

    def InsertData(self,data):
        if data < self.key:
            if self.left is None:
                self.left = newNode(data)
            else:
                self.left.InsertData(data)

        else:
            if self.right is None:
                self.right = newNode(data)

            else:
                self.right.InsertData(data)

# Converts tree with given root to threaded
# binary tree.
# This function returns rightmost child of
# root.
def createThreaded(root):
    # Base cases : Tree is empty or has
    #               single node
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root

    # Find predecessor if it exists
    if root.left != None:
        # Find predecessor of root (Rightmost
        # child in left subtree)
        l = createThreaded(root.left)

        # Link a thread from predecessor
        # to root.
        l.right = root
        l.isThreaded = True

    # If current node is rightmost child
    if root.right == None:
        return root

    # Recur for right subtree.
    return createThreaded(root.right)


# A utility function to find leftmost node
# in a binary tree rooted with 'root'.
# This function is used in inOrder()
def leftMost(root):
    while root != None and root.left != None:
        root = root.left
    return root


# Function to do inorder traversal of a
# threaded binary tree
def inOrder(root):
    if root == None:
        return

    # Find the leftmost node in Binary Tree
    cur = leftMost(root)

    while cur != None:
        print(cur.key, end=" ")

        # If this Node is a thread Node, then
        # go to inorder successor
        if cur.isThreaded:
            cur = cur.right

        else:  # Else go to the leftmost child
            # in right subtree
            cur = leftMost(cur.right)


# Driver Code
if __name__ == '__main__':

    root = newNode(int(input("Enter the value for Root Node: ")))
    x = int(input("Enter the number of nodes which you want to insert: "))
    for i in range(0,x):
        root.InsertData(int(input("Enter the data: ")))
    # root.left = newNode(int(input("Enter the value of Node: ")))
    # root.right = newNode(int(input("Enter the value of Node: ")))
    # root.left.left = newNode(int(input("Enter the value of Node: ")))
    # root.left.right = newNode(int(input("Enter the value of Node: ")))
    # root.right.left = newNode(int(input("Enter the value of Node: ")))
    # root.right.right = newNode(int(input("Enter the value of Node: ")))

    createThreaded(root)

    print("Inorder traversal of created",
          "threaded tree is")
    inOrder(root)

