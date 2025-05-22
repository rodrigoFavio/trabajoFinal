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
            
elif opcion == "2":          
    # Calculamos ingresos con for       
        total_ingresos = 0
        for pedido in pedidos:
            total_ingresos += pedido[1]

        print("\nResumen:")
        print(f"- Pedidos realizados: {len(pedidos)}")
        print(f"- Ingresos acumulados: S/ {total_ingresos:.2f}")
        print(f"- Hojas restantes: {stock}")



for pedido in pedidos:
            paginas = pedido[0]
            monto = pedido[1]
            print(f"{pedido_numero}. {paginas} páginas - S/ {monto:.2f}")
            total_ingresos += monto
            pedido_numero += 1

            print(f"\nTotal de pedidos: {len(pedidos)}")
            print(f"Ingresos totales: S/ {total_ingresos:.2f}")
            print(f"Hojas restantes:  {stock}")
            print("¡Gracias por usar el sistema!")
            break

else:
        print("Opción no válida. Por favor, ingresa 1, 2, 3 o 4.")
