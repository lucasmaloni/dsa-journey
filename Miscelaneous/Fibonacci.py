import time

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

def fibonacciIterativo(numero):
    anterior_dois = 0
    anterior_um = 1
    
    for i in range(1, numero):
        num_fibonacci = anterior_um + anterior_dois
        anterior_dois = anterior_um
        anterior_um = num_fibonacci
    
    return num_fibonacci


numero = 10

# Medindo o tempo de execução da função recursiva
inicio_recursivo = time.time()
resultado_recursivo = fibonacciRecursivo(numero)
fim_recursivo = time.time()

# Medindo o tempo de execução da função iterativa
inicio_iterativo = time.time()
resultado_iterativo = fibonacciIterativo(numero)
fim_iterativo = time.time()

# Exibindo os resultados
print(f"Resultado Fibonacci Recursivo: {resultado_recursivo}")
print(f"Tempo de execução (Recursivo): {fim_recursivo - inicio_recursivo} segundos")

print(f"Resultado Fibonacci Iterativo: {resultado_iterativo}")
print(f"Tempo de execução (Iterativo): {fim_iterativo - inicio_iterativo} segundos")