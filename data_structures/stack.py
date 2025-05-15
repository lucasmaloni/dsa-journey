class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self): #inicializamos a pilha vazia
        self.top = None
        self._size = 0
    
    def is_empty(self): #retorna booleano para sabermos se a pilha é vazia
        return self.top is None

    def push(self, value): #método de adição de elementos
        new_element = Node(value)
        
        if self.is_empty():
            self.top = new_element
        else:
            new_element.next = self.top #adição de elementos realoca referências
            self.top = new_element
        self._size += 1
    
    def pop(self): #método de remoção do elemento do topo da pilha
        
        if self.is_empty():
            return None
        else:
            popped_element = self.top
            self.top = self.top.next #fazemos o segundo elemento passar a ser o primeiro
            self._size -= 1
            return popped_element.value
        
    def peek(self): #método para checarmos o primeiro elemento da pilha
        
        if self.is_empty():
            return None
        else:
            return self.top.value
    
    def _size(self): #retorna o tamanho da pilha contando todos os elementos que não forem None (fim da fila)
        return self._size