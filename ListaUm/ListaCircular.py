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
        
        elif novo_no.idade < self.head.idade:
            novo_no.next = self.head
            self.head = novo_no
            self.tail.next = self.head
        
        else:
            atual = self.head
            anterior = None
            # Caso 2: Percorrer a lista para encontrar o ponto correto de inserção
            while True:
                if novo_no.idade < atual.idade:
                    anterior.next = novo_no
                    novo_no.next = atual
                    if atual == self.tail:  # Se for o último nó, atualiza o tail
                        self.tail = novo_no
                    break
                anterior = atual
                atual = atual.next
                if atual == self.head:  # Se chegamos de volta ao início, paramos o loop
                    break

            # Caso 3: Inserir no final (após o último nó)
            if atual == self.head:  # Isso significa que percorremos toda a lista
                self.tail.next = novo_no
                self.tail = novo_no
                self.tail.next = self.head  # O novo tail aponta para o head, mantendo a circularidade    
        
        if self.e_circular():
            print("Lista continua circular!")
        
        else:
            print("lista não é mais circular. Erro.")
            
    def display(self):
        if self.e_vazio():
            print("A lista está vazia.")
            return
        
        atual = self.head
        while True:
            print(f'Nome: {atual.nome}, Idade: {atual.idade}')
            atual = atual.next
            if atual == self.head:
                break
    
#teste
lista = LinkedListCircular()

# Saídas esperadas: "Lista continua circular!"
lista.adicionar("João", 25)
lista.adicionar("Maria", 30)
lista.adicionar("Pedro", 20)

lista.display()