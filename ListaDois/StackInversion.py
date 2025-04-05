from Stack import Stack

def StackInversion(stack):
    invertedStack = Stack()
    
    current = stack.top
    while current is not None: #percorremos toda a pilha passada como argumento
        invertedStack.push(current.value)
        current = current.next
    return invertedStack

def mostrarElementos(stack):
    elementos = []
    current = stack.top
    while current is not None:
        elementos.append(current.value)
        current = current.next
    
    return elementos

pilha = Stack()

pilha.push(10)
pilha.push(20)
pilha.push(30)
pilha.push(40)
pilha.push(50)

elementos_pilha1 = mostrarElementos(pilha)
novapilha = StackInversion(pilha)
elementos_pilha2 = mostrarElementos(novapilha)

print(elementos_pilha1)
print(elementos_pilha2)
