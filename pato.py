from animal import Animal
class Pato(Animal):
    """Clase hija - Representa a un pato con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_plumaje, puede_volar):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del pato
        self.tipo_plumaje = tipo_plumaje
        self.puede_volar = puede_volar
        self.tipo = "Ave acuática"
        self.numero_patas = 2
    
    def moverse(self):
        movimiento = "vuela, nada y camina" if self.puede_volar else "nada y camina"
        return f"{self.nombre} {movimiento} con facilidad"
    
    def comunicacion(self):
        return f"{self.nombre} grazna en diferentes tonos para comunicarse"
    
    def volar(self):
        """Método específico del pato"""
        if self.puede_volar:
            return f"{self.nombre} vuela sobre el agua batiendo sus alas"
        return f"{self.nombre} no puede volar pero es excelente nadador"
    
    def nadar(self):
        """Método específico del pato"""
        return f"{self.nombre} nada en la superficie del agua usando sus patas palmeadas"
    
    def describir(self):
        """Descripción detallada del pato"""
        vuelo = "puede volar largas distancias" if self.puede_volar else "ha perdido la capacidad de vuelo"
        return (f"{self.nombre} es un pato con hermoso plumaje {self.tipo_plumaje} de color {self.color}. "
                f"Es un ave acuática omnívora que habita en {self.habitat} y se alimenta de {self.dieta}. "
                f"{self.nombre} {vuelo}, pero siempre es un excelente nadador gracias a sus patas palmeadas. "
                f"Su plumaje impermeable lo mantiene seco mientras nada. Los patos tienen {self.numero_patas} patas "
                f"y son animales sociales que viven en grupos.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Tipo de plumaje: {self.tipo_plumaje}")
        print(f"Puede volar: {'Sí' if self.puede_volar else 'No'}")
        print(f"Número de patas: {self.numero_patas}")

