
productos = []

def registrar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad_producto = input("Ingrese la cantidad del producto: ")
    
    for producto in productos:
        if producto['id'] == id_producto or producto['nombre'] == nombre_producto:
            print("El producto ya existe en la lista.")
            return
    
    productos.append({'id': id_producto, 'nombre': nombre_producto, 'cantidad': cantidad_producto})
    print("Producto registrado exitosamente.")

def modificar_producto():
    nombre_producto = input("Ingrese el nombre del producto a modificar: ")
    campo = input("Ingrese el campo a modificar (id, nombre, cantidad): ")
    
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            producto[campo] = nuevo_valor
            print("Producto modificado exitosamente.")
            return
    
    print("Producto no encontrado.")

def eliminar_producto():
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    
    for producto in productos:
        if producto['id'] == id_producto:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    
    print("Producto no encontrado.")

def consultar_productos():
    consulta = input("Desea consultar todos los productos (todos) o por nombre (nombre): ")
    
    if consulta == 'todos':
        for producto in productos:
            print(producto)
    elif consulta == 'nombre':
        nombre_producto = input("Ingrese el nombre del producto a consultar: ")
        for producto in productos:
            if producto['nombre'] == nombre_producto:
                print(producto)
                return
        print("Producto no encontrado.")
    else:
        print("Opción no válida.")

while True:
    print("\n1. Registrar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Consultar productos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_producto()
    elif opcion == '2':
        modificar_producto()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        consultar_productos()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")