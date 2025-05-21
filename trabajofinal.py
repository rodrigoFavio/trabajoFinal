def calcular_precio(paginas):
    if paginas <= 20:
        return 0.20
    elif paginas <= 50:
        return 0.18
    else:
        return 0.15

 # Hojas de papel disponibles
stock = 2000
# Lista que guardará tuplas (páginas, monto)
pedidos = []          
     # menú principal
while True:                  
    print("\n1) Nuevo pedido\n2) Resumen\n3) Cargar hojas\n4) Cerrar caja")
    opcion = input("Opción: ")

if opcion == "1":
        paginas = int(input("¿Cuántas páginas desea copiar?: "))
        precio_por_pagina = calcular_precio(paginas)
        monto = paginas * precio_por_pagina
        # Guardamos el pedido como tupla
        pedidos.append((paginas, monto))  
        # Descontamos las hojas del stock
        stock -= paginas                            

        print(f"Pedido: {paginas} páginas x S/ {precio_por_pagina:.2f} = S/ {monto:.2f}")

        if stock < 200:
            print("¡Queda poco papel! Reponer pronto.")