class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self): #inicializamos a pilha vazia
        self.top = None
        self._size = 0
    
    def isEmpty(self): #retorna booleano para sabermos se a pilha é vazia
        return self.top is None

    def push(self, value): #método de adição de elementos
        newElement = Node(value)
        
        if self.isEmpty():
            self.top = newElement
        else:
            newElement.next = self.top #adição de elementos realoca referências
            self.top = newElement
        self._size += 1
    
    def pop(self): #método de remoção do elemento do topo da pilha
        
        if self.isEmpty():
            return None
        else:
            popped_element = self.top
            self.top = self.top.next #fazemos o segundo elemento passar a ser o primeiro
            self._size -= 1
            return popped_element.value
        
    def peek(self): #método para checarmos o primeiro elemento da pilha
        
        if self.isEmpty():
            return None
        else:
            return self.top.value
    
    def size(self): #retorna o tamanho da pilha contando todos os elementos que não forem None (fim da fila)
        return self._size

# Exemplo de uso:
pilha = Stack()

# Adicionando elementos
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(f"Topo da pilha: {pilha.peek()}")  # Exibe o topo da pilha
print(f"Tamanho da pilha: {pilha.size()}")  # Exibe o tamanho da pilha

# Removendo elementos
print(f"Elemento removido: {pilha.pop()}")  # Remove o topo
print(f"Novo tamanho da pilha: {pilha.size()}") #Mostra novo tamanho da pilha
print(f"Topo da pilha após remoção: {pilha.peek()}") #Mostra novo topo da pilha