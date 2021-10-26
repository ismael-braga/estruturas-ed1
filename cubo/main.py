import opcubo as opc 

# Criação do cubo
cubo = opc.criar_cubo(5.0)
# Retorna o comprimento do cubo
print(f'Comprimento do cubo: {opc.comprimento_cubo(cubo):.2f}m')
# Retorna a largura do cubo
print(f'Largura do cubo: {opc.largura_cubo(cubo):.2f}m')
# Retorna a altura do cubo
print(f'Altura do cubo: {opc.altura_cubo(cubo):.2f}m')
# Retorna a área do cubo
print(f'Área do cubo: {opc.calcular_area(cubo):.2f}m²')
# Retorna o volume do cubo
print(f'Volume do cubo: {opc.calcular_volume(cubo):.2f}m³')
