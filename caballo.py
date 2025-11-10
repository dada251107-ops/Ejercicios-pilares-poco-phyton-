from animal import Animal
class Caballo(Animal):
    """Clase hija - Representa a un caballo con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, raza, velocidad_max):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del caballo
        self.raza = raza
        self.velocidad_max = velocidad_max
        self.tipo = "Mamífero terrestre"
        self.numero_patas = 4
    
    def moverse(self):
        return f"{self.nombre} galopa a una velocidad máxima de {self.velocidad_max} km/h"
    
    def comunicacion(self):
        return f"{self.nombre} relincha para comunicarse con otros caballos"
    
    def trotar(self):
        """Método específico del caballo"""
        return f"{self.nombre} está trotando elegantemente por el campo"
    
    def describir(self):
        """Descripción detallada del caballo"""
        return (f"{self.nombre} es un hermoso caballo de raza {self.raza} con pelaje {self.color}. "
                f"Es un mamífero herbívoro que vive en {self.habitat}. Tiene {self.numero_patas} patas "
                f"fuertes y musculosas que le permiten alcanzar velocidades de hasta {self.velocidad_max} km/h. "
                f"Los caballos son animales sociales que se comunican mediante relinchos y movimientos corporales.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Raza: {self.raza}")
        print(f"Velocidad máxima: {self.velocidad_max} km/h")
        print(f"Número de patas: {self.numero_patas}")
