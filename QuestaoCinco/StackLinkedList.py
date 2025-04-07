class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None

    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    
    def pop(self):
        if self.isEmpty():
            print("Pilha vazia!")
            return None
        else:
            poppedValue = self.top
            self.top = self.top.next
            return poppedValue
    
    