from recuros import Recursos
from tropas import Tropas

class Lideres(Recursos, Tropas):
    num_jugadores = 0  # Atributo estático para contar el número de jugadores

    def __init__(self, nombre, recursos, infanteria, caballeria, artilleria):
        Recursos.__init__(self, recursos)
        Tropas.__init__(self, infanteria, caballeria, artilleria)
        self.nombre = nombre
        Lideres.num_jugadores += 1  # Incrementa el contador al crear un nuevo líder

    @classmethod
    def get_num_jugadores(cls):
        return cls.num_jugadores
