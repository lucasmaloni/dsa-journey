class Node:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next = None

class LinkedListCircular:
    
    def __init__(self):
        self.head = None
        self.head = None
    
    def e_vazio(self):
        return self.head is None
    
    def e_circular(self):
        
        if not self.e_vazio():
            return self.tail.next == self.head
        return True
    
    def adicionar(self, nome, idade):
        
        novo_no = Node(nome, idade)
        
        if self.e_vazio():
            self.head = novo_no
            self.tail = novo_no
            self.tail.next = self.head
        
        else:
            self.tail.next = novo_no
            self.tail = novo_no
            self.tail.next = self.head
        
        if self.e_circular():
            print("Lista continua circular!")
        
        else:
            print("lista não é mais circular. Erro.")
    
#teste
lista = LinkedListCircular()

# Saídas esperadas: "Lista continua circular!"
lista.adicionar("João", 25)
lista.adicionar("Maria", 30)
lista.adicionar("Pedro", 20)