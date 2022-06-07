from ClaseCalefactor import Calefactor


class Electrico(Calefactor):
    __potenciaMaxima = ''

    def __init__(self, marca='', modelo='', potenciaMaxima=''):
        super().__init__(marca, modelo)
        self.__potenciaMaxima = potenciaMaxima

    def __str__(self):
        cadena = super().__str__()
        cadena += '\nPotencia Máxima: ' + self.__potenciaMaxima
        return cadena

    def __lt__(self, other):
        return self.__consumo < other.__consumo

    def calcularConsumo(self, cantidad, costo):
        self.__consumo = float((int(self.__potenciaMaxima) / 1000) * cantidad * costo)
        return self.__consumo