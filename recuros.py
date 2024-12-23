class Recursos():
    def __init__(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad de recursos no puede ser negativa")
        elif cantidad > 20:
            raise ValueError("La cantidad de recursos no puede ser mayor a 20")
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad
    
        