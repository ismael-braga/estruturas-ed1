from op_ncomplexo import Complexo

z1 = Complexo()
# Criando o primeiro número complexo
z1.criar_complexo(4, 3)
z2 = Complexo()
# Criando o segundo número complexo
z2.criar_complexo(2, 6)
# Multiplicando z1 e z2
print(f'z1 x z2 = {z1.multiplicar_complexos(z1, z2)}')
