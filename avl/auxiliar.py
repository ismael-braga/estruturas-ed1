from no import No

class AVL:
    def __init__(self):
        self._raiz = None
        self._nos = 0
    
    
    def inserir(self, raiz, valor):
        no = No(valor)
        if self._raiz == None:
            self._raiz = no
            raiz = self._raiz
        atual = raiz
        auxiliar = None
        if valor < atual.valor:
            auxiliar = self.inserir(atual.esquerda, valor)
            if auxiliar:
                if self.fatorBalanceamento(atual) >= 2:
                    if valor < raiz.esquerda.valor:
                        self.rotacaoLL(raiz)
                    else:
                        self.rotacaoLR(raiz)
        else:
            if valor > atual.valor:
                auxiliar = self.inserir(atual.direita, valor)
                if auxiliar:
                    if self.fatorBalanceamento(atual) >= 2:
                        if raiz.direita.valor < valor:
                            self.rotacaoRR(raiz)
                        else:
                            self.rotacaoRL(raiz)
            else:
                print('Valor duplicado.')
        atual.altura = self.maior(self.alturaNo(atual.esquerda), self.alturaNo(atual.direita)) + 1
        return auxiliar
    
    '''
    def inserir(self, valor):
        no = No(valor)
        if self._raiz == None:
            self._raiz = no
        atual = self._raiz
        auxiliar = None
        if valor < atual.valor:
            auxiliar = self.inserir(atual.esquerda, valor)
            if auxiliar:
                if self.fatorBalanceamento(atual) >= 2:
                    if valor < self._raiz.esquerda.valor:
                        self.rotacaoLL(self._raiz)
                    else:
                        self.rotacaoLR(self._raiz)
        else:
            if valor > atual.valor:
                auxiliar = self.inserir(atual.direita, valor)
                if auxiliar:
                    if self.fatorBalanceamento(atual) >= 2:
                        if self._raiz.direita.valor < valor:
                            self.rotacaoRR(self._raiz)
                        else:
                            self.rotacaoRL(self._raiz)
            else:
                print('Valor duplicado.')
        atual.altura = self.maior(self.alturaNo(atual.esquerda), self.alturaNo(atual.direita)) + 1
        return auxiliar
    '''

    def _auxiliarRemocao(self, atual):
        """Funcao auxiliar no caso da remoção de um no que possui 2 filhos"""
        no_1 = atual
        no_2 = atual.esquerda
        while no_2 != None:
            no_1 = no_2
            no_2 = no_2.esquerda
        return no_1

    '''
    def remover(self, raiz, valor):
        if raiz == None:
            raise Exception('A arvore esta vazia.')
        if valor < raiz.valor:
            auxiliar = self.remover(raiz.esquerda, valor)
            if auxiliar:
                if self.fatorBalanceamento(raiz) >= 2:
                    if self.alturaNo(raiz.direita.esquerda) <= self.alturaNo(raiz.direita.direita):
                        self.rotacaoRR(raiz)
                    else:
                        self.rotacaoRL(raiz)
        if raiz.valor < valor:
            auxiliar = self.remover(raiz.direita, valor)
            if auxiliar:
                if self.fatorBalanceamento(raiz) >= 2:
                    if self.alturaNo(raiz.esquerda.direita) <= self.alturaNo(raiz.esquerda.esquerda):
                        self.rotacaoLL(raiz)
                    else:
                        self.rotacaoLR(raiz)
        if raiz.valor == valor:
            if raiz.esquerda == None or raiz.direita == None:
                antigo = raiz
                if raiz.esquerda != None:
                    raiz = raiz.esquerda
                else:
                    raiz = raiz.direita
            else:
                temporario = self._auxiliarRemocao(raiz.direita)
                raiz.valor = temporario.valor
                self.remover(raiz.direita, raiz.valor)
                if self.fatorBalanceamento(raiz) >= 2:
                    if self.alturaNo(raiz.esquerda.direita) <= self.alturaNo(raiz.esquerda.esquerda):
                        self.rotacaoLL(raiz)
                    else:
                        self.rotacaoLR(raiz)
            return 1
        return auxiliar
    '''

    def remover(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if valor < self._raiz.valor:
            auxiliar = self.remover(self._raiz.esquerda, valor)
            if auxiliar:
                if self.fatorBalanceamento(self._raiz) >= 2:
                    if self.alturaNo(self._raiz.direita.esquerda) <= self.alturaNo(self._raiz.direita.direita):
                        self.rotacaoRR(self._raiz)
                    else:
                        self.rotacaoRL(self._raiz)
        if self._raiz.valor < valor:
            auxiliar = self.remover(self._raiz.direita, valor)
            if auxiliar:
                if self.fatorBalanceamento(self._raiz) >= 2:
                    if self.alturaNo(self._raiz.esquerda.direita) <= self.alturaNo(self._raiz.esquerda.esquerda):
                        self.rotacaoLL(self._raiz)
                    else:
                        self.rotacaoLR(self._raiz)
        if self._raiz.valor == valor:
            if self._raiz.esquerda == None or self._raiz.direita == None:
                antigo = self._raiz
                if self._raiz.esquerda != None:
                    raiz = self._raiz.esquerda
                else:
                    raiz = self._raiz.direita
            else:
                temporario = self._auxiliarRemocao(self._raiz.direita)
                self._raiz.valor = temporario.valor
                self.remover(self._raiz.direita, self._raiz.valor)
                if self.fatorBalanceamento(self._raiz) >= 2:
                    if self.alturaNo(self._raiz.esquerda.direita) <= self.alturaNo(self._raiz.esquerda.esquerda):
                        self.rotacaoLL(self._raiz)
                    else:
                        self.rotacaoLR(self._raiz)
            return 1
        return auxiliar

    def busca(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')

        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                return True
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
        return False

    def preOrdem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)
    
    def Ordem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            self.Ordem(no.esquerda)
            print(no.valor)
            self.Ordem(no.direita)

    def posOrdem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            self.posOrdem(no.esquerda)
            self.posOrdem(no.direita)
            print(no.valor)

    def restauraABB(self):
        self._raiz = None
        self._nos = 0

    def obterRaiz(self):
        return self._raiz

    def quantidadeNos(self):
        return self._nos

    def alturaNo(self, no):
        if no == None:
            return -1
        return no.altura
    
    def fatorBalanceamento(self, no):
        return (self.alturaNo(no.esquerda) - self.alturaNo(no.direita))

    def maior(self, v1, v2):
        if v1 > v2:
            return v1
        return v2

    def altura(self, no):
        if no == None:
            return 0
        else:
            altura_esq = self.altura(no.esquerda)
            altura_dir = self.altura(no.direita)
            if altura_esq > altura_dir:
                return altura_esq + 1
            return altura_dir + 1
    
    def rotacaoLL(self, raiz):
        no = raiz.esquerda
        raiz.esquerda = no.direita
        no.direita = raiz
        raiz.altura = self.maior(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        no.altura = self.maior(self.alturaNo(no.esquerda), raiz.altura) + 1
        raiz = no
    
    def rotacaoRR(self, raiz):
        no = raiz.direita
        raiz.direita = no.esquerda
        no.esquerda = raiz
        raiz.altura = self.maior(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        no.altura = self.maior(self.alturaNo(no.direita), raiz.altura) + 1
        raiz = no
    
    def rotacaoLR(self, raiz):
        self.rotacaoRR(raiz.esquerda)
        self.rotacaoLL(raiz)

    def rotacaoRL(self, raiz):
        self.rotacaoLL(raiz.direita)
        self.rotacaoRR(raiz)
    
    def arvoresIguais(self, a1_r, a2_r):
        """Sao passados as raizes das arvores para a funcao"""
        if a1_r == None and a2_r == None:
            return True
        elif a1_r != None and a2_r != None:
            return ((a1_r.valor == a2_r.valor) and self.arvoresIguais(a1_r.esquerda, a2_r.esquerda) and self.arvoresIguais(a1_r.direita, a2_r.direita))
        return False

    def __del__(self):
        return
    
