

class Calefactor:
    __marca = ''
    __modelo = ''

    def __init__(self, marca='', modelo=''):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        cadena = '\nMarca: ' + self.__marca
        cadena += '\nModelo: ' + self.__modelo
        return cadena

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

