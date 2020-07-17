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
        new_element.next = this.head
        head = new_element


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        count = 0
        temp = head
        while temp != null:
            count += 1
            if count == position:
                return temp.value
            temp = temp.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        count = 0
        curr = head
        while (curr != null):
            count += 1
            if count == position - 1:
                temp = curr.next
                curr.next = new_element
                new_element.next = temp
            curr = curr.next

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp = head
        head = temp.next
        return temp
