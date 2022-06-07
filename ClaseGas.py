from ClaseCalefactor import Calefactor


class Gas(Calefactor):
    __matricula = ''
    __calorias = ''

    def __init__(self, marca='', modelo='', matricula='', calorias=''):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    def __str__(self):
        cadena = super().__str__()
        cadena += '\nMartricula: ' + self.__matricula
        cadena += '\nCalorias: ' + self.__calorias
        cadena += '\nConsumo: ' + str(self.__consumo)
        return cadena

    def __lt__(self, other):
        return self.__consumo < other.__consumo

    def calcularConsumo(self, cantidad, costo):
        self.__consumo = float((int(self.__calorias) / 1000) * cantidad * costo)
        return self.__consumo
