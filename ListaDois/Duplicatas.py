def removeDups(list):
    validSet = set() #uso de sets por só conter valores únicos
    
    #queremos controlar nós atuais e anteriores, para fazer realocação de nexts entre os nós!
    currentNode = list.head
    previousNode = None 
    
    if currentNode is None:
        print("Lista está vazia!")
        return list
    
    while currentNode is not None:
        
        if currentNode.content not in validSet:
            validSet.add(currentNode.content)
            previousNode = currentNode
            currentNode = currentNode.next
        else:
            previousNode.next = currentNode.next
            currentNode = currentNode.next
    
    return list
            
