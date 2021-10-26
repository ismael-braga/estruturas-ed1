from node import No
from doublylinkedlist.doublylinkedlist import ListaDuplamenteEncadeada

class PilhaDuplamenteEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0
    
    def empilha(self, elemento):
        no = No(elemento)
        apontador = self._topo
        no.proximo = apontador
        no.anterior = apontador
        self._topo = no
        self._tamanho = self._tamanho + 1
    
    def desempilha(self):
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        else:
            elemento_removido = self._topo
            novo_topo = self._topo.proximo
            self._topo = novo_topo
        self._tamanho = self._tamanho - 1
        return elemento_removido.dado
    
    def topo(self):
        #Metodo que retorna o elemento que esta no topo da pilha
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        return self._topo.dado

    def tamanhoPilha(self):
        #Metodo que retorna o tamanho da pilha
        return self._tamanho

    def estaVazia(self):
        #Metodo que verifica se a pilha esta vazia
        if self._tamanho == 0:
            return True
        return False

    def estaCheia(self):
        #Metodo que verifica se a pilha esta cheia
        return False
    
    def buscaElemento(self, pilha, elemento):
        pilha = pilha
        if elemento % 2 == 0:
            apontador = pilha._topo
            while apontador != None:
                if apontador.dado == elemento:
                    print(pilha)
                    break
                pilha.desempilha()
                apontador = apontador.proximo
            if apontador == None:
                print(0)
        else:
            apontador = pilha._topo
            while apontador != None:
                if apontador.dado == elemento:
                    print(pilha)
                    break
                pilha.desempilha()
                apontador = apontador.proximo
            if apontador == None:
                print(0)

    def __len__(self):
        #Metodo que retorna o tamanho da pilha, exemplo: len(pilha)
        return self._tamanho

    def __repr__(self):
        #Metodo que mostra a pilha para o desenvolvedor no modo interativo do Python
        return str(self)

    def __str__(self):
        #Metodo que mostra a pilha para o usuario atraves da funcao print()
        representacao = ''
        apontador = self._topo
        while apontador != None:
            representacao = representacao + f'{apontador.dado} '
            apontador = apontador.proximo
        return representacao

    def __del__(self):
        #Metodo destrutor
        return 
