class ListaEstatica:
	def __init__(self, maximo):
		self.maximo = maximo
		self._lista = [None] * self._maximo
		self._tamanho = 0

	@property
	def maximo(self):
		return self._maximo

	@maximo.setter
	def maximo(self, max):
		if not isinstance(max, int):
			max = int(max)
		self._maximo = max
	
	def estaVazia(self):
		if self._tamanho == 0:
			return True
		return False

	def estaCheia(self):
		if self._tamanho == self._maximo:
			return True
		return False

	def tamanhoLista(self):
		return self._tamanho
		
	def insereElementoInicio(self, elemento):
		if self._tamanho == self._maximo:
			return False
		if self._tamanho == 0 or self._lista[0] == None:
			self._lista[0] = elemento
		else:
			i = self._tamanho
			while i >= 0:
				self._lista[i+1] = self._lista[i]
				i = i - 1
			self._lista[0] = elemento
		self._tamanho = self._tamanho + 1
	
	def insereElementoFinal(self, elemento):
		if self._tamanho == self._maximo:
			return False
		self._lista[self._tamanho] = elemento
		self._tamanho = self._tamanho + 1
	
	def insereElementoPorIndice(self, indice, elemento):
		if self._tamanho == self._maximo:
			raise Exception('Lista cheia.')
		if indice < 0:
			raise IndexError('Nao e possivel inserir um elemento passando um indice negativo.')
		if indice < self._tamanho:
			i = self._tamanho
			while i >= indice:
				self._lista[i] = self._lista[i - 1]
				i = i - 1
			self._lista[indice] = elemento
			self._tamanho = self._tamanho + 1
		else:
			self.insereElementoFinal(elemento)

	def removeElementoFinal(self):
		if self._tamanho == 0:
			return False
		self._lista[self._tamanho - 1] = None
		self._tamanho = self._tamanho - 1

	def removeElementoInicio(self):
		if self._tamanho == 0:
			return False
		self._lista[0] = None
		i = 0
		while i < self._tamanho:
			self._lista[i] = self._lista[i+1]
			i = i + 1
		self._tamanho = self._tamanho - 1

	def removeElementoPorIndice(self, indice):
		if self._tamanho == 0:
			raise Exception('Lista vazia.')
		if indice < 0:
			raise IndexError('Nao e possivel remover um elemento passando um indice negativo.')
		elif indice == 0:
			self.removeElementoInicio()
		elif indice == (self._tamanho - 1):
			self._lista[self._tamanho - 1] = None
			self._tamanho = self._tamanho - 1
		elif indice < self._tamanho:
			i = 0
			while i < self._tamanho and i != indice:
				i = i + 1
			if i == self._tamanho:
				raise IndexError('Indice da lista fora do intervalo.')
			k = i
			while k < self._tamanho:
				self._lista[k] = self._lista[k + 1]
				k = k + 1
			self._tamanho = self._tamanho - 1
		else:
			raise IndexError(f'Nao ha indice {indice} na lista.')
		
	"""
	def removeElementoPorValor(self, valor=None):
		if self._tamanho == 0:
			return False
		if valor == None:
			return Exception('O valor deve seguir a seguinte regra: 0 <= valor < tamanho da lista')
		i = 0
		while i < self._tamanho and self._lista[i] != valor:
			i = i + 1
		if i == self._tamanho:
			return 0
		k = i
		while k < self._tamanho:
			self._lista[k] = self._lista[k+1]
			k = k + 1
		self._tamanho = self._tamanho - 1
	"""

	def indice(self, elemento):
		if self._tamanho == 0:
			return False 
		i = 0
		while i < self._tamanho:
			if self._lista[i] == elemento:
				break
			i = i + 1
		if i == self._tamanho:
			raise ValueError(f'{elemento} nao esta na lista.')
		return i

	def nVezes(self, elemento):
		aparicoes = 0
		for i in range(self._tamanho):
			if self._lista[i] == elemento:
				aparicoes = aparicoes + 1
		return aparicoes

	def restauraLista(self):
		i = 0
		while i < self._tamanho:
			self._lista[i] = None
			i = i + 1
		self._tamanho = 0

	def inverteLista(self):
		if self._tamanho == 0:
			raise Exception('A lista esta vazia.')
		inicio = 0 
		final = self._tamanho - 1
		while inicio < (self._tamanho // 2):
			auxiliar = self._lista[inicio]
			self._lista[inicio] = self._lista[final]
			self._lista[final] = auxiliar
			inicio = inicio + 1
			final = final - 1

	def criaListaInvertida(self):
		if self._tamanho == 0:
			raise Exception('Lista vazia.')
		lista_invertida = ListaEstatica(self._maximo)
		i = self._tamanho - 1
		while i >= 0:
			lista_invertida.insereElementoFinal(self._lista[i]) 
			i = i - 1
		return lista_invertida
	
	def elementoContido(self, elemento):
		i = 0
		while i < self._tamanho:
			if self._lista[i] == elemento:
				return True
			i = i + 1
		return False

	def criaCopiaLista(self):
		if self._tamanho == 0:
			raise Exception('Lista vazia.')
		copia_lista = ListaEstatica(self._maximo)
		i = 0
		while i < self._tamanho:
			if copia_lista.elementoContido(self._lista[i]):
				pass
			else:
				copia_lista.insereElementoFinal(self._lista[i])
			i = i + 1
		return copia_lista

	def listasIguais(self, lista, tamanho_lista):
		if self._tamanho == tamanho_lista:
			i = 0 
			while i < tamanho_lista:
				if self._lista[i] == lista[i]:
					i = i + 1
				else:
					return False
		if i == self._tamanho:
			return True
		return False
		
	def trataIndice(self, indice):
		if indice < 0 or abs(indice) >= self._tamanho:
			raise IndexError('Indice fora do intervalo.')
		return indice

	def __getitem__(self, indice):
		indice = self.trataIndice(indice)
		return self._lista[indice]
	
	def __setitem__(self, indice, elemento):
		indice = self.trataIndice(indice)
		self._lista[indice] = elemento

	def __len__(self):
		return self._tamanho

	def __repr__(self):
		return str(self)

	def __str__(self):
		representacao = ''
		for i in range(0, self._tamanho):
			representacao = representacao + f'{self._lista[i]} '
		return representacao

	"""
	def __str__(self):
		if self._tamanho < 100:
			elementos = '\033[1;32m' + f'{self._tamanho}' + '\033[0;0m'
		else:
			elementos = '\033[1;31m' + f'{self._tamanho}' + '\033[0;0m'
		max = '\033[1;31m' + f'{self._maximo}' + '\033[0;0m'
		representacao = f'Lista[{elementos}/{max}] = '
		representacao = representacao + f'{[self._lista[i] for i in range(0, self._tamanho)]}'
		return representacao
	"""

	def __del__(self):
		#Metodo destrutor
		return
