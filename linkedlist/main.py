from typing import List
from node import No
from linkedlist import ListaEncadeada

l1 = ListaEncadeada()
l2 = ListaEncadeada()

elem_l1 = input().split()
elem_l2 = input().split()

for i in range((len(elem_l1) - 1), -1, -1):
    l1.insereElementoFinal(elem_l1[i])

for i in range((len(elem_l2) - 1), -1, -1):
    l1.insereElementoFinal(elem_l2[i])

print(l1)
print(l2)
auxiliar = l1.solucao(l1, l2)
print(auxiliar)
