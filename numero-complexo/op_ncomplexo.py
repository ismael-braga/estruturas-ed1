class Complexo:
    def __init__(self):
        self.complexo = {}
    
    def criar_complexo(self, real, imaginario):
        self.complexo = {'real': real, 'imaginario': imaginario}
        return self.complexo

    def __del__(self):
        return 0

    def conjugado_complexo(self, z):
        self.complexo['imaginario'] *= -1
        return self.complexo

    def multiplicar_complexos(self, z1, z2):
        # z1 = a + bi 
        # z2 = c + di
        # resultado = (ac - bd) + (ad + bc)i
        ac = self.complexo['real'] * self.complexo['real']
        ad = self.complexo['real'] * self.complexo['imaginario']
        bc = self.complexo['imaginario'] * self.complexo['real']
        bd = self.complexo['imaginario'] * self.complexo['imaginario']
        real = ac - bd
        imaginario = ad + bc
        return {'real': real, 'imaginario': imaginario}

    def dividir_complexos(self, z1, z2):
        # z1 = a + bi 
        # z2 = c + di
        # resultado = ac + bd + (cb - ad)i / c² + d² 
        ac = self.complexo['real'] * self.complexo['real']
        bd = self.complexo['imaginario'] * self.complexo['imaginario']
        cb = self.complexo['real'] * self.complexo['imaginario']
        ad = self.complexo['real'] * self.complexo['imaginario']
        c_ao_quadrado = self.complexo['real'] ** 2 
        d_ao_quadrado = self.complexo['imaginario'] ** 2
        numerador_real = ac + bd
        numerador_imaginario = cb - ad
        denominador = c_ao_quadrado + d_ao_quadrado
        return {'numerador_real': numerador_real, 'numerador_imaginario': numerador_imaginario, 'denominador': denominador}

    def __repr__(self):
        return str(self)

    def __str__(self):
        if len(self.complexo) <= 2:
            if z['imaginario'] < 0:
                simbolo = '-'
            else:
                simbolo = '+'
            if self.complexo['imaginario'] == 0:
                return f'{self.complexo["real"]}'
            if self.complexo['real'] == 0:
                return f'{self.complexo["imaginario"]}i'
            return f'{self.complexo["real"]} {simbolo} {abs(self.complexo["imaginario"])}i'
        else:
            if self.complexo['numerador_imaginario'] < 0:
                simbolo = '-'
            else:
                simbolo = '+'
            if self.complexo['numerador_imaginario'] == 0:
                return f'{self.complexo["numerador_real"]} / {self.complexo["denominador"]}'
            if self.complexo['numerador_real'] == 0:
                return f'{self.complexo["numerador_imaginario"]}i'
            return f'{self.complexo["numerador_real"]} {simbolo} {abs(self.complexo["numerador_imaginario"])}i / {self.complexo["denominador"]}'
