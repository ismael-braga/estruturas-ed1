from node import No
from linkedstack import PilhaDinamica
from linkedlist.linkedlist import ListaEncadeada

p1 = PilhaDinamica()
p2 = PilhaDinamica()
n = int(input())
elementos = list(map(int, input().split()))
for i in range(n):
    p1.empilha(elementos[i])
for i in range(n):
    p2.empilha(p1.desempilha())
print(p2)
