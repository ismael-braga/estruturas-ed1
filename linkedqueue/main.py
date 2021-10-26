from node import No
from linkedqueue import FilaDinamica

"""
palavra = input().lower()

f1 = FilaDinamica()
f2 = FilaDinamica()
teste = palavra
i = 0
while i <= len(palavra) - 1:
    f1.enfileira(palavra[i])
    i = i + 1
i = len(palavra) - 1
while i >= 0:
    f2.enfileira(palavra[i])
    i = i - 1

if f1.filasIguais(f2, f2.tamanhoFila()):
    print('SIM')
else:
    print('NAO')
"""

fila = FilaDinamica()
quantidade = list(map(int, input().split()))
elementos = list(map(int, input().split()))
for i in range((quantidade[0] + quantidade[1])):
    fila.enfileira(elementos[i])
fila.somaFila(quantidade[0], quantidade[1])
print(fila)
