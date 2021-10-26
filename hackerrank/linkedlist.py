from node import No

class ListaEncadeada:
    def __init__(self):
        self._cabeca = None
        self._tamanho = 0
    
    def _retornaElementoPeloIndice(self, indice):
        #Metodo auxiliar que retorna o elemento dado um indice
        apontador = self._cabeca
        i = 0
        while i != indice:
            if apontador != None:
                apontador = apontador.proximo
                i = i + 1
            else:
                raise IndexError('Indice da lista fora do intervalo.')
        return apontador

    def insereElementoInicio(self, elemento):
        #Metodo que insere um elemento no inicio
        no = No(elemento)
        if self._cabeca != None:
            apontador = self._cabeca
            self._cabeca = no
            self._cabeca.proximo = apontador
        else:
            self._cabeca = no
        self._tamanho = self._tamanho + 1
    
    def insereElementoFinal(self, elemento):
        #Metodo que insere um elemento no final
        no = No(elemento)
        if self._cabeca != None:
            apontador = self._cabeca
            while apontador.proximo != None:
                apontador = apontador.proximo
            apontador.proximo = no
        else:
            self._cabeca = no
        self._tamanho = self._tamanho + 1

    def insereElementoPorIndice(self, indice, elemento):
        #Metodo que insere um elemento pelo indice
        no = No(elemento)
        if indice < 0:
            raise IndexError('Nao e possivel inserir um elemento passando um indice negativo.')
        elif indice == 0:
            apontador = self._retornaElementoPeloIndice(indice)
            no.proximo = apontador
            self._cabeca = no
            self._tamanho = self._tamanho + 1
        elif indice < self._tamanho:
            apontador = self._retornaElementoPeloIndice(indice - 1)
            no.proximo = apontador.proximo
            apontador.proximo = no
            self._tamanho = self._tamanho + 1
        else:
            self.insereElementoFinal(elemento)

    def removeElementoInicio(self):
        #Metodo que remove o elemento que esta no inicio
        if self._tamanho != 0:
            if self._tamanho == 1:
                self._cabeca = None
            else:
                self._cabeca = self._cabeca.proximo
        else:
            raise Exception('Lista vazia.')
        self._tamanho = self._tamanho - 1
    
    def removeElementoFinal(self):
        #Metodo que remove o elemento que esta no final
        if self._tamanho != 0:
            if self._tamanho == 1:
                self._cabeca = None
            else:
                atual = self._cabeca
                while atual.proximo != None:
                    anterior = atual
                    atual = atual.proximo
                anterior.proximo = None
        else:
            raise Exception('Lista vazia.')
        self._tamanho = self._tamanho - 1
    
    def removeElementoPorIndice(self, indice):
        #Metodo que remove um elemento dado um indice e retorna o elemento removido
        if self._tamanho == 0:
            raise Exception('Lista vazia.')
        else:
            if indice < 0:
                raise IndexError('Nao e possivel remover um elemento passando um indice negativo.')
            elif indice == 0:
                apontador = self._retornaElementoPeloIndice(indice)
                self._cabeca = apontador.proximo
                self._tamanho = self._tamanho - 1
                return apontador.dado
            elif indice < self._tamanho:
                anterior = self._retornaElementoPeloIndice(indice - 1)
                atual = self._retornaElementoPeloIndice(indice)
                anterior.proximo = atual.proximo
                self._tamanho = self._tamanho - 1
                return atual.dado
            else:
                raise IndexError(f'Nao ha indice {indice} na lista.')
    
    def tamanhoLista(self):
        #Metodo que retorna o tamanho da lista
        return self._tamanho

    def estaVazia(self):
        #Metodo que verifica se a lista esta vazia
        if self._tamanho == 0:
            return True
        return False

    def estaCheia(self):
        #Metodo que verifica se a lista esta cheia
        return False
    
    def consultaElementoPorIndice(self, indice):
        #Acessa o elemento em determinada posicao
        apontador = self._retornaElementoPeloIndice(indice)
        if apontador != None:
            return apontador.dado
        else:
            raise IndexError('Indice fora do intervalo.')
    
    def alteraElementoPorIndice(self, indice, elemento):
        #Altera um valor a partir de um indice
        apontador = self._retornaElementoPeloIndice(indice)
        if apontador != None:
            apontador.dado = elemento
        else:
            raise IndexError('Indice da lista fora do intervalo.')
    
    def indiceDoElemento(self, elemento):
        #Retorna o indice do elemento passado como parametro
        apontador = self._cabeca
        indice_elemento = 0
        while apontador != None:
            if apontador.dado == elemento:
                return indice_elemento
            apontador = apontador.proximo
            indice_elemento = indice_elemento + 1
        raise ValueError(f'{elemento} nao esta na lista.')
    
    def restauraLista(self):
        #Metodo que restaura a lista
        self._cabeca = None
        self._tamanho = 0
    
    def inverteLista(self):
        #Metodo que inverte a lista original
        if self._tamanho == 0:
            raise Exception('Lista vazia.')
        inicio = 0
        final = self._tamanho - 1
        while inicio < (self._tamanho // 2):
            auxiliar = self[inicio]
            self[inicio] = self[final]
            self[final] = auxiliar
            inicio = inicio + 1
            final = final - 1
    
    def criaListaInvertida(self):
        #Metodo que cria uma lista com os elementos invertidos
        lista_invertida = ListaEncadeada()
        apontador = self._cabeca
        while apontador != None:
            lista_invertida.insereElementoInicio(apontador.dado)
            apontador = apontador.proximo
        return lista_invertida

    def criaCopiaLista(self):
        #Metodo que cria uma copia da lista sem elementos repetidos
        lista_copia = ListaEncadeada()
        apontador = self._cabeca
        while apontador != None:
            if not lista_copia.elementoContido(apontador.dado):
                lista_copia.insereElementoFinal(apontador.dado)
            apontador = apontador.proximo
        return lista_copia

    def elementoContido(self, elemento):
        #Metodo auxiliar que verifica se um elemento esta contido na lista
        apontador = self._cabeca
        while apontador != None:
            if apontador.dado == elemento:
                return True 
            apontador = apontador.proximo
        return False

    def listasIguais(self, lista, tamanho_lista):
        #Metodo que verifica se duas listas sao iguais
        if self._tamanho == tamanho_lista:
            apontador = self._cabeca
            i = 0
            while i < tamanho_lista:
                if apontador.dado == lista[i]:
                    apontador = apontador.proximo
                    i = i + 1
                else:
                    return False
        if i == self._tamanho:
            return True
        return False

    def rearranjarLista(self, n):
        inicio = 0
        proximo = 1
        if n == 2:
            auxiliar = self[inicio]
            self[inicio] = self[proximo]
            self[proximo] = auxiliar
        else:
            inicio = 1
            proximo = inicio + ((n // 2) - 1)
            while proximo != (self._tamanho - 1):
                auxiliar = self[inicio]
                self[inicio] = self[proximo]
                self[proximo] = auxiliar
                inicio = inicio + 1
                proximo = proximo + 1

    def __len__(self):
        #Metodo que retorna o tamanho da lista, exemplo: len(lista)
        return self._tamanho

    def __getitem__(self, indice):
        #Acessa o elemento em determinada posicao, exemplo: lista[indice]
        apontador = self._retornaElementoPeloIndice(indice)
        if apontador != None:
            return apontador.dado
        else:
            raise IndexError('Indice fora do intervalo.')
    
    def __setitem__(self, indice, elemento):
        #Altera um valor a partir de um indice, exemplo: lista[indice] = elemento
        apontador = self._retornaElementoPeloIndice(indice)
        if apontador != None:
            apontador.dado = elemento
        else:
            raise IndexError('Indice da lista fora do intervalo.')
    
    def __repr__(self):
        #Metodo que mostra a lista para o desenvolvedor no modo interativo do Python
        return str(self)

    def __str__(self):
        #Metodo que mostra a lista para o usuario atraves da funcao print()
        apontador = self._cabeca
        representacao = ''
        while apontador != None:
            representacao = representacao + f'{apontador.dado} '
            if apontador.proximo == None:
                break
            apontador = apontador.proximo
        return representacao

    def __del__(self):
        #Metodo destrutor
        return

