from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_menu():
    
    gestor = Restaurante()
    while True:
        print("\n=================================")
        print("    SISTEMA DE RESTAURANTE   ")
        print("=================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("---------------------------------")
        print("4. Registrar cliente")
        print("5. Listar cliente")
        print("6. Buscar cliente")
        print("------------------------------------")
        print("7. Salir")
        print("===================================")

        opcion = input("por favor, elija una de las siguientes opciones (1-7): ").strip()

        if opcion == "1":
            print("\n[registro de producto]")
            try:
                nombre = input("nombre del articulo: ")
                categoria = input("categoria/seccion: ")
                precio = float(input("precio al publico: "))

                nuevo_prod = Producto(nombre, categoria, precio)
                gestor.registrar_producto(nuevo_prod)
            except ValueError as error:
                print(f"error al guardar. {error}")

        elif opcion == "2":
            gestor.listar_productos()

        elif opcion == "3":
            print("\n[Búsqueda de Productos]")
            nombre_buscar = input("nombre del producto que busca: ")
            resultado = gestor.buscar_productos(nombre_buscar)
            if resultado:
                print(f"resultado: {resultado.mostrar_informacion}")
            else: 
                print("no se encuentra ningun articulo relacionado")
        
        elif opcion == "4":
            print("\n[Registro de Cliente]")
            id_cli = input("NUMERO DE CEDULA O ID").strip()
            if not id_cli:
                print("el documento de identidad no puede estar vacio")
                continue
            nombre_cli =input("nombre y apellido: ")
            correo_cli =input("correo electronicos: ")

            nuevo_cli =Cliente(id_cli, nombre_cli, correo_cli)
            gestor.registrar_cliente(nuevo_cli)
        
        elif opcion == "5":
            gestor.listar_clientes()

        elif opcion == "6":
            print("\n[Búsqueda de Clientes]")
            id_buscar = input("ingrese el numero de cedula")
            resultado = gestor.buscar_cliente(id_buscar)
            if resultado:
              print(f"resultado: resultado: {resultado.mostrar_informacion()}")
            else:
                print("el cliente solicitado no consta en los registros")
        
        elif opcion == "7":
            print("cerrando el gestor. ¡hsata pronto")
            break
        else:
            print("opcion no valida. por favor, intente con un numero del 1 al 7")
if __name__ == "__main__":
    ejecutar_menu()  