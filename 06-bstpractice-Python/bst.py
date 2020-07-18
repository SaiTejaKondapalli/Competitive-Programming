class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        self.inserNode(self.root, new_val)

    def insertNode(self,node,new_val):
        if self.root is None:
            self.root.value = new_val
        else:
            if self.root.value < new_val:
                if self.root.right is None:
                    self.root.right = Node(new_val)
                else:
                    return BST.insertNode(self.root.right, new_val)
            else:
                if self.root.left is None:
                    self.root.left = Node(new_val)
                else:
                    return BST.insertNode(self.root.left, new_val)

    def printSelf(self):
        # Your code goes here
        if self.root:
            BST.printSelf(self.root.left)
            print(self.root.value)
            BST.printSelf(self.root.right)

    def search(self, find_val):
        # Your code goes here
        return BST.searchNode(self.root, find_val)

    def searchNode(self,node,find_val):
        # print(BST.printSelf(self))
        if self.root == None:
            return False
        if self.root.value == find_val:
            return True
        if self.root.value < find_val:
            return BST.searchNode(self.root.left, find_val)
        return BST.searchNode(self.root.right,find_val)

