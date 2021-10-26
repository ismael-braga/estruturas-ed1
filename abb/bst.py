class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def filhoEsquerda(self):
        return self.esquerda.valor
    
    def filhoDireita(self):
        return self.direita.valor
    

class BST:
    def __init__(self):
        self._raiz = None
        self._nos = 0
        
    def inserir(self, valor):
        no = NoArvore(valor)
        if self._raiz == None:
            self._raiz = no
            self._nos = self._nos + 1
        else:
            atual = self._raiz
            pai = None
            while True:
                if atual != None:
                    pai = atual
                    if no.valor < atual.valor:
                        atual = atual.esquerda
                    else:
                        atual = atual.direita
                else:
                    if no.valor < pai.valor:
                        pai.esquerda = no
                        self._nos = self._nos + 1
                        return
                    else:
                        pai.direita = no
                        self._nos = self._nos + 1
                        return

    def inserirInverso(self, valor):
        no = NoArvore(valor)
        if self._raiz == None:
            self._raiz = no
            self._nos = self._nos + 1
        else:
            atual = self._raiz
            pai = None
            while True:
                if atual != None:
                    pai = atual
                    if no.valor < atual.valor:
                        atual = atual.direita
                    else:
                        atual = atual.esquerda
                else:
                    if no.valor < pai.valor:
                        pai.direita = no
                        self._nos = self._nos + 1
                        return
                    else:
                        pai.esquerda = no
                        self._nos = self._nos + 1
                        return

    def remover(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                if atual == self._raiz:
                    self._raiz = self._auxiliarRemocao(atual)
                    self._nos = self._nos - 1
                else:
                    if anterior.direita == atual:
                        anterior.direita = self._auxiliarRemocao(atual)
                        self._nos = self._nos - 1
                    else:
                        anterior.esquerda = self._auxiliarRemocao(atual)
                        self._nos = self._nos - 1
            anterior = atual
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
    
    def _auxiliarRemocao(self, atual):
        if atual.esquerda == None:
            no_2 = atual.direita
            return no_2
        no_1 = atual
        no_2 = atual.esquerda
        while no_2.direita != None:
            no_1 = no_2
            no_2 = no_2.direita
        if no_1 != atual:
            no_1.direita = no_2.esquerda
            no_2.esquerda = atual.esquerda
        no_2.direita = atual.direita
        return no_2

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

    def altura(self, no):
        if no == None:
            return 0
        else:
            altura_esq = self.altura(no.esquerda)
            altura_dir = self.altura(no.direita)
            if altura_esq > altura_dir:
                return altura_esq + 1
            return altura_dir + 1
    
    def balanceamento(self, raiz):
        if not raiz:
            return 0
        return self.alturaNo(raiz.esquerda) - self.alturaNo(raiz.direita)

    def arvoresIguais(self, a1_r, a2_r):
        """aão passados as raizes das arvores para a funcao"""
        if a1_r == None and a2_r == None:
            return True
        elif a1_r != None and a2_r != None:
            return ((a1_r.valor == a2_r.valor) and self.arvoresIguais(a1_r.esquerda, a2_r.esquerda) and self.arvoresIguais(a1_r.direita, a2_r.direita))
        return False

    def arvoresSimilares(self, a1_r, a2_r):
        """Sao passados as raizes das arvores para a funcao"""
        if a1_r == None and a2_r == None:
            return True
        elif a1_r != None and a2_r != None:
            if self.arvoresSimilares(a1_r.esquerda, a2_r.esquerda) and self.arvoresSimilares(a1_r.direita, a2_r.direita):
                return True
        return False
    
    def balanceamento(self, raiz):
        if not raiz:
            raise Exception('A arvore esta vazia.')
        fator_balanceamento = self.altura(raiz.esquerda) - self.altura(raiz.direita)
        if abs(fator_balanceamento) > 1:
            # nao e uma avl
            return 0
        else:
            # e uma avl
            return 1

    def verificaAVL(self, raiz):
        if not raiz:
            raise Exception('A arvore esta vazia.')
        fator_balanceamento = self.altura(raiz.esquerda) - self.altura(raiz.direita)
        if abs(fator_balanceamento) > 1:
            # nao e uma avl
            return 0
        else:
            self.preOrdem(raiz)
                

    def estritamenteBinaria(self, no):
        if no != None:
            if no.esquerda != None and no.direita != None:
                pass
            else:
                if no.esquerda == None:
                    no.esquerda.valor = no.direita.valor
                elif no.direita == None:
                    no.direita.valor = no.esquerda.valor
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)
    
    def nivel(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')

        nivel = 0
        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                break
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
            nivel = nivel + 1
        if atual == None:
            nivel = -1
            return nivel
        return nivel

    def imprimeArvorePorAltura(self, raiz):
        self.nivel(raiz)
    

    def antecessor(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')

        antecessor = None
        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                break
            if valor > atual.valor:
                antecessor = atual
                atual = atual.direita
            else:
                antecessor = atual
                atual = atual.esquerda
        return antecessor.valor

    def sucessor(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        
        sucessor_esquerda = None
        sucessor_direita = None
        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                if atual.esquerda == None:
                    sucessor_esquerda = 0
                else:
                    sucessor_esquerda = atual.esquerda.valor
                if atual.direita == None:
                    sucessor_direita = 0
                else:
                    sucessor_direita = atual.direita.valor
                break
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
        if sucessor_esquerda == None and sucessor_direita == None:
            return False
        return (sucessor_esquerda, sucessor_direita)
        

    def arvoreEspelho(self, valor):
        self.inserirInverso(valor)

    def __del__(self):
        return

