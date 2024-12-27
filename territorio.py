class Territorio:
    def __init__(self, nombre, defensa, ocupado=False, lider=None):
        self.nombre = nombre
        self.defensa = defensa
        self.ocupado = ocupado
        self.lider = lider
        self.tropas = None

    def asignar_tropas(self, tropas):
        self.tropas = tropas

    def ocupar(self, lider):
        self.ocupado = True
        self.lider = lider

    def desocupar(self):
        self.ocupado = False
        self.lider = None

    def get_nombre(self):
        return self.nombre

    def get_defensa(self):
        return self.defensa

    def resolver_ataque(self, tropas):
        fuerza_ataque = tropas.get_fuerza()
        fuerza_defensa = self.defensa + (self.tropas.get_fuerza() if self.tropas else 0)
        if fuerza_ataque > fuerza_defensa:
            self.ocupar(tropas.lider)
            self.asignar_tropas(tropas)  # Asignar tropas del atacante al territorio
            return True
        elif fuerza_ataque == fuerza_defensa:
            return False  # El defensor mantiene el territorio en caso de empate
        else:
            return False

    def __str__(self):
        estado = "Ocupado" if self.ocupado else "Libre"
        lider = self.lider if self.lider else "Ninguno"
        return f"{self.nombre}: Defensa {self.defensa}, Estado {estado}, Líder {lider}"
