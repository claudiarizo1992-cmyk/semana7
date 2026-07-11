class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Pasamos los datos directamente por los setters para activar las validaciones desde el inicio
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

        # --- Nombre ---
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = valor.strip()

        # ---Categoria ---
    @property
    def categoria (self) -> str:
        return self._categoria
            
    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        self._categoria = valor.strip()

        # --- Precio ---
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio del producto debe ser un numero mayor que cero")
        self._precio = valor

        # --- Disponibilidad ---
    @property
    def disponible(self) -> bool:
        return self._disponible
                    
    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

        # Metodo para mostrar los datos de forma legible
    def mostrar_informacion(self) -> str:
        estado = "disponible" if self.disponible else "agotado"
        return f"[{self.categoria.upper()}] {self.nombre} -> ${self.precio:.2f} ({estado})"
        

    
            
    