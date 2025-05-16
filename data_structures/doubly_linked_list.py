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
            self.head = self.head.next
            self.head.prev = None
    
    