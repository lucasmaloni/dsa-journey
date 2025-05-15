class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, value):
        '''add values to the end of the queue'''
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node

            
            
            
    def dequeue(self):
        '''remove from the queue (FIFO)'''
        if self.is_empty():
            print("The queue is empty! nothing to remove\n")
            return None

        else:
            dequeued_value = self.head.value
            self.head = self.head.next
            
            return dequeued_value
    
    def display(self):
        elements = []
        current = self.head
        
        while current:
            elements.append(current.value)
            current = current.next
        
        print(elements)
        
    
fila = Queue()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

fila.display()
