class Node:
    
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class FilaCircular:

    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanhoMaximo = 5
        self.tamanhoAtual = 0
        
    def isFull (self):
        return self.tamanhoAtual > self.tamanhoMaximo

    def enqueue(self, valor):
        novoNo = Node(valor)

        if self.head is None:
            self.head = novoNo
            self.tail = self.head
        else:
            self.tail.next = novoNo     #realocamos os ponteiros do tail
            self.tail = novoNo          #realocamos o tail
            self.tail.next = self.head  #realocamos o ponteiro do novo tail
        
        self.tamanhoAtual += 1
        
        if self.isFull():
            self.head = self.head.next
            self.tail.next = self.head
            self.tamanhoAtual -= 1


    def dequeue (self):
        if self.head is None:
            print("lista vazia")
            return
        
        else:
            self.head.next  = self.head
            self.tail.next = self.head
            self.tamanhoAtual -= 1
    
    def display(self):
        if self.head is None:
            print("fila vazia, não há o que mostrar!")
            return
        
        else:
            current = self.head
            elementos = []
            for i in range(self.tamanhoAtual):
                elementos.append(current.valor)
                current = current.next
            
            return elementos

fila = FilaCircular()

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.enqueue(40)
fila.enqueue(50)

print(fila.display()) #saída esperada -> [10, 20, 30, 40, 50]

fila.enqueue(60)

print (fila.display()) #saída esperada -> [20, 30, 40, 50, 60]
