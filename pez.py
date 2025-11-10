from animal import Animal
class Pez(Animal):
    """Clase hija - Representa a un pez con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, especie, profundidad_max):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del pez
        self.especie = especie
        self.profundidad_max = profundidad_max
        self.tipo = "Vertebrado acuático"
        self.numero_aletas = 7
    
    def moverse(self):
        return f"{self.nombre} nada ágilmente usando sus aletas"
    
    def comunicacion(self):
        return f"{self.nombre} se comunica mediante movimientos corporales y señales visuales"
    
    def nadar(self):
        """Método específico del pez"""
        return f"{self.nombre} nada hasta {self.profundidad_max} metros de profundidad"
    
    def respirar_agua(self):
        """Método específico del pez"""
        return f"{self.nombre} respira oxígeno disuelto en el agua mediante sus branquias"
    
    def describir(self):
        """Descripción detallada del pez"""
        return (f"{self.nombre} es un pez {self.especie} de colores {self.color} brillantes. "
                f"Es un vertebrado acuático que vive en {self.habitat} y se alimenta de {self.dieta}. "
                f"Puede sumergirse hasta {self.profundidad_max} metros de profundidad. Tiene {self.numero_aletas} aletas "
                f"que le permiten maniobrar con precisión en el agua. Los peces respiran a través de branquias "
                f"que extraen oxígeno del agua.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Especie: {self.especie}")
        print(f"Profundidad máxima: {self.profundidad_max} metros")
        print(f"Número de aletas: {self.numero_aletas}")

