from node import No
from linkedlist.linkedlist import ListaEncadeada

class PilhaDinamica:
    def __init__(self):
        self._topo = None
        self._tamanho = 0
    
    def empilha(self, elemento):
        #Metodo que insere um elemento no topo da pilha
        no = No(elemento)
        no.proximo = self._topo
        self._topo = no
        self._tamanho = self._tamanho + 1

    def desempilha(self):
        #Metodo que remove um elemento do topo da pilha
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
    
    def restauraPilha(self):
        #Metodo que restaura a pilha
        self._topo = None
        self._tamanho = 0

    def invertePilha(self):
        #Metodo que inverte a pilha
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        p1 = PilhaDinamica()
        p2 = PilhaDinamica()
        apontador = self._topo
        while apontador != None:
            p1.empilha(self.desempilha())
            apontador = apontador.proximo

        apontador = p1._topo
        while apontador != None:
            p2.empilha(p1.desempilha())
            apontador = apontador.proximo
        
        apontador = p2._topo
        while apontador != None:
            self.empilha(p2.desempilha())
            apontador = apontador.proximo
    
    def pilhasIguais(self, pilha, tamanho_pilha):
        #Metodo que verifica se duas pilhas sao iguais
        i = 0
        p1 = self._topo
        p2 = pilha._topo
        if self._tamanho == tamanho_pilha:
            while i < tamanho_pilha:
                if p1.dado == p2.dado:
                    p1 = p1.proximo
                    p2 = p2.proximo
                    i = i + 1
                else:
                    break
        if i == self._tamanho:
            return 'Sim'
        return 'Nao'

    def verificaParentizacao(self, elemento):
        #Metodo que verifica a parentizacao
        auxiliar = PilhaDinamica()
        balanceamento = True
        indice = 0
        while indice < len(elemento) and balanceamento == True:
            simbolo = elemento[indice]
            if simbolo == '(':
                auxiliar.empilha(simbolo)
            else:
                if auxiliar.estaVazia():
                    balanceamento = False
                else:
                    auxiliar.desempilha()
            indice = indice + 1
        
        if balanceamento == True and auxiliar.estaVazia():
            return 'Correto'
        else:
            return 'Incorreto'

    def ordenaLista(self, lista):
        #Metodo que ordena uma lista utilizando duas pilhas
        p1 = PilhaDinamica()
        p2 = PilhaDinamica()
        indice = 0
        while indice < len(lista):
            elemento = lista[indice]
            if indice == 0:
                p1.empilha(elemento)
            else:
                if elemento <= p1._topo.dado:
                    p1.empilha(elemento)
                else:
                    apontador = p1._topo
                    while apontador != None:
                        if elemento > apontador.dado:
                            p2.empilha(p1.desempilha())
                            apontador = apontador.proximo
                        else:
                            break
                    p1.empilha(elemento)
                    apontador = p2._topo
                    while apontador != None:
                        p1.empilha(p2.desempilha())
                        apontador = apontador.proximo
            indice = indice + 1
        return p1

    def concatenaPilhas(self, p2):
        #Metodo que concatena duas pilhas
        self._tamanho = self._tamanho + p2._tamanho
        novo_topo = p2._topo
        apontador = p2._topo
        while apontador.proximo != None:
            apontador = apontador.proximo
        apontador.proximo = self._topo
        self._topo = novo_topo
        p2.restaurarPilha()

    def elementoContido(self, elemento):
        #Metodo que verifica se um elemento esta contido em uma pilha
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        apontador = self._topo
        while apontador != None:
            if apontador.dado == elemento:
                return True
            apontador = apontador.proximo
        return False

    def delimitadores(self, expressao):
        auxiliar = PilhaDinamica()
        abertura = '[({'
        fechamento = '])}'
        for i in expressao:
            if i in abertura:
                auxiliar.empilha(i)
            elif i in fechamento:
                indice = fechamento.index(i)
                if auxiliar.tamanhoPilha() > 0 and abertura[indice] == fechamento[auxiliar.tamanhoPilha() - 1]:
                    auxiliar.desempilha()
                else:
                    return 'Nao'
        if auxiliar.tamanhoPilha() == 0:
            return 'Sim'
        else:
            return 'Nao'
    

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
