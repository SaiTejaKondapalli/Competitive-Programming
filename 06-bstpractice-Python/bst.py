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
        self.insertNode(self.root, new_val)

    def insertNode(self,node,new_val):
        if node.value < new_val:
            if node.right is None:
                node.right = Node(new_val)
            else:
                self.insertNode(node.right, new_val)
        else:
            if node.left is None:
                node.left = Node(new_val)
            else:
                self.insertNode(node.left, new_val)

    def printSelf(self):
        # Your code goes here
        if self.root:
            BST.printSelf(self.root.left)
            print(self.root.value)
            BST.printSelf(self.root.right)

    def search(self, find_val):
        # Your code goes here
        return self.searchNode(self.root, find_val)

    def searchNode(self,node,find_val):
        # print(BST.printSelf(self))
        if node == None:
            return False
        if node.value == find_val:
            return True
        if node.value < find_val:
            return self.searchNode(node.right, find_val)
        if node.value > find_val:
            return self.searchNode(node.left,find_val)
        return False
