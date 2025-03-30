class Node:
    def __init__(self, content):
        self.content = content
        self.next = None

class Deque:                
    def __init__ (self):
        self.head = None
        self.tail = self.head
    
    def addLeft(self, content):
        newNode = Node(content)
        
        if self.head is None:
            self.head = newNode
            self.tail = self.head            
        else:        
            newNode.next = self.head
            self.head = newNode
            self.head.next = newNode.next
    
    def addRight(self, content):
        newNode = Node(content)
        
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def removeLeft(self):
        
        if self.head is None:
            print("Não há elementos na lista!")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
            
    def removeRight(self):
        
        if self.tail is None:
            print("Não há elementos na lista")
            return
        elif self.tail == self.tail:
            self.tail = None
            self.head = self.tail
        else:
            currentNode = self.head
            
            while currentNode.next != self.tail:
                currentNode = currentNode.next
            
            self.tail = currentNode
            self.tail.next = None
            
deque = Deque()

deque.removeLeft()
deque.removeRight()

deque.addLeft("Lucas")
deque.addRight("Marina")

print(deque.head.content) #Lucas
print(deque.tail.content) #Marina

deque.removeLeft()

print(deque.head.content) #Marina
print(deque.tail.content) #Marina

deque.removeRight()

print(deque.head) #None
print(deque.tail) #None