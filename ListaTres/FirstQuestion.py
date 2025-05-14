import random
import time
import matplotlib.pyplot as plt

# Algoritmos de ordenação
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        valor_atual = arr[i]
        posicao = i
        while posicao > 0 and arr[posicao - 1] > valor_atual:
            arr[posicao] = arr[posicao - 1]
            posicao -= 1
        arr[posicao] = valor_atual
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[0]
    menores = [x for x in arr[1:] if x <= pivo]
    maiores = [x for x in arr[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Tamanhos de entrada
sizes = [1000, 10000, 20000, 30000, 40000, 50000]
algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Shell Sort": shell_sort,
}
timings = {name: [] for name in algorithms}

# Teste com listas aleatórias
for size in sizes:
    original = random.sample(range(size * 2), size)
    for name, func in algorithms.items():
        arr = original.copy()
        start = time.time()
        func(arr)
        end = time.time()
        timings[name].append(end - start)

# Plotagem dos resultados para listas aleatórias
plt.figure(figsize=(12, 6))
for name, times in timings.items():
    plt.plot(sizes, times, marker='o', label=name)
plt.title("Comparação de tempo - Listas Aleatórias")
plt.xlabel("Tamanho da lista")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Teste com lista decrescente de 50000 elementos
descendente = list(range(50000, 0, -1))
desc_timing = {}
for name, func in algorithms.items():
    arr = descendente.copy()
    start = time.time()
    func(arr)
    end = time.time()
    desc_timing[name] = end - start

# Plotagem dos resultados para lista decrescente
plt.figure(figsize=(10, 5))
plt.bar(desc_timing.keys(), desc_timing.values(), color='coral')
plt.title("Tempo de execução com lista decrescente (50.000 elementos)")
plt.ylabel("Tempo (s)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

desc_timing
