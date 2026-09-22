# CRUD System

ventas = []
incremental = 1

# Create
def registrar_venta(producto:str, cantidad:int, precio:float) -> None:
    global incremental
    nueva_venta = {
        "id" : incremental,
        "producto" : producto,
        "cantidad" : cantidad,
        "precio" : precio,
        "total" : cantidad * precio
    }
    ventas.append(nueva_venta)
    incremental += 1
    print(f"Venta de {producto} registrada con éxito. ID de venta: {nueva_venta['id']}")
# Read
def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas todavía")
        return 
    
    print("========= Registro de ventas =========")
    
    for venta in ventas:
        print(f"ID: {venta['id']} | Producto: {venta['producto']} | Precio: {venta['precio']} | Cantidad: {venta['cantidad']} | Total: {venta['total']}")
    
    print("\033[33m" + "-" * 60 + "\033[0m")
        
# Update
def actualizar_venta(id:int, producto:str, cantidad:int, precio:float) -> bool:
    if not ventas:
        print("No hay ventas aún")
    for venta in ventas:
        if venta['id'] == id:
            venta["producto"] = producto
            venta["cantidad"] = cantidad
            venta["precio"] = precio
            venta["total"] = cantidad * precio
            
            print(f"El producto fue actualizado correctamente")
            return True
        
    print("No se encontó un producto con ese ID")
    return False

# Delete
def eliminar_venta(id: int)-> None:
    global ventas
    
    original_len = len(ventas)
    
    ventas = [v for v in ventas if v["id"] != id]
    
    if len(ventas) < original_len:
        print(f"Venta {id} eliminada")
    else:
        print("No se encontró venta con ese ID.")
  
  
# Menu Pedir datos

def pedir_datos()->tuple:
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    
    return producto, cantidad, precio
      
opcion = None

while opcion != "5":
   
    print("Bienvenido a mi app de ventas. ")
    print("\033[31m" + "-" * 60 + "\033[0m")
    print("1. Ver productos")
    print("2. Registrar productos")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("5. Salir")
    print("\033[31m" + "-" * 60 + "\033[0m")
    
    print("\033[31m" + "-" * 60 + "\033[0m")
    opcion = input("------Escoja una opción: ")
    print("\033[31m" + "-" * 60 + "\033[0m")
    
    
    if opcion == "1":
        mostrar_ventas()
    elif opcion == "2":
        producto, cantidad, precio = pedir_datos()
        registrar_venta(producto, cantidad, precio)
    elif opcion == "3": 
        id = int(input("Ingrese el ID del producto: "))
        producto, cantidad, precio = pedir_datos()
        actualizar_venta(id, producto, cantidad, precio)
    elif opcion == "4":
        id = int(input("Ingrese el ID del producto: "))
        eliminar_venta(id)
    else:
        print("Por favor escoja una opción válida")    
        
        
    
    
    
print("Gracias por usar mi sistema, que tenga buen día :)")