import operacoes as op 

z1 = op.criar_complexo(5, 1)
z2 = op.criar_complexo(2, -1)
print(op.multiplicar_complexos(z1, z2))

print(op.conjugado_complexo(z2))

z3 = op.criar_complexo(1, 1)
z4 = op.criar_complexo(1, 2)
print(op.dividir_complexos(z3, z4))
