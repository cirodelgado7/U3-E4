from Empleado import Empleado

class Planta(Empleado):

    __sueldoBasico = 0.0
    __antiguedad = 0.0

    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def __str__(self):
        return super(Planta, self).__str__() + '\n Sueldo Basico: {} \n Antigüedad: {}'\
            .format(self.__sueldoBasico, self.__antiguedad)

    def Sueldo(self):
        sueldo = self.__sueldoBasico + (1.1 * self.__sueldoBasico * self.__antiguedad)
        return sueldo
