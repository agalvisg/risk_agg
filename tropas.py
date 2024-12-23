class Tropas():

    COSTOS = {
        'infanteria': 1,
        'caballeria': 3,
        'artilleria': 5
    }

    FUERZA = {
        'infanteria': 1,
        'caballeria': 3,
        'artilleria': 5
    }

    def __init__(self, infanteria, caballeria, artilleria):
        total_costo = (infanteria * self.COSTOS['infanteria'] +
                      caballeria * self.COSTOS['caballeria'] +
                      artilleria * self.COSTOS['artilleria'])
        if total_costo > 20:
            raise ValueError("No se pueden tener más de 20 tropas")
        
        super().__init__(total_costo)
        self.infanteria = infanteria
        self.caballeria = caballeria
        self.artilleria = artilleria


#Metodos get
    def get_infanteria(self):
        return self.infanteria
    
    def get_caballeria(self):
        return self.caballeria
    
    def get_artilleria(self):    
        return self.artilleria
    def get_fuerza(self):
        return self.infanteria * self.FUERZA['infanteria'] + self.caballeria * self.FUERZA['caballeria'] + self.artilleria * self.FUERZA['artilleria']
    