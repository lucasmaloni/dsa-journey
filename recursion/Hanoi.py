def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        # Caso base: mover o único disco da origem para o destino
        print(f"Mover disco 1 de {origem} para {destino}")
    else:
        # Passo 1: mover n-1 discos de origem para a torre auxiliar
        torres_de_hanoi(n-1, origem, auxiliar, destino)
        
        # Passo 2: mover o disco maior (n) da origem para o destino
        print(f"Mover disco {n} de {origem} para {destino}")
        
        # Passo 3: mover os n-1 discos da torre auxiliar para o destino
        torres_de_hanoi(n-1, auxiliar, destino, origem)

# Exemplo de uso da função com 3 discos
n = 2
torres_de_hanoi(n, 'A', 'C', 'B')
