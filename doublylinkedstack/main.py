from node import No
from doublylinkedstack import PilhaDuplamenteEncadeada
from doublylinkedlist.doublylinkedlist import ListaDuplamenteEncadeada

pilha_impares = PilhaDuplamenteEncadeada()
pilha_pares = PilhaDuplamenteEncadeada()
elementos = list(map(int, input().split()))
for i in range(10):
    if elementos[i] % 2 == 1:
        pilha_impares.empilha(elementos[i])
for j in range(10):
    if elementos[j] % 2 == 0:
        pilha_pares.empilha(elementos[j])
elemento_buscado = int(input())
if elemento_buscado % 2 == 0:
    pilha_pares.buscaElemento(pilha_pares, elemento_buscado)
else:
    pilha_impares.buscaElemento(pilha_impares, elemento_buscado)
