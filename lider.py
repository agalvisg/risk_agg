from tropas import Tropas


class Lider():
    def __init__(self, nombre, tropas):
        """
        :param nombre: Nombre del líder
        :param tropas: Instancia de la clase Tropas que contiene las tropas del líder
        """
        
        self.nombre = nombre
        self.tropas = tropas

    def asignar_tropas_a_territorio(self, territorio, infanteria, caballeria, artilleria):
        """
        Asigna tropas del líder a un territorio
        :param territorio: Instancia de la clase Territorio
        :param infanteria: Número de infantería a asignar
        :param caballeria: Número de caballería a asignar
        :param artilleria: Número de artillería a asignar
        """
        # Validar si  el líder tiene suficientes tropas para asignar
        if (self.tropas.infanteria >= infanteria and
            self.tropas.caballeria >= caballeria and
            self.tropas.artilleria >= artilleria):
            
            #Restar las tropas asignadas al líder
            self.tropas.infanteria -= infanteria
            self.tropas.caballeria -= caballeria
            self.tropas.artilleria -= artilleria

            #Asignar las tropas al territorio
            tropas_asignadas = Tropas(infanteria, caballeria, artilleria)
            territorio.asignar_tropas(tropas_asignadas)
            territorio.ocupar(self)

            print(f"Tropas asignadas a {territorio.nombre} por {self.nombre}: {tropas_asignadas}")

        else:
            print(f"{self.nombre} no tiene suficientes tropas para asignar a {territorio.nombre}")
            

        def mostrar_tropas_disponibles(self):
            """
            Muestra las tropas disponibles del líder
            """
            print(f"Tropas disponibles de {self.nombre}: {self.tropas}")