class Animal:
    """Clase padre que define los atributos y métodos comunes de todos los animales"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        # Atributos comunes (según la imagen)
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
    
    # Métodos comunes (según la imagen)
    def moverse(self):
        return f"{self.nombre} se está moviendo"
    
    def comunicacion(self):
        return f"{self.nombre} puede comunicarse con seres vivios en su entorno"
    
    def reproduccion(self):
        return f"{self.nombre} puede reproducirse"
    
    def alimentarse(self):
        return f"{self.nombre} se está alimentando con {self.dieta}"
    
    def adaptacion(self):
        return f"{self.nombre} se adapta a su entorno"
    
    def instintos(self):
        return f"{self.nombre} sigue sus instintos naturales"
    
    def descanso(self):
        return f"{self.nombre} está descansar en su hábitat"
    
    def sueno(self):
        return f"{self.nombre} puede dormir para recuperar energías"
    
    def interaccion_social(self):
        return f"{self.nombre} interactúa socialmente"
    
    def describir(self):
        """Descripción detallada del animal"""
        return f"{self.nombre} es un animal que habita en {self.habitat}"
    
    def mostrar_info(self):
        """Muestra toda la información del animal"""
        print(f"\n{'='*50}")
        print(f"informacio sobre: {self.nombre.upper()}")
        print(f"{'='*50}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamano}")
        print(f"Color: {self.color}")
