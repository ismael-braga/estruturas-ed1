from typing import Collection
from itemhash import ItemHash
from tabelahash import TabelaHash

'''
th = TabelaHash()
n = 10
for i in range(n):
    elementos = list(map(str, input().split()))
    elementos[0] = int(elementos[0])
    th.inserirElemento(elementos[0], elementos[1])
    del elementos

q = int(input())
chaves = []
for j in range(q):
    chave = int(input())
    chaves.append(chave)

for k in range(len(chaves)):
    print(th.buscarElemento(chaves[k]))
'''

th = TabelaHash(10)
H = int(input())
elementos = list(map(int, input().split()))

if H == 1:
    for i in range(10):
        th.inserirElemento(elementos[i], elementos[i], 1)
        colisao = th.colisoes()
        
elif H == 2:
    for i in range(10):
        th.inserirElemento(elementos[i], elementos[i], 2)
        colisao = th.colisoes()
elif H == 3:
    for i in range(10):
        th.inserirElemento(elementos[i], elementos[i], 3)
        colisao = th.colisoes()
elif H == 4:
    for i in range(10):
        th.inserirElemento(elementos[i], elementos[i], 4)
        colisao = th.colisoes()

print(colisao)
