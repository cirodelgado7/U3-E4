from ManejadorCalefactores import ManejadorC

if __name__ == '__main__':
    mc = ManejadorC(int(input('\nCantidad de Calefactores: ')))
    mc.cargarArchivos()
    mc.ingresarDatos()