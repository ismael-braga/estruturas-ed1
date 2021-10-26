from no import No
from avl import AVL

myTree = AVL()
raiz = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    raiz = myTree.inserir(raiz, num)
key = 13
raiz = myTree.remover(raiz, key)

myTree.Ordem(raiz)
