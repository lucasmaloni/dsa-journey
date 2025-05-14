class Node:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def is_circular(self):
        #se não for vazia, verificamos se o final da lista aponta para o ínicio
        if not self.is_empty():
            return self.tail.next == self.head #retorno de valor boleano
        return True
    
    def add(self, name, age):
        
        newNode = Node(name, age)
        
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        
        elif newNode.age < self.head.age:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        
        else:
            current = self.head
            previous = None
            # Caso 2: Percorrer a lista para encontrar o ponto correto de inserção
            while True:
                if newNode.age < current.age:
                    previous.next = newNode
                    newNode.next = current
                    if current == self.tail:  # Se for o último nó, currentiza o tail
                        self.tail = newNode
                    break
                previous = current
                current = current.next
                if current == self.head:  # Se chegamos de volta ao início, paramos o loop
                    break

            # Caso 3: Inserir no final (após o último nó)
            if current == self.head:  # Isso significa que percorremos toda a lista
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head  # O novo tail aponta para o head, mantendo a circularage    
        
        if self.is_circular():
            print("Lista continua circular!")
        
        else:
            print("lista não é mais circular. Erro.")
            
    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        current = self.head
        while True:
            print(f'name: {current.name}, age: {current.age}')
            current = current.next
            if current == self.head:
                break
    
#teste
lista = CircularLinkedList()

# Saídas esperadas: "Lista continua circular!"
lista.add("João", 25)
lista.add("Maria", 30)
lista.add("Pedro", 20)

lista.display()