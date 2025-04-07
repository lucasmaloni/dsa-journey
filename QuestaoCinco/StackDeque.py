from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def pushTop(self, value):
        self.stack.appendleft(value) #função da biblioteca que adiciona elemento no inicio da pilha
        
    def pushBottom(self, value):
        self.stack.append(value) #função da biblioteca que adiciona elemento no fim da pilha
    
    def removeTop(self):
        if self.isEmpty():
            print("Lista vazia, sem elementos para remover!")
            return None
        else:
            self.stack.popleft()
            
    def removeBottom(self):
        if self.isEmpty():
            print("Lista vazia, sem elementos para remover!")
            return None
        else:
            self.stack.pop()
    
    