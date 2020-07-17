"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Your code goes here
        # new_element.next = self.head
        # self.head = new_element
        if self.head == None:
            self.head = new_element
            new_element = None
        else:
            self.head.next = new_element
            new_element.next = None


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        count = 0
        temp = self.head
        while temp != None:
            print(temp.value)
            if count == position - 1:
                print(temp.value)
                return temp
            count += 1
            temp = temp.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        count = 0
        curr = self.head
        while (curr != None):
            count += 1
            if count == position - 1:
                temp = curr.next
                curr.next = new_element
                new_element.next = temp
            curr = curr.next

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        # curr = self.head
        # prev = None
        # while curr != None:
        #     if temp.value == value: