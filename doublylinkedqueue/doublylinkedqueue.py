from node import No
from doublylinkedlist.doublylinkedlist import ListaDuplamenteEncadeada

class FilaDuplamenteEncadeada:
    def __init__(self):
        self._inicio = None
        self._final = None
        self._tamanho = 0
    
    def enfileira(self, elemento):
        #Metodo que insere um elemento no final da fila
        no = No(elemento)
        if self._tamanho == 0:
            self._inicio = no
            self._final = no
        else:
            apontador = self._final
            apontador.proximo = no
            no.anterior = apontador
            self._final = no
        self._tamanho = self._tamanho + 1
    
    def desenfileira(self):
        #Metodo que remove o elemento que esta no início da fila
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        else:
            if self._tamanho == 1:
                elemento_removido = self._inicio.dado
                self._inicio = None
                self._final = None
            else:
                elemento_removido = self._inicio.dado
                apontador = self._inicio.proximo
                self._inicio = apontador
        self._tamanho = self._tamanho - 1
        return elemento_removido

    def tamanhoFila(self):
        #Metodo que retorna o tamanho da fila
        return self._tamanho
    
    def estaVazia(self):
        #Metodo que verifica se a fila esta vazia
        if self._tamanho == 0:
            return True
        return False

    def estaCheia(self):
        #Metodo que verifica se a fila esta cheia
        return False
    
    def primeiroElemento(self):
        #Metodo que retorna o primeiro elemento da fila
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        return self._inicio.dado
    
    def ultimoElemento(self):
        #Metodo que retorna o ultimo elemento da fila
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        return self._final.dado

    def restauraFila(self):
        #Metodo que restaura a fila
        self._inicio = None
        self._final = None
        self._tamanho = 0

    def inverteFila(self):
        #Metodo que inverte a fila original
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        inicio = 0
        final = self._tamanho - 1
        while inicio < (self._tamanho // 2):
            auxiliar = self[inicio]
            self[inicio] = self[final]
            self[final] = auxiliar
            inicio = inicio + 1
            final = final - 1

    def criaFilaInvertida(self):
        #Metodo que cria uma fila com os elementos invertidos
        fila_invertida = FilaDuplamenteEncadeada()
        final = self._tamanho - 1
        while final >= 0:
            fila_invertida.enfileira(self[final])
            final = final - 1
        return fila_invertida
    
    def criaCopiaFila(self):
        #Metodo que cria uma copia da fila"""
        fila_copia = FilaDuplamenteEncadeada()
        apontador = self._inicio
        while apontador != None:
            fila_copia.enfileira(apontador.dado)
            apontador = apontador.proximo
        return fila_copia
    
    def elementoContido(self, elemento):
        #Metodo auxiliar que verifica se um elemento esta contido na fila
        apontador = self._inicio
        while apontador != None:
            if apontador.dado == elemento:
                return True 
            apontador = apontador.proximo
        return False

    def filasIguais(self, fila, tamanho_fila):
        #Metodo que verifica se duas filas sao iguais
        if self._tamanho == tamanho_fila:
            apontador = self._inicio
            i = 0
            while i < tamanho_fila:
                if apontador.dado == fila[i]:
                    apontador = apontador.proximo
                    i = i + 1
                else:
                    return False
        if i == self._tamanho:
            return True
        return False
    
    def concatenaFilas(self, f2):
        #Metodo que concatena duas filas
        self._tamanho = self._tamanho + f2._tamanho
        auxiliar = f2._final
        self._final.proximo = f2._inicio
        self._final = auxiliar
        f2.restauraFila()
    
    def __len__(self):
        #Metodo que retorna o tamanho da fila, exemplo: len(fila)
        return self._tamanho

    def __getitem__(self, indice):
        #Acessa o elemento em determinada posicao, exemplo: fila[indice]
        apontador = self._inicio
        i = 0
        while i != indice:
            if apontador != None:
                apontador = apontador.proximo
                i = i + 1
        if apontador != None:
            return apontador.dado
        else:
            raise IndexError('Indice fora do intervalo.')
    
    def __setitem__(self, indice, elemento):
        #Altera um valor a partir de um indice, exemplo: fila[indice] = elemento
        apontador = self._inicio
        i = 0
        while i != indice:
            if apontador != None:
                apontador = apontador.proximo
                i = i + 1
        if apontador != None:
            apontador.dado = elemento
        else:
            raise IndexError('Indice da fila fora do intervalo.')

    def __repr__(self):
        #Metodo que mostra a fila para o desenvolvedor no modo interativo do Python
        return str(self)

    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        representacao = ''
        apontador = self._inicio
        while(apontador != None):
            representacao = representacao + f"{apontador.dado} "
            if apontador.proximo is None:
                break
            apontador = apontador.proximo
        return representacao

    """
    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        representacao = "\033[1;31m" + "Primeiro" + "\033[0;0m" + "\n"
        representacao = representacao + "\033[1;34mNone\033[0;0m "
        apontador = self._inicio
        while(apontador != None):
            representacao = representacao + f" <- {apontador.dado} -> "
            if apontador.proximo is None:
                break
            apontador = apontador.proximo
        representacao = representacao + "\033[1;34mNone\033[0;0m"
        return representacao
    """

    def __del__(self):
        #Metodo destrutor
        return
