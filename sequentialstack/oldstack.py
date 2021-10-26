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
        """Método que insere um elemento no topo da pilha"""
        if self._tamanho == self._maximo:
            raise Exception('A pilha está cheia.')
        self._pilha[self._tamanho] = elemento
        self._topo = elemento
        self._tamanho = self._tamanho + 1

    def desempilha(self):
        """Método que remove um elemento do topo da pilha"""
        if self._tamanho == 0:
            raise Exception('A pilha está vazia.')
        indice = self._tamanho - 1
        elemento_removido = self.topo()
        self._pilha[indice] = None
        indice = indice - 1
        self._topo = self._pilha[indice]
        self._tamanho = self._tamanho - 1
        return elemento_removido

    def topo(self):
        """Método que retorna o elemento que está no topo da pilha"""
        if self._tamanho == 0:
            raise Exception('A pilha está vazia.')
        return self._topo

    def tamanhoPilha(self):
        """Método que retorna o tamanho da pilha"""
        return self._tamanho

    def estaVazia(self):
        """Método que verifica se a pilha está vazia"""
        if self._tamanho == 0:
            return True
        return False
    
    def estaCheia(self):
        """Método que verifica se a pilha está cheia"""
        if self._tamanho == self._maximo:
            return True
        return False

    def restauraPilha(self):
        """Método que restaura a pilha"""
        indice = self._tamanho - 1
        while indice >= 0:
            self._topo = None 
            self._topo = self._pilha[indice]
            indice = indice - 1
        self._tamanho = 0
    
    def invertePilha(self):
        """Método que inverte a pilha"""
        if self._tamanho == 0:
            raise Exception('A pilha está vazia.')
        p1 = PilhaEstatica(self.maximo)
        p2 = PilhaEstatica(self.maximo)
        indice = self._tamanho - 1
        while indice >= 0 and self.tamanhoPilha() != 0:
            p1.empilha(self.desempilha())
            indice = indice - 1
        
        indice = p1._tamanho - 1
        while indice >= 0 and p1.tamanhoPilha() != 0:
            p2.empilha(p1.desempilha())
            indice = indice - 1
        
        indice = p2._tamanho - 1
        while indice >= 0 and p2.tamanhoPilha() != 0:
            self.empilha(p2.desempilha())
            indice - 1

    def pilhasIguais(self, p, tamanho_pilha):
        """Método que verifica se duas pilhas são iguais"""
        indice = self._tamanho - 1
        contador = 0
        p1 = self._pilha[indice]
        p2 = p._pilha[indice]
        if self._tamanho == tamanho_pilha:
            while indice >= 0:
                if p1 == p2:
                    indice = indice - 1
                    contador = contador + 1
                else:
                    break
        if contador == self._tamanho:
            return 'Sim'
        return 'Não'

    def verificaParentizacao(self, elemento):
        auxiliar = PilhaEstatica(self.maximo)
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
        """Método que ordena uma lista utilizando duas pilhas"""
        p1 = PilhaEstatica(self.maximo)
        p2 = PilhaEstatica(self.maximo)
        indice = 0
        while indice < len(lista):
            elemento = lista[indice]
            if indice == 0:
                p1.empilha(elemento)
            else:
                if elemento <= p1.topo():
                    p1.empilha(elemento)
                else:
                    i = p1.tamanhoPilha() - 1
                    while i >= 0:
                        if elemento > p1._topo:
                            p2.empilha(p1.desempilha())
                            i = i - 1
                            p1._topo = p1._pilha[i]
                        else:
                            break
                    p1.empilha(elemento)
                    i = p2.tamanhoPilha() - 1
                    while i >= 0:
                        p1.empilha(p2.desempilha())
                        i = i - 1
            indice = indice + 1
        return p1
  
    def __len__(self):
        """Método que retorna o tamanho da pilha, exemplo: len(pilha)"""
        return self._tamanho

    def __getitem__(self, indice):
        """
        Método auxiliar utilizado nas funções da pilha: desempilha(), restauraPilha()
        Exemplo: pilha[indice]
        """
        return self._pilha[indice]
	
    def __setitem__(self, indice, elemento):
        """
        Método auxiliar utilizado nas funções da pilha: empilha(), desempilha()
        Exemplo: pilha[indice] = elemento
        """
        self._pilha[indice] = elemento

    def __repr__(self):
        """Método que mostra a pilha para o desenvolvedor no modo interativo do Python"""
        return str(self)

    def __str__(self):
        """Método que mostra a pilha para o usuário através da função print()"""
        representacao = ''
        for i in range((self._tamanho - 1), -1, - 1):
            representacao = representacao + f'{self._pilha[i]} '
        return representacao

    def __del__(self):
        """Método destrutor"""
        return
