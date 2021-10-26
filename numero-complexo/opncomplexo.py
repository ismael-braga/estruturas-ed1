def criar_complexo(real, imaginario):
    numero_complexo = {'real': real, 'imaginario': imaginario}
    return numero_complexo

def destruir_complexo(z):
    def __del__():
        return 0

def conjugado_complexo(z):
    z['imaginario'] *= -1
    return z

def multiplicar_complexos(z1, z2):
    # z1 = a + bi 
    # z2 = c + di
    # resultado = (ac - bd) + (ad + bc)i
    ac = z1['real'] * z2['real']
    ad = z1['real'] * z2['imaginario']
    bc = z1['imaginario'] * z2['real']
    bd = z1['imaginario'] * z2['imaginario']
    real = ac - bd
    imaginario = ad + bc
    return {'real': real, 'imaginario': imaginario}

def dividir_complexos(z1, z2):
    # z1 = a + bi 
    # z2 = c + di
    # resultado = ac + bd + (cb - ad)i / c² + d² 
    ac = z1['real'] * z2['real']
    bd = z1['imaginario'] * z2['imaginario']
    cb = z2['real'] * z1['imaginario']
    ad = z1['real'] * z2['imaginario']
    c_ao_quadrado = z2['real'] ** 2 
    d_ao_quadrado = z2['imaginario'] ** 2
    numerador_real = ac + bd
    numerador_imaginario = cb - ad
    denominador = c_ao_quadrado + d_ao_quadrado
    return {'numerador_real': numerador_real, 'numerador_imaginario': numerador_imaginario, 'denominador': denominador}

def mostra_complexo(z):
    if len(z) <= 2:
        if z['imaginario'] < 0:
            simbolo = '-'
        else:
            simbolo = '+'
        if z['imaginario'] == 0:
            return f'{z["real"]}'
        if z['real'] == 0:
            return f'{z["imaginario"]}i'
        return f'{z["real"]} {simbolo} {abs(z["imaginario"])}i'
    else:
        if z['numerador_imaginario'] < 0:
            simbolo = '-'
        else:
            simbolo = '+'
        if z['numerador_imaginario'] == 0:
            return f'{z["numerador_real"]} / {z["denominador"]}'
        if z['numerador_real'] == 0:
            return f'{z["numerador_imaginario"]}i'
        return f'{z["numerador_real"]} {simbolo} {abs(z["numerador_imaginario"])}i / {z["denominador"]}'
