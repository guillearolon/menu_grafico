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

    opcion = input("Elija una opción del 1 al 5: ").strip()

    if opcion == "1":
        while True:
            print("\n--- Agregar nuevo producto ---")

            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            categoria = input("Ingrese la categoría del producto: ").strip().lower()
            if not categoria:
                print("La categoría no puede estar vacía.")
                continue

            while True:
                precio = input("Ingrese el precio del producto (solo números enteros): ").strip()
                if precio.isdigit():
                    precio = int(precio)
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        break
                else:
                    print("Ingrese un número válido.")

            lista_productos.append([nombre, categoria, precio])
            print("Producto agregado correctamente.")

            continuar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            if continuar != "s":
                break

    elif opcion == "2":
        print("\n--- Lista de productos ---")
        if not lista_productos:
            print("No hay productos guardados.")
        else:
            i = 1
            for producto in lista_productos:
                print(f"\nProducto {i}:")
                print(f" - Nombre: {producto[0]}")
                print(f" - Categoría: {producto[1]}")
                print(f" - Precio: ${producto[2]}")
                i += 1

    elif opcion == "3":
        print("\n--- Buscar producto ---")
        busqueda = input("Ingrese parte o todo el nombre del producto: ").strip().lower()
        if not busqueda:
            print("No escribió nada para buscar.")
        else:
            encontrados = []
            for producto in lista_productos:
                if busqueda in producto[0]:
                    encontrados.append(producto)

            if encontrados:
                print("\nProductos encontrados:")
                for prod in encontrados:
                    print(f" - Nombre: {prod[0]}, Categoría: {prod[1]}, Precio: ${prod[2]}")
            else:
                print("No se encontraron productos con ese nombre.")

    elif opcion == "4":
        print("\n--- Eliminar producto ---")
        if not lista_productos:
            print("No hay productos para eliminar.")
        else:
            eliminar = input("Escriba el nombre exacto del producto que desea eliminar: ").strip().lower()
            encontrado = False
            for i in range(len(lista_productos)):
                if lista_productos[i][0] == eliminar:
                    del lista_productos[i]
                    encontrado = True
                    print(f"Producto '{eliminar}' eliminado correctamente.")
                    break
            if not encontrado:
                print(f"No se encontró el producto '{eliminar}'.")

    elif opcion == "5":
        print("Gracias por usar el sistema. Hasta pronto.")
        break

    else:
        print("Opción no válida. Por favor elija un número del 1 al 5.")
