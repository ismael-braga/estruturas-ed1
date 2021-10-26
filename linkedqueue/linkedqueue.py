from typing import List, final
from node import No
from linkedlist.linkedlist import ListaEncadeada

class FilaDinamica:
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
            self._final = no
        self._tamanho = self._tamanho + 1

    def desenfileira(self):
        #Metodo que remove o elemento que esta no inicio da fila
        if self._tamanho != 0:
            elemento_removido = self._inicio.dado
            self._inicio = self._inicio.proximo
        else:
            raise Exception('Fila vazia.')
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
        #Metodo que inverte os elementos originais da fila
        if self._tamanho == 0:
            raise Exception('Fila vazia.')

        lista = ListaEncadeada()

        apontador = self._inicio
        while apontador != self._final.proximo:
            lista.insereElementoFinal(self._inicio.dado)
            self.desenfileira()
            apontador = apontador.proximo
        
        apontador = lista._cabeca
        final = lista._tamanho - 1
        while apontador != None:
            self.enfileira(lista[final])
            final = final - 1
            apontador = apontador.proximo

    def criaFilaInvertida(self):
        #Metodo que cria uma fila com os elementos invertidos
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        
        fila_invertida = FilaDinamica()
        lista = ListaEncadeada()

        apontador = self._inicio
        while apontador != self._final.proximo:
            lista.insereElementoFinal(apontador.dado)
            apontador = apontador.proximo

        apontador = lista._cabeca
        final = lista._tamanho - 1
        while apontador != None:
            fila_invertida.enfileira(lista[final])
            final = final - 1
            apontador = apontador.proximo
        return fila_invertida

    def criaCopiaFila(self):
        #Metodo que cria uma copia da fila
        fila_copia = FilaDinamica()
        apontador = self._inicio
        while apontador != self._final.proximo:
            fila_copia.enfileira(self.desenfileira())
            apontador = apontador.proximo
        return fila_copia

    def elementoContido(self, elemento):
        #Metodo auxiliar que verifica se um elemento esta contido na fila
        if self._tamanho == 0:
            raise Exception('Fila vazia.')
        apontador = self._inicio
        while apontador != None:
            if apontador.dado == elemento:
                return True 
            apontador = apontador.proximo
        return False

    def filasIguais(self, fila, tamanho_fila):
        #Metodo que verifica se duas filas sao iguais
        i = 0
        f1 = self._inicio
        f2 = fila._inicio
        if self._tamanho == tamanho_fila:
            while i < tamanho_fila:
                if f1.dado == f2.dado:
                    f1 = f1.proximo
                    f2 = f2.proximo
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

    def palindromo(self, palavra):
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
    def somaFila(self, primeira_quantidade, segunda_quantidade):
        f1 = FilaDinamica()
        f2 = FilaDinamica()
        i = 0
        while i < primeira_quantidade:
            f1.enfileira(self.desenfileira())
            i = i + 1
        j = 0
        while j < segunda_quantidade:
            f2.enfileira(self.desenfileira())
            j = j + 1  
        apontador_f1 = f1._inicio
        apontador_f2 = f2._inicio
        while apontador_f1 != None and apontador_f2 != None:
            if f1.tamanhoFila() - f2.tamanhoFila() == 0:
                self.enfileira((apontador_f1.dado + apontador_f2.dado))
            else:
                indice = 0
                if primeira_quantidade > segunda_quantidade:
                    while indice != f1.tamanhoFila() - f2.tamanhoFila():
                        self.enfileira(apontador_f1.dado)
                        indice = indice + 1
                        apontador_f1 = apontador_f1.proximo
                elif segunda_quantidade > primeira_quantidade:
                    while indice != f2.tamanhoFila() - f1.tamanhoFila():
                        self.enfileira(apontador_f2.dado)
                        indice = indice + 1
                        apontador_f2 = apontador_f2.proximo
                while apontador_f1 != None and apontador_f2 != None:
                    self.enfileira((apontador_f1.dado + apontador_f2.dado))
                    apontador_f1 = apontador_f1.proximo
                    apontador_f2 = apontador_f2.proximo
                if apontador_f1 == None and apontador_f2 == None:
                    break
            apontador_f1 = apontador_f1.proximo
            apontador_f2 = apontador_f2.proximo
    """    
    
    def __len__(self):
        #Metodo que retorna o tamanho da fila, exemplo: len(fila)
        return self._tamanho

    def __repr__(self):
        #Metodo que mostra a fila para o desenvolvedor no modo interativo do Python"""
        return str(self)

    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        representacao = ''
        apontador = self._inicio
        while(apontador != None):
            representacao += f"{apontador.dado} "
            if apontador.proximo is None:
                break
            apontador = apontador.proximo
        return representacao
    
    """
    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        representacao = "\033[1;31m" + "Primeiro" + "\033[0;0m" + " -> "
        apontador = self._inicio
        while(apontador != None):
            representacao += f"{apontador.dado} -> "
            if apontador.proximo is None:
                break
            apontador = apontador.proximo
        representacao += "\033[1;34mNone\033[0;0m"
        return representacao
    """

    def __del__(self):
        #Metodo destrutor
        return
