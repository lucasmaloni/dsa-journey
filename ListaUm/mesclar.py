from ListaCircular import LinkedListCircular

def mesclar(lista1, lista2):
    # Criar uma nova lista circular que será a lista mesclada
    lista_mesclada = LinkedListCircular()
    
    # Inicializar ponteiros para ambas as listas
    atual1 = lista1.head
    atual2 = lista2.head

    # Se ambas as listas estiverem vazias
    if lista1.e_vazio() and lista2.e_vazio():
        return lista_mesclada

    # Mesclar as duas listas
    while True:  # Continuar até percorrer ambas as listas
        # Se a idade do atual1 for menor que a de atual2, adicionamos o atual1
        if atual1.idade < atual2.idade:
            lista_mesclada.adicionar(atual1.nome, atual1.idade)
            atual1 = atual1.next
            if atual1 == lista1.head:  # Verifica se chegou ao final de lista1
                break
        else:
            lista_mesclada.adicionar(atual2.nome, atual2.idade)
            atual2 = atual2.next
            if atual2 == lista2.head:  # Verifica se chegou ao final de lista2
                break

    # Adicionar os elementos restantes de lista1, se houver
    while atual1 != lista1.head:
        lista_mesclada.adicionar(atual1.nome, atual1.idade)
        atual1 = atual1.next

    # Adicionar os elementos restantes de lista2, se houver
    while atual2 != lista2.head:
        lista_mesclada.adicionar(atual2.nome, atual2.idade)
        atual2 = atual2.next

    # Retornar a lista mesclada
    return lista_mesclada

# Criando as duas listas encadeadas
lista1 = LinkedListCircular()
lista1.adicionar("João", 25)
lista1.adicionar("Ana", 22)
lista1.adicionar("Maria", 30)

lista2 = LinkedListCircular()
lista2.adicionar("Carlos", 20)
lista2.adicionar("Pedro", 26)
lista2.adicionar("Juliana", 24)

# Mesclar as duas listas
lista_mesclada = mesclar(lista1, lista2)

# Exibir a lista mesclada
lista_mesclada.display()  # A lista deve ser exibida ordenada por idade: Carlos (20), Ana (22), Juliana (24), João (25), Pedro (26), Maria (30)
