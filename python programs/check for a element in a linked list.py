# Iterative Python program to search
# an element in linked list
 
# Node class
class Node:
     
    # Function to initialise the
    # node object
    def __init__(self, data):
     
        # Assign data
        self.data = data
 
        # Initialize next as null
        self.next = None
 
# Linked List class
class LinkedList:
    def __init__(self):
 
        # Initialize head as None
        self.head = None
 
    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):
     
        # Create a new Node
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node
 
    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):
 
        # Initialize current to head
        current = self.head
 
        # Loop till current not equal to None
        while current != None:
            if current.data == x:
 
                # Data found
                return True
             
            current = current.next
         
        # Data Not found
        return False
 
# Driver code
if __name__ == '__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Use push() to construct list
    # 14->21->11->30->10
    llist.push(10);
    llist.push(30);
    llist.push(11);
    llist.push(21);
    llist.push(14);
 
    if llist.search(21):
        print("Yes")
    else:
        print("No")
