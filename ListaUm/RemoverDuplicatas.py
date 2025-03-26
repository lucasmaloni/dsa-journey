class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
class LinkedList:

    def __init__(self):
        #inicializamos a lista vazia, cabeça é None
        self.head = None
    
    def adicionar(self, valor):
        #cenário em que a LinkedList está vazia - apenas tornamos a cabeça novo Nó com valor
        if self.head == None: 
            self.head = Node(valor)
        else:
            #atribuímos a cabeça da lista como elemento que estamos olhando
            current_node = self.head
            while current_node is not None: #enquanto não for None, não chegamos ao último elemento
                current_node = current_node.next
            
            #chegamos ao último elemento, aqui, dizemos que next (None) é igual a um novo Node com o conteudo valor
            current_node.next = Node(valor)
    
    def remover(self, valor):
        if self.head == None: #lista vazia
            return "Lista está vazia ,não há o que remover!"
        
        if self.head.valor == valor: #valor está no primeiro nó da lista
            self.head = self.head.next #tornamos o próximo elemento a cabeça, o resto não muda nada!
            return
        
        #lista não é vazia nem valor é o primeiro elemento
        current_node = self.head
        previous_node = None
        
        while current_node.next is not None:
            #Aqui, encontramos valor ono penúltimo nó               
            if current_node.valor == valor:
                #o último nó vira o último nó
                if previous_node:
                    previous_node.next = current_node.next
                    return
            
            previous_node = current_node
            current_node = current_node.next
        
        return "Valor não encontrado na lista"

def remover_duplicatas(lista: LinkedList):
    if lista.head is None:
        print("A lista está vazia! Não há duplicidades para remover!")
    else:
        # Vamos percorrer a lista a partir do primeiro nó
        no_verificado = lista.head
        
        while no_verificado is not None:
            # O ponteiro current_node vai verificar todos os nós após o no_verificado
            current_node = no_verificado
            while current_node.next is not None:
                if current_node.next.valor == no_verificado.valor:
                    # Se encontramos um valor duplicado, removemos o nó
                    current_node.next = current_node.next.next
                else:
                    # Se não for duplicado, apenas avançamos o ponteiro
                    current_node = current_node.next
            
            # Avançamos para o próximo nó a ser verificado
            no_verificado = no_verificado.next
        
        print("Valores duplicados removidos!") 
        