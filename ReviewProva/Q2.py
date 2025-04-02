def sequenciaDeJacobsthal(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num > 1:
        return sequenciaDeJacobsthal(num-1) + 2*sequenciaDeJacobsthal(num-2)
    
print(sequenciaDeJacobsthal(0))
print(sequenciaDeJacobsthal(1))
print(sequenciaDeJacobsthal(2))
print(sequenciaDeJacobsthal(3))
print(sequenciaDeJacobsthal(4))
print(sequenciaDeJacobsthal(5))
