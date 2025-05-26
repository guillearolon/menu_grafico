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

    opcion = input("Indique del 1 al 5 la acción que desea realizar: ").strip()

    if opcion == "1":
        while True:
            nombre = input("\nIngrese el nombre de un producto: ").strip().lower()
            if not nombre:
                print("¡ERROR! El nombre no puede estar vacío.")
                continue

            categoria = input("Ingrese la categoría a la que corresponde: ").strip().lower()
            if not categoria:
                print("¡ERROR! La categoría no puede estar vacía.")
                continue

            while True:
                precio = input("Ingrese el precio del producto: ").strip()
                if precio.isdigit():
                    precio = int(precio)
                    if precio < 0:
                        print("¡ERROR! El precio no puede ser negativo.")
                    else:
                        break
                else:
                    print("¡ERROR! Ingrese un número entero válido.")

            lista_productos.append([nombre, categoria, precio])
            print("Producto agregado correctamente.")

            continuar = input("\n¿Desea agregar otro producto? (s/n): ").strip().lower()
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
        busqueda = input("\nIngrese el nombre del producto a buscar: ").strip().lower()
        if not busqueda:
            print("¡ERROR! No se ingresó un nombre para buscar.")
        else:
            encontrados = []
            for producto in lista_productos:
                if busqueda in producto[0]:
                    encontrados.append(producto)

            if encontrados:
                print(f"\nProductos encontrados con '{busqueda}':")
                for prod in encontrados:
                    print(f" - Nombre: {prod[0]}, Categoría: {prod[1]}, Precio: ${prod[2]}")
            else:
                print(f"No se encontraron productos con el nombre '{busqueda}'.")

    elif opcion == "4":
        if not lista_productos:
            print("\nNo hay productos para eliminar.")
        else:
            eliminar = input("\nIngrese el nombre exacto del producto a eliminar: ").strip().lower()
            encontrado = False
            for i, producto in enumerate(lista_productos):
                if producto[0] == eliminar:
                    del lista_productos[i]
                    encontrado = True
                    print(f"Producto '{eliminar}' eliminado correctamente.")
                    break
            if not encontrado:
                print(f"No se encontró el producto '{eliminar}' en la lista.")

    elif opcion == "5":
        print("Usted ha salido del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor elija del 1 al 5.")
