class Node:
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None

    def add(self, value):
        #add value to the end of the list
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
    def remove(self):
        #remove from the start of the list
        if self.is_empty():
            print("nothing to remove!\n")
            return

        else:
            removed_element = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return removed_element
    
    def display(self):
        #print all the values of the list
        elements = []
        
        if self.is_empty():
            return elements
        
        else:
            current = self.head
            
            while current is not None:
                elements.append(current.value)
                current = current.next
            
            return elements
        
#testing

dllist = DoublyLinkedList()

dllist.add(1)
dllist.add(2)
dllist.add(3)
dllist.add(4)
dllist.add(5)

#[1, 2, 3, 4, 5]
print(dllist.display())

print(dllist.remove())  #1
print(dllist.remove())  #2
print(dllist.remove())  #3

#[4, 5]
print(dllist.display())