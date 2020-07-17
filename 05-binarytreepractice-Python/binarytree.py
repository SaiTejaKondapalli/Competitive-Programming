class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if self.root:
            return BinaryTree.preorder_search(self, self.root, find_val)
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        traversal = []
        BinaryTree.preorder_print(self, self.root, traversal)
        return ' '.join(traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        # Your code goes here
        if start:
            if start.value == find_val:
                return True
            left = BinaryTree.preorder_search(self, start.left, find_val)
            right = BinaryTree.preorder_search(self, start.right, find_val)
            return left or right
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # Your code goes here
        if start:
            traversal.append(str(start.value))
            BinaryTree.preorder_print(self, start.left, traversal)
            BinaryTree.preorder_print(self, start.right, traversal)

