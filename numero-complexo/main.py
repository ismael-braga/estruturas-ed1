import opncomplexo as opnc 

# Criando o primeiro número complexo
z1 = opnc.criar_complexo(4, 3)
# Criando o segundo número complexo
z2 = opnc.criar_complexo(2, 6)
# Multiplicando z1 e z2
print(f'z1 x z2 = {opnc.mostra_complexo(opnc.multiplicar_complexos(z1, z2))}')

# Criando o terceiro número complexo
z3 = opnc.criar_complexo(10, -3)
# Criando o quarto número complexo
z4 = opnc.criar_complexo(2, 4)
# Dividindo z3 e z4
print(f'z3 / z4 = {opnc.mostra_complexo(opnc.dividir_complexos(z3, z4))}')

# Conjugado de z1, caso em que o valor imaginário é positivo
print(f'Conjugado de z1 = {opnc.mostra_complexo(opnc.conjugado_complexo(z1))}')
# Conjugado de z3, caso em que o valor imaginário é negativo
print(f'Conjugado de z3 = {opnc.mostra_complexo(opnc.conjugado_complexo(z3))}')
