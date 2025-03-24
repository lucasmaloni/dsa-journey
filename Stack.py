class Stack:
    def __init__(self): # Construtor da classe e inicializador de Array
        self.itens = []

    def push(self, item): #adição de novo elemento
        self.itens.append(item)
        print("Item adicionado!\n")
    
    def pop(self): #remoção de último elemento
        if len(self.itens)==0:
            print("Pilha vazia, impossível remover elemento.\n") 
        else:
            self.itens.pop()

    def peek(self): #mostrando ultimo elemento para usuário
        if self.is_empty():
            print("Pilha sem elementos, não há o que apresentar.\n")
        else:
            print(self.itens[-1])
    
    def is_empty(self): #retorna booleao se está ou não vazio
        return self.size() == 0

    def size(self): #tamanho da pilha
        return len(self.itens)

