from dataclasses import dataclass

@dataclass
class ItemCompra:
    def __init__(self, libro: int, cantidad: int):
        self.libro: int = libro
        self.cantidad: int = cantidad

    def calcular_subtotal(self):
        subtotal = self.libro.precio * self.cantidad
        return subtotal
