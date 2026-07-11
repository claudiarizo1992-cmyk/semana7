from dataclasses import dataclass

@dataclass
class Cliente:
    """Clase limpia para representar a un cliente mediante una dataclass."""
    nombre: str
    correo: str
    id_cliente: str
    def mostrar_informacion(self) -> str:
        return f"ID: {self.id_cliente} | nombre: {self.nombre} | Correo: {self.correo}"
    