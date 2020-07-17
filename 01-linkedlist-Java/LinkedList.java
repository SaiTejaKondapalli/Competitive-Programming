
class Element{
	int value;
	Element next;
	public Element(int value){
		this.value = value;
		this.next = null;
	}
}

public class LinkedList{
	Element head;
	public LinkedList(Element head){
		this.head = head;
	}

	public void append(Element new_element){
		// Your code goes here
		Element temp = head;
		while (temp.next != null) {
			temp = temp.next;
		}
		temp.next = new_element;
		new_element.next = null;
	}

	public Element get_position(int position){
		// Get an element from a particular position.
        // Assume the first position is "1".
        // Return null if position is not in the list
		// Your code goes here
		int count = 0;
		Element curr = head;
		while (curr != null) {
			System.out.println(curr.value);
			if (count == position - 1) {
				return curr;
			}
			count += 1;
			curr = curr.next;
		}
		return null;

	}

	public void insert(Element new_element, int position){
	   // """Insert a new node at the given position.
       // Assume the first position is "1".
       // Inserting at position 3 means between
       // the 2nd and 3rd elements."""
		// Your code goes here
		int count = 0;
		Element curr = head;
		while (curr != null) {
			count += 1;
			if (count == position - 1) {
				Element temp = curr.next;
				curr.next = new_element;
				new_element.next = temp;
			}
			curr = curr.next;
		}
	}

	public void delete(int value) {
		// Delete the first node with a given value.
		// Your code goes here
		Element curr = head;
		Element prev = null;
		if (curr != null && curr.value == value) {
			head = curr.next;
			return;
		}
		while (curr != null && curr.value != value) {
			prev = curr;
			curr = curr.next;
		}
		if (curr == null)
			return;
		prev.next = curr.next;
	}
}
