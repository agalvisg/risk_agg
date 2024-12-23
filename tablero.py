class Tablero:
    def __init__(self):
        self.territorios = []

    def agregar_territorio(self, territorio):
        self.territorios.append(territorio)

    def mostrar_tablero(self):
        for territorio in self.territorios:
            estado = "Ocupado" if territorio.ocupado else "Desocupado"
            print(f"{territorio.nombre}: {estado}, Defensa: {territorio.defensa}")
