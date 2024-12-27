from territorio import Territorio

class Tablero:
    def __init__(self):
        self.territorios = []  # Lista para almacenar los territorios

    def agregar_territorio(self, territorio):
        self.territorios.append(territorio)

    def inicializar_territorios(self, num_territorios, defensas=None):
        """
        Genera territorios con fuerzas de defensa definidas.
        :param num_territorios: Número total de territorios.
        :param defensas: Lista de fuerzas de defensa (opcional). Si no se pasa, se asignan valores aleatorios.
        """
        if defensas and len(defensas) == num_territorios:
            # Usar las defensas proporcionadas
            for i, defensa in enumerate(defensas, 1):
                self.agregar_territorio(Territorio(f"Territorio {i}", defensa))
        else:
            # Asignar defensas aleatorias si no se especifican
            import random
            for i in range(1, num_territorios + 1):
                defensa = random.randint(5, 20)  # Fuerzas de defensa entre 5 y 20
                self.agregar_territorio(Territorio(f"Territorio {i}", defensa))

    def mostrar_tablero(self):
        for territorio in self.territorios:
            estado = "Ocupado" if territorio.ocupado else "Desocupado"
            print(f"{territorio.nombre}: {estado}, Defensa: {territorio.defensa}")
