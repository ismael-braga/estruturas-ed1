import opmatriz as opm 

a = opm.criar_matriz(2, 3)
print(f'Matriz A: {a}')
b = opm.criar_matriz(2, 3)
print(f'Matriz B: {b}')

soma = opm.somar_matrizes(a, b)
print(f'A soma entre as matrizes {a} e {b} resulta na matriz {soma}')
subtracao = opm.subtrair_matrizes(a, b)
print(f'A subtração entre as matrizes {a} e {b} resulta na matriz {subtracao}')
# Quantidade de linhas da matriz A
qtd_linhas_matriz_a = opm.quantidade_linhas_matriz(a)
print(f'A matriz {a} possui {qtd_linhas_matriz_a} linhas.')
# Quantidade de colunas da matriz B
qtd_colunas_matriz_a = opm.quantidade_colunas_matriz(b)
print(f'A matriz {b} possui {qtd_colunas_matriz_a} colunas.')
