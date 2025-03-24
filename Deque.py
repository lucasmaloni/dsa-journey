'''
Implemente um Deque utilizando listas encadeadas. O TAD deve permitir inserções e
remoções em ambas as extremidades. Após a implementação, explique a escolha da
estrutura de lista encadeada utilizada e justifique as vantagens dessa abordagem.
'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def adicionar(self, valor):
        #cenário em que a LinkedList está vazia - apenas tornamos a cabeça novo Nó com valor
        if self.head == None: 
            self.head = Node(valor)
        else:
            #contionuar
            return 0