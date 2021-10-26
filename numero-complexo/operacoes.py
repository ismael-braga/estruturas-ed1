def criar_complexo(real=0, imaginaria=0):
    numero_complexo = [real, imaginaria]
    return numero_complexo

def multiplicar_complexos(z1, z2):
    # z1 = a + bi 
    # z2 = c + di
    # resultado = (ac - bd) + (ad + bc)i
    ac = z1[0] * z2[0]
    ad = z1[0] * z2[1]
    bc = z1[1] * z2[0]
    bd = z1[1] * z2[1]
    return [ac - bd, ad + bc]

def conjugado_complexo(z):
    z[1] *= -1
    return z

def dividir_complexos(z1, z2):
    # z1 = a + bi 
    # z2 = c + di
    # resultado = ac + bd + (cb - ad)i / c² + d² 
    ac = z1[0] * z2[0]
    bd = z1[1] * z2[1]
    cb = z2[0] * z1[1]
    ad = z1[0] * z2[1]
    c_ao_quadrado = z2[0] ** 2 
    d_ao_quadrado = z2[1] ** 2
    numerador_real = ac + bd
    numerador_imaginario = cb - ad
    denominador = c_ao_quadrado + d_ao_quadrado
    return [numerador_real, numerador_imaginario, denominador]
