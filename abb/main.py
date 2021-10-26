from bst import BST



'''

bst = BST()
elementos = [3, 2, 4]
for i in range(len(elementos)):
    bst.inserir(elementos[i])

print(bst.sucessor(3))

'''

'''

# Níveis de uma Árvore

bst = BST()
elementos = [3, 2, 1, 4, 5]
for i in range(len(elementos)):
    bst.inserir(elementos[i])

nos = bst.quantidadeNos()
impares = []
pares = []
for j in range(nos):
    nivel = bst.nivel(elementos[j])
    if nivel % 2 != 0:
        impares.append(elementos[j])
    else:
        pares.append(elementos[j])

print(impares)
print(pares)

'''

'''

# Questão - É uma AVL?

bst = BST()
elementos = [3, 1, 2, 4, 5]
for i in range(len(elementos)):
    bst.inserir(elementos[i])

raiz = bst.obterRaiz()
balanceamento = bst.balanceamento(raiz)
if balanceamento:
    print('S')
else:
    print('N')
print(f'balanceamento = {balanceamento}')

'''

'''

# Questão - Árvores Similares

bst1 = BST()
bst2 = BST()
N = int(input())

# Se N = 5

e1 = [3, 2, 1, 4, 5]
e2 = [50, 15, 20, 10, 5]

# Se N = 9

#e1 = [67, 79, 75, 88, 90, 66, 73, 76, 87]
#e2 = [55, 10, 70, 65, 60, 68, 80, 75, 85]

for i in range(N):
    bst1.inserir(e1[i])
    bst2.inserir(e2[i])

raiz1 = bst1.obterRaiz()
raiz2 = bst2.obterRaiz()

if bst1.arvoresSimilares(raiz1, raiz2):
    print('S')
else:
    print('N')

'''