lista_productos = []

while True:
    print("\n--------------------------------------")
    print("Sistema de Gestión Básica De Productos")
    print("--------------------------------------")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("--------------------------------------")

    opcion = input("Indice del 1 al 5 la acción que desea realizar: ").strip()

    if opcion == "1":
        while True:
            nombre = input("\nIngrese el nombre de un producto: ").strip().lower()
            categoria = input("Ingrese la categoría a la que corresponde: ").strip().lower()
            
            while True:
                precio = input("Ingrese el precio del producto: ")
                if precio.isdigit():
                    precio = int(precio)
                    if precio < 0:
                        print("¡ERROR!, el valor del producto no puede ser negativo")
                    else:
                        break
                else:
                    print("¡ERROR!, ingrese un número entero")
            
            lista_productos.append([nombre, categoria, precio])

            continuar = input("\n¿Quiere seguir agregando productos a la lista? s/n: ").strip().lower()
            if continuar != "s":
                break

    elif opcion == "2":
        if not lista_productos:
            print("\nNo hay productos para mostrar.")
        else:
            print("\nListado de productos:")
            for i, producto in enumerate(lista_productos, start=1):
                print(f"\nProducto {i}:")
                print(f" - Nombre: {producto[0]}")
                print(f" - Categoría: {producto[1]}")
                print(f" - Precio: ${producto[2]}")

    elif opcion == "3":
        break

    elif opcion == "4":
        break

    elif opcion == "5":
        print("Usted ha salido del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor elija del 1 al 5.")
