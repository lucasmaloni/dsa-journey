def fibonacciRecursivo(numero):
    if numero <=0:
        return "Número deve ser maior que 0!\n"
    elif numero == 1:
        return 1
    elif numero == 2:
        return 1
    else:
        #Aqui, a recursão irá entrar em loop, até ter números inteiros como retorno!
        return fibonacciRecursivo(numero-1) + fibonacciRecursivo(numero-2) 
    
print(fibonacciRecursivo(8))