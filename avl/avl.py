from no import No

class AVL:
    def __init__(self):
        self._nos = 0

    def inserir(self, raiz, valor):
        no = No(valor)
        if not raiz:
            self._nos = self._nos + 1
            return no
        elif valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)
        raiz.altura = max(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        fator_balanceamento = self.balanceamento(raiz)
        if fator_balanceamento > 1:
            if valor < raiz.esquerda.valor:
                return self.rotacaoLL(raiz)
            else:
                raiz.esquerda = self.rotacaoRR(raiz.esquerda)
                return self.rotacaoLL(raiz)
        if fator_balanceamento < -1:
            if valor > raiz.direita.valor:
                return self.rotacaoRR(raiz)
            else:
                raiz.direita = self.rotacaoLL(raiz.direita)
                return self.rotacaoRR(raiz)
        return raiz
    

    def remover(self, raiz, valor):
        if not raiz:
            return raiz
        elif valor < raiz.valor:
            raiz.esquerda = self.remover(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)
        else:
            if raiz.esquerda is None:
                auxiliar = raiz.direita
                raiz = None
                self._nos = self._nos - 1
                return auxiliar
            elif raiz.direita is None:
                auxiliar = raiz.esquerda
                raiz = None
                self._nos = self._nos - 1
                return auxiliar
            auxiliar = self.menorValorNo(raiz.direita)
            raiz.valor = auxiliar.valor
            raiz.direita = self.remover(raiz.direita, auxiliar.valor)
        if raiz is None:
            return raiz
        raiz.altura = max(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        fator_balanceamento = self.balanceamento(raiz)
        if fator_balanceamento > 1:
            if self.balanceamento(raiz.esquerda) >= 0:
                return self.rotacaoLL(raiz)
            else:
                # rotacaoLR
                raiz.esquerda = self.rotacaoRR(raiz.esquerda)
                return self.rotacaoLL(raiz)
        if fator_balanceamento < -1:
            if self.balanceamento(raiz.direita) <= 0:
                return self.rotacaoRR(raiz)
            else:
                # rotacaoRL
                raiz.direita = self.rotacaoLL(raiz.direita)
                return self.rotacaoRR(raiz)
        return raiz

    def busca(self, raiz, valor):
        if self.quantidadeNos() == 0:
            raise Exception('A arvore esta vazia.')
        atual = raiz
        while atual != None:
            if valor == atual.valor:
                return True
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
        return False

    def quantidadeNos(self):
        return self._nos

    def rotacaoRR(self, raiz):
        no = raiz.direita
        auxiliar = no.esquerda
        no.esquerda = raiz
        raiz.direita = auxiliar
        raiz.altura = max(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        no.altura = max(self.alturaNo(no.esquerda), self.alturaNo(no.direita)) + 1
        return no

    def rotacaoLL(self, raiz):
        no = raiz.esquerda
        auxiliar = no.direita
        no.direita = raiz
        raiz.esquerda = auxiliar
        raiz.altura = max(self.alturaNo(raiz.esquerda), self.alturaNo(raiz.direita)) + 1
        no.altura = max(self.alturaNo(no.esquerda), self.alturaNo(no.direita)) + 1
        return no

    def alturaNo(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def balanceamento(self, raiz):
        if not raiz:
            return 0
        return self.alturaNo(raiz.esquerda) - self.alturaNo(raiz.direita)

    def menorValorNo(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.menorValorNo(raiz.esquerda)

    def preOrdem(self, no):
        if not no:
            return
        print(no.valor)
        self.preOrdem(no.esquerda)
        self.preOrdem(no.direita)
    
    def Ordem(self, no):
        if not no:
            return
        self.Ordem(no.esquerda)
        print(no.valor)
        self.Ordem(no.direita)
    
    def posOrdem(self, no):
        if not no:
            return
        self.posOrdem(no.esquerda)
        self.posOrdem(no.direita)
        print(no.valor)

    def altura(self, no):
        if no == None:
            return 0
        else:
            altura_esq = self.altura(no.esquerda)
            altura_dir = self.altura(no.direita)
            if altura_esq > altura_dir:
                return altura_esq + 1
            return altura_dir + 1

    def __del__(self):
        return

avl = AVL()
raiz = None

insercao = [60, 45, 42, 83, 69, 58, 70, 55, 39,71]
for i in range(len(insercao)):
    raiz = avl.inserir(raiz, insercao[i])

remocao = [45, 83, 39, 60]
for r in range(len(remocao)):
    raiz = avl.remover(raiz, remocao[r])


insercao = [77, 85, 44, 83, 11, 20]
for i in range(len(insercao)):
    raiz = avl.inserir(raiz, insercao[i])

avl.posOrdem(raiz)
