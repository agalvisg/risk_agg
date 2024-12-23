class Territorio():
    def __init__(self, nombre, defensa, ocupado=False, lider=None):
        self.nombre = nombre
        self.defensa = defensa
        self.ocupado = ocupado
        self.lider = lider
        self.tropas = None

    def asiganar_tropas(self, tropas):
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
        fuerza_defensa = self.defensa + self.tropas.get_fuerza()
        if fuerza_ataque > fuerza_defensa:
            self.ocupar(tropas.lider)
            return True
        else:
            return False

        