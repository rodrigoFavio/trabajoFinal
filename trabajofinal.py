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

if opcion == "1":
        paginas = int(input("¿Cuántas páginas desea copiar?: "))
        precio_por_pagina = calcular_precio(paginas)
        monto = paginas * precio_por_pagina
        pedidos.append((paginas, monto))              # Guardamos el pedido como tupla
        stock -= paginas                             # Descontamos las hojas del stock

        print(f"Pedido: {paginas} páginas x S/ {precio_por_pagina:.2f} = S/ {monto:.2f}")

        if stock < 200:
            print("¡Queda poco papel! Reponer pronto.")