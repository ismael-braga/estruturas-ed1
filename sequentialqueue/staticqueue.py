class FilaEstatica:
    def __init__(self, maximo):
        self.maximo = maximo
        self._fila = [None] * self._maximo
        self._inicio = None
        self._final = None
        self._tamanho = 0
    
    @property
    def maximo(self):
        return self._maximo
    
    @maximo.setter
    def maximo(self, max):
        if not isinstance(max, int):
            max = int(max)
        self._maximo = max
    
    def enfileira(self, elemento):
        #Metodo que insere um elemento no final da fila
        if self._tamanho == self._maximo:
            raise Exception('A fila esta cheia.')
        if self._tamanho == 0:
            self._inicio = elemento
            self._final = elemento
        else:
            self._final = elemento
        self._fila[self._tamanho] = elemento
        self._tamanho = self._tamanho + 1

    def desenfileira(self):
        #Metodo que remove o elemento que esta no inicio da fila
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        elemento_removido = self._fila[0]
        self._fila[0] = None
        i = 0
        while i < self._tamanho:
            self._fila[i] = self._fila[i + 1]
            i = i + 1
        self._tamanho = self._tamanho - 1
        if self._tamanho != 0:
            self._inicio = self._fila[0]
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
        if self._tamanho == self._maximo:
            return True
        return False

    def primeiroElemento(self):
        #Metodo que retorna o primeiro elemento
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        return self._inicio
    
    def ultimoElemento(self):
        #Metodo que retorna o ultimo elemento
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        return self._final

    def restauraFila(self):
        #Metodo que restaura a fila
        i = 0
        while i < self._tamanho:
            self._fila[i] = None
            i = i + 1
        self._tamanho = 0
    
    def inverteFila(self):
        #Metodo que inverte a fila original
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        inicio = 0
        final = self._tamanho - 1
        while inicio < (self._tamanho // 2):
            auxiliar = self._fila[inicio]
            self._fila[inicio] = self._fila[final]
            self._fila[final] = auxiliar
            inicio = inicio + 1
            final = final - 1

    def criaFilaInvertida(self):
        #Metodo que cria uma fila invertida
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        fila_invertida = FilaEstatica(self._maximo)
        final = self._tamanho - 1
        while final >= 0:
            fila_invertida.enfileira(self._fila[final])
            final = final - 1
        return fila_invertida
    
    def criaCopiaFila(self):
        #Metodo que cria uma copia da fila
        if self._tamanho == 0:
            raise Exception('A fila esta vazia.')
        fila_copia = FilaEstatica(self._maximo)
        i = 0
        while i < self._tamanho:
            fila_copia.enfileira(self._fila[i])
            i = i + 1
        return fila_copia        

    def filasIguais(self, fila, tamanho_fila):
        #Metodo que verifica se duas filas sao iguais
        if self._tamanho == tamanho_fila:
            i = 0
            while i < tamanho_fila:
                if self._fila[i] == fila[i]:
                    i = i + 1
                else:
                    return False
        if i == self._tamanho:
            return True
        return False

    def concatenaFilas(self, f2):
        #Metodo que concatena duas filas
        i = 0
        while i < f2._tamanho:
            self.enfileira(f2[i])
            i = i + 1
        f2.restauraFila()
    
    def trataIndice(self, indice):
        #Metodo auxiliar que trata o indice
        if indice < 0 or abs(indice) >= self._tamanho:
            raise IndexError('Indice fora do intervalo.')
        return indice

    def __len__(self):
        #Metodo que retorna o tamanho da fila, exemplo: len(fila)
        return self._tamanho

    def __getitem__(self, indice):
        #Acessa o elemento em determinada posicao, exemplo: fila[indice]
        indice = self.trataIndice(indice)
        return self._fila[indice]
	
    def __setitem__(self, indice, elemento):
        #Altera um valor a partir de um indice, exemplo fila[indice] = elemento
        indice = self.trataIndice(indice)
        self._fila[indice] = elemento

    def __repr__(self):
        #Metodo que mostra a fila para o desenvolvedor no modo interativo do Python
        return str(self)

    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        representacao = ''
        for i in range(0, self._tamanho):
            representacao = representacao + f'{self._fila[i]} '
        return representacao

    """
    def __str__(self):
        #Metodo que mostra a fila para o usuario atraves da funcao print()
        if self._tamanho < 100:
            elementos = '\033[1;32m' + f'{self._tamanho}' + '\033[0;0m'
        else:
            elementos = '\033[1;31m' + f'{self._tamanho}' + '\033[0;0m'
        max = '\033[1;31m' + f'{self._maximo}' + '\033[0;0m'
        representacao = f'Fila[{elementos}/{max}] = '
        representacao = representacao + f'{[self._fila[i] for i in range(0, self._tamanho)]}'
        return representacao
    """

    def __del__(self):
        #Metodo destrutor
        return
