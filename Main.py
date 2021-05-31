import csv
from datetime import datetime
from Planta import Planta
from Contratado import Contratado
from Externo import Externo
from ManejadorE import ManejadorE
from Menu import Menu


def cargarArreglo(ce):

    with open("Planta.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Planta(row[0], row[1], row[2], row[3], float(row[4]), int(row[5])))
    archivo.close()

    with open("Contratados.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Contratado(row[0], row[1], row[2], row[3],
            datetime.strptime(row[4], "%d/%m/%Y"), datetime.strptime(row[5], "%d/%m/%Y"), int(row[6])))
    archivo.close()

    with open("Externos.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Externo(row[0], row[1], row[2], row[3], row[4],
            datetime.strptime(row[5], "%d/%m/%Y"), datetime.strptime(row[6], "%d/%m/%Y"),
            float(row[7]), float(row[8]), float(row[9])))
    archivo.close()

    Contratado.setValorPorHora(float(300))  # Valor de la hora para empleados contratados

if __name__ == '__main__':
    ce = ManejadorE(int(9))  # Cantidad de Empleados
    cargarArreglo(ce)
    print(ce)
    menu = Menu()
    menu.mostrarMenu(ce)
