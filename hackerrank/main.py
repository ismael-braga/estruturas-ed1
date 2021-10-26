from node import No
from linkedlist import ListaEncadeada

n = int(input())
lista = ListaEncadeada()
elementos = list(map(int, input().split()))
for i in range(n):
    lista.insereElementoFinal(elementos[i])

if n > 2:
    inicio = 1
    proximo = n // 2
    while proximo != lista.tamanhoLista() - 1:
        lista.insereElementoPorIndice(inicio, lista[proximo])
        lista.removeElementoPorIndice(proximo + 1)
        inicio = inicio + 2
        proximo = proximo + 1
print(lista)
