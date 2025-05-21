def calcular_precio(paginas):
    if paginas <= 20:
        return 0.20
    elif paginas <= 50:
        return 0.18
    else:
        return 0.15


stock = 2000           # Hojas de papel disponibles
pedidos = []           # Lista que guardará tuplas (páginas, monto)

while True:                   # menú principal
    print("\n1) Nuevo pedido\n2) Resumen\n3) Cargar hojas\n4) Cerrar caja")
    opcion = input("Opción: ")
