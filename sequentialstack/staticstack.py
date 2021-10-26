from sequentiallist.lista_estatica import ListaEstatica

class PilhaEstatica:
    def __init__(self, maximo):
        self.maximo = maximo
        self._pilha = [None] * self._maximo
        self._topo = None
        self._tamanho = 0
    
    @property
    def maximo(self):
        return self._maximo
    
    @maximo.setter
    def maximo(self, max):
        if not isinstance(max, int):
            max = int(max)
        self._maximo = max
    
    def empilha(self, elemento):
        #Metodo que insere um elemento no topo da pilha
        if self._tamanho == self._maximo:
            raise Exception('Pilha cheia.')
        self._pilha[self._tamanho] = elemento
        self._topo = elemento
        self._tamanho = self._tamanho + 1

    def desempilha(self):
        #Metodo que remove um elemento do topo da pilha
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        indice = self._tamanho - 1
        elemento_removido = self.topo()
        self._pilha[indice] = None
        indice = indice - 1
        self._topo = self._pilha[indice]
        self._tamanho = self._tamanho - 1
        return elemento_removido

    def topo(self):
        #Metodo que retorna o elemento que esta no topo da pilha
        if self._tamanho == 0:
            raise Exception('Pilha vazia.')
        return self._topo

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
        if self._tamanho == self._maximo:
            return True
        return False

    def __len__(self):
        #Metodo que retorna o tamanho da pilha, exemplo: len(pilha)
        return self._tamanho

    def __getitem__(self, indice):
        #Metodo auxiliar utilizado nas funcao da pilha: desempilha()
        #Exemplo: pilha[indice]
        return self._pilha[indice]
	
    def __setitem__(self, indice, elemento):
        #Metodo auxiliar utilizado nas funcoes da pilha: empilha(), desempilha()
        #Exemplo: pilha[indice] = elemento
        self._pilha[indice] = elemento

    def __repr__(self):
        #Metodo que mostra a pilha para o desenvolvedor no modo interativo do Python
        return str(self)

    def __str__(self):
        #Metodo que mostra a pilha para o usuario atraves da funcao print()
        representacao = ''
        for i in range((self._tamanho - 1), -1, - 1):
            representacao = representacao + f'{self._pilha[i]} '
        return representacao

    def __del__(self):
        #Metodo destrutor
        return
