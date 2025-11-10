from animal import Animal
class EscarabajoRinoceronte(Animal):
    """Clase hija - Representa a un escarabajo rinoceronte con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, longitud_cuerno, peso_soportado):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del escarabajo rinoceronte
        self.longitud_cuerno = longitud_cuerno
        self.peso_soportado = peso_soportado
        self.tipo = "Insecto"
        self.numero_patas = 6
    
    def moverse(self):
        return f"{self.nombre} camina con sus 6 patas y puede volar distancias cortas"
    
    def comunicacion(self):
        return f"{self.nombre} se comunica mediante feromonas y sonidos de fricción"
    
    def usar_cuerno(self):
        """Método específico del escarabajo rinoceronte"""
        return f"{self.nombre} usa su cuerno de {self.longitud_cuerno} cm para pelear con otros machos"
    
    def levantar_peso(self):
        """Método específico del escarabajo rinoceronte"""
        return f"{self.nombre} puede levantar hasta {self.peso_soportado} veces su propio peso"
    
    def describir(self):
        """Descripción detallada del escarabajo rinoceronte"""
        return (f"{self.nombre} es un escarabajo rinoceronte de color {self.color} brillante. "
                f"Es un insecto herbívoro que habita en {self.habitat} y se alimenta de {self.dieta}. "
                f"Su característica más distintiva es su cuerno de {self.longitud_cuerno} cm que los machos usan "
                f"para combatir por territorio y hembras. Es uno de los animales más fuertes del planeta en proporción "
                f"a su tamaño, pudiendo cargar hasta {self.peso_soportado} veces su peso corporal. "
                f"Tiene {self.numero_patas} patas y un exoesqueleto duro que lo protege.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Longitud del cuerno: {self.longitud_cuerno} cm")
        print(f"Peso soportado: {self.peso_soportado}x su peso")
        print(f"Número de patas: {self.numero_patas}")
