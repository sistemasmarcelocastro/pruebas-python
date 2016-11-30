"""
def sasa(algo):
    algo.append('hola')


dada = [1, 2, 3]
sasa(dada)
print(dada)
"""
import copy

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = copy.deepcopy(lista1)
print(id(lista1))
print(id(lista2))