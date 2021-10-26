from typing import List
from itemhash import ItemHash
from linkedlist.linkedlist import ListaEncadeada

class TabelaHash:
    def __init__(self, tamanho=101):
        self._tamanho = tamanho
        self._tabela = [None] * self._tamanho
        self._quantidade_elementos = 0

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tam):
        if not isinstance(tam, int):
            tam = int(tam)
        self._tamanho = tam
     
    def _metodoDoResto(self, chave):
        # Funcao de hashing do metodo do resto
        espalhamento = (chave & 0x7FFFFFFF) % self._tamanho
        return espalhamento

    def _hashStrings(self, chave):
        # Funcao de hashing utilizada com strings
        soma = 0
        inicio = 0
        final = len(chave)
        while inicio < final:
            valor = ord(chave[inicio]) * (inicio + 1)
            soma = soma + valor
            inicio = inicio + 1
        indice = soma % self._tamanho
        return indice

    def _hashFolding(self, chave):
        # Funcao de hashing que divide a chave em tamanhos iguais (o ultimo pedaco possa ser que nao seja igual)
        chave = str(chave)
        parcela = ''
        inicio = 0
        final = len(chave)
        temporaria = 0
        while inicio < final:
            parcela = parcela + chave[inicio]
            if len(parcela) == 2 or inicio == (final - 1):
                parcela = int(parcela)
                temporaria = temporaria + parcela
                parcela = ''
            inicio = inicio + 1
        indice = temporaria % self._tamanho
        return indice

    def _hashQuadradoDoMeio(self, chave):
        # Funcao de hashing que eleva o item ao quadrado e depois extrai uma parte dos dígitos resultantes
        chave = chave ** 2
        chave = str(chave)
        inicio = (len(chave) - 1) // 2
        final = len(chave) - 1
        temporaria = ''
        while inicio < final:
            temporaria = temporaria + chave[inicio]
            inicio = inicio + 1
        temporaria = int(temporaria)
        indice = temporaria % self._tamanho
        return indice

    # Insercao e Busca utilizando Enderecamento Encadeado
    def inserirElemento(self, chave, valor):
        elemento = ItemHash(chave, valor)
        indice = self._metodoDoResto(chave)
        #indice = self._hashStrings(chave)
        if self._tabela[indice] == None:
            lista = ListaEncadeada()
            self._tabela[indice] = lista
            lista.insereElementoFinal(elemento)
        else:
            self._tabela[indice].insereElementoFinal(elemento)
        self._quantidade_elementos = self._quantidade_elementos + 1

    def buscarElemento(self, chave):
        indice = self._metodoDoResto(chave)
        #indice = self._hashStrings(chave)
        if self._tabela[indice] == None:
            return None
        else:
            apontador = self._tabela[indice]._cabeca
            while apontador != None:
                if apontador.dado.chave == chave:
                    valor = apontador.dado.valor
                if apontador.proximo == None:
                    break
                apontador = apontador.proximo
            return valor
            '''
            representacao = ''
            while apontador != None:
                if apontador.proximo == None:
                    representacao = representacao + f'{apontador.dado.valor}'
                    break
                else:
                    representacao = representacao + f'{apontador.dado.valor} -> '
                apontador = apontador.proximo
            return representacao
            '''

    def restauraTabelaHash(self):
        # Metodo que restaura a Tabela Hash
        self._tabela = [None] * self._tamanho
        self._quantidade_elementos = 0
    
    def __setitem__(self, chave, valor):
        # Metodo que permite utilizar tabela_hash[chave] = valor, serve para inserir elemento na tabela
        self.inserirElemento(chave, valor)

    def __getitem__(self, chave):
        # Metodo que permite utilizar tabela_hash[chave] e é retornado o valor
        return self.buscarElemento(chave)

    def __len__(self):
        # Metodo que retorna o tamanho da tabela através do len(tabela_hash)
        return self._quantidade_elementos

    def __repr__(self):
        # Metodo que mostra a tabela hash para o desenvolvedor no modo interativo do Python
        return str(self)
    
    def __str__(self):
        # Metodo que mostra a tabela hash para o usuário através da função print()
        representacao = ''
        for indice in range(0, self._tamanho):
            representacao = representacao + f'{indice}: '
            if self._tabela[indice] != None:
                apontador = self._tabela[indice]._cabeca
                while apontador != None:
                    representacao = representacao + f'{apontador.dado.chave} '
                    if apontador.proximo == None:
                        break
                    apontador = apontador.proximo
            representacao = representacao + '\n'
        return representacao        

    def __del__(self):
        return

