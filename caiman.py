from animal import Animal
class Caiman(Animal):
    """Clase hija - Representa a un caimán con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, longitud, fuerza_mordida):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del caimán
        self.longitud = longitud
        self.fuerza_mordida = fuerza_mordida
        self.tipo = "Reptil acuático"
        self.numero_dientes = 80
    
    def moverse(self):
        return f"{self.nombre} se desplaza nadando con su poderosa cola y caminando en tierra"
    
    def comunicacion(self):
        return f"{self.nombre} emite gruñidos y silbidos para comunicarse"
    
    def cazar(self):
        """Método específico del caimán"""
        return f"{self.nombre} acecha pacientemente a su presa bajo el agua"
    
    def tomar_sol(self):
        """Método específico del caimán"""
        return f"{self.nombre} está termorregulando su cuerpo tomando el sol en la orilla"
    
    def describir(self):
        """Descripción detallada del caimán"""
        return (f"{self.nombre} es un imponente caimán de {self.longitud} metros de longitud con piel {self.color}. "
                f"Es un reptil carnívoro que habita en {self.habitat}. Su mandíbula puede ejercer una fuerza de "
                f"{self.fuerza_mordida} PSI, siendo uno de los depredadores más temidos de su ecosistema. "
                f"Tiene aproximadamente {self.numero_dientes} dientes afilados. Los caimanes son reptiles de sangre fría "
                f"que pasan tiempo tanto en el agua como en tierra firme.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Longitud: {self.longitud} metros")
        print(f"Fuerza de mordida: {self.fuerza_mordida} PSI")
        print(f"Número de dientes: {self.numero_dientes}")


