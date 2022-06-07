import numpy as np
import csv
from ClaseCalefactor import Calefactor
from ClaseEléctrico import Electrico
from ClaseGas import Gas


class ManejadorC:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=0, incremento=5):
        self.__listaCalefactores = np.empty(dimension, dtype=Calefactor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = "\n***** Calefactores*****\n"
        for lista in self.__listaCalefactores:
            s += str(lista) + '\n'
        return s

    def agregarCalefactor(self, unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCalefactores.resize(self.__dimension)
        self.__listaCalefactores[self.__cantidad] = unCalefactor
        self.__cantidad += 1

    def cargarArchivos(self):
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                unCalefactor = Gas(fila[0], fila[1], fila[2], fila[3])
                self.agregarCalefactor(unCalefactor)
        archivo.close()
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                unCalefactor = Electrico(fila[0], fila[1], fila[2])
                self.agregarCalefactor(unCalefactor)
        archivo.close()

    def ingresarDatos(self):
        print("\n***** Calefactores a Gas*****")
        cantidadm3 = int(input('Cantidad estimada de M3: '))
        costoM3 = int(input('Costo por M3: '))
        menorConsumoGas = 99999999999999
        menorGas = None
        for calefactor in self.__listaCalefactores:
            if isinstance(calefactor, Gas):
                consumoGas = calefactor.calcularConsumo(cantidadm3, costoM3)
                if consumoGas < menorConsumoGas:
                    menorConsumoGas = consumoGas
                    menorGas = calefactor
        print(menorGas)
        print("\n***** Calefactores Eléctricos*****")
        cantidadKw = int(input('Cantidad estimada de Kw: '))
        costoKw = int(input('Costo por Kw: '))
        menorConsumoElectrico = 999999999999999
        menorElectrico = None
        for calefactor in self.__listaCalefactores:
            if isinstance(calefactor, Electrico):
                consumoElectrico = calefactor.calcularConsumo(cantidadm3, costoM3)
                if consumoElectrico < menorConsumoElectrico:
                    menorConsumoElectrico = consumoElectrico
                    menorElectrico = calefactor
        print(menorElectrico)
