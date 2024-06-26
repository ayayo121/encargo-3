import funciones as fn 
libro = []

while True:
    print("Bienvenido a la biblioteca de Duoc uc")
    print("por favor, ingrese la opcion")

    print("opcion 1: Registrar libro")
    print("opcion 2: listar todos los libros")
    print("opcion 3: registrar venta")
    print("opcion 4: imprimir reporte de ventas")
    print("opcion 5: generar txt")
    print("opcion 6: Salir")
    opcion = int(input(""))

    if opcion == 1:
        fn.registrar_libro(libro)
    elif opcion == 2:
        fn.listar_libros(libro)
    elif opcion == 3:
        fn.registrar_venta(libro)
    elif opcion == 4:
        fn.imprimir_ventas(libro)
    elif opcion == 5:
        fn.imprimir_ventas(libro)
    elif opcion == 6:
        break
    else:
        print("Opcion no valida")