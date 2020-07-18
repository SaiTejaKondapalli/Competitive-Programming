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
        if self.root is None:
            self.root.value = new_val
        else:
            if self.root.value < new_val:
                if self.root.right is None:
                    self.root.right.value = new_val
                else:
                    return insert(self.root.right, new_val)
            else:
                if self.root.left is None:
                    self.root.left.value = new_val
                else:
                    return self.insert(self.root.left, new_val)

    def printSelf(self):
        # Your code goes here
        if self.root:
            self.printSelf(self.root.left)
            print(self.root.value)
            self.printSelf(self.root.right)

    def search(self, find_val):
        # Your code goes here
        if self.root is None or self.root.value == find_val:
            return self.root
        if self.root.value < find_val:
            return self.search(self.root.left, find_val)
        return self.search(self.root.right,find_val)

