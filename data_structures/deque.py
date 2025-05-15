class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Deque:                
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def add_left(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head            
        else:        
            new_node.next = self.head
            self.head = new_node
    
    def add_right(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_left(self):
        if self.head is None:
            print("No elements in the list!")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
            
    def remove_right(self):
        if self.tail is None:
            print("No elements in the list!")
            return
        elif self.tail == self.tail:
            self.tail = None
            self.head = self.tail
        else:
            current_node = self.head
            
            while current_node.next != self.tail:
                current_node = current_node.next
            
            self.tail = current_node
            self.tail.next = None
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Tests
deque = Deque()

deque.remove_left()
deque.remove_right()

deque.add_left("Lucas")
deque.add_right("Marina")

print(deque.head.value)  # Lucas
print(deque.tail.value)  # Marina

deque.remove_left()

print(deque.head.value)  # Marina
print(deque.tail.value)  # Marina

deque.remove_right()

print(deque.head)  # None
print(deque.tail)  # None
