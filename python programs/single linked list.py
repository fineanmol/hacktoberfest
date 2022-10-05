#Creating node class of the singly linked list  
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
#Creating addNode() to add newly created nodes.
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

 #Creating display() to print newly created nodes via traversing.
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
s = SinglyLinkedList()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data = int(input('Enter data: '))
    s.addNode(data)
print('The linked list: ', end = '')
s.display()
