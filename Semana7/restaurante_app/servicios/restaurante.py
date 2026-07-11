from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self):
        # Iniciamos las listas privadas para proteger la informacion 
        self._productos = []
        self._clientes = []

        # --- METODOS PARA PRODUCTOS ---
    def registrar_producto(self,producto: Producto):
        self._productos.append(producto)
        print(f"sistema: '{producto.nombre}' se guardó correctamente. ")

    def listar_productos(self):
        if not self._productos:
               print("aviso: no existen productos registrados todavia")
               return
        print("\n--- CATALOGO DE PRODUCTOS ---")
        for prod in self._productos:
               print(prod.mostrar_informacion())
            
    def buscar_productos(self, nombre: str) -> Producto:
        # Buscamos ignorando mayusculas/minusculas y espacios extra
        for prod in self._productos:
            if prod.nombre.lower() == nombre.lower().strip():
                return prod
        return None
                
        # --- METODOS PARA CLIENTES ---
    def registrar_cliente(self, cliente: Cliente):
        self._clientes.append(cliente)
        print(f"sistema: cliente '{cliente.nombre}' registrado con éxito.")

    def listar_clientes(self):
        if not self._clientes:
              print("aviso: no hay cliente en la base de datos. ")
              return
        print("\n--- cliente registrado ---")
        for cli in self._clientes:
              print(cli.mostrar_infomacion())
                    
    def buscar_cliente(self, id_cliente: str) -> Cliente:
        # Buscamos por el identificador unico
        for cli in self._clientes:
            if cli.id_cliente.strip() == id_cliente.strip():
                return cli
        return None

