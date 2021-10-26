def criar_matriz(n, m):
    matriz = []
    auxiliar = []
    for linha in range(n):
        for coluna in range(m):
            auxiliar.append(int(input(f'M[{linha+1}][{coluna+1}]: ')))
        matriz.append(auxiliar[:])
        auxiliar.clear()
    return matriz

def somar_matrizes(primeira_matriz, segunda_matriz):
    matriz_resultante = []
    auxiliar = []
    if (len(primeira_matriz) != len(segunda_matriz) or len(primeira_matriz[0]) != len(segunda_matriz[0])):
        print('Não é possível somar as matrizes, pois possuem tamanhos diferentes.')
    else:
        for linha in range(len(primeira_matriz)):
            for coluna in range(len(primeira_matriz[0])):
                auxiliar.append(primeira_matriz[linha][coluna] + segunda_matriz[linha][coluna])
            matriz_resultante.append(auxiliar[:])
            auxiliar.clear()
        return matriz_resultante

def subtrair_matrizes(primeira_matriz, segunda_matriz):
    matriz_resultante = []
    auxiliar = []
    if (len(primeira_matriz) != len(segunda_matriz) or len(primeira_matriz[0]) != len(segunda_matriz[0])):
        print('Não é possível subtrair as matrizes, pois possuem tamanhos diferentes.')
    else:
        for linha in range(len(primeira_matriz)):
            for coluna in range(len(primeira_matriz[0])):
                auxiliar.append(primeira_matriz[linha][coluna] - segunda_matriz[linha][coluna])
            matriz_resultante.append(auxiliar[:])
            auxiliar.clear()
        return matriz_resultante

def quantidade_linhas_matriz(matriz):
    return len(matriz)

def quantidade_colunas_matriz(matriz):
    return len(matriz[0])
