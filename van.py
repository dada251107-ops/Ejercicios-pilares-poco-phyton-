class Van(Vehiculo):
    """Clase para vans/microbuses - Hereda de Vehiculo"""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros,
                 tipo_combustible, tipo_servicio, aire_acondicionado, capacidad_carga):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        # Atributos únicos de la van
        self.tipo_servicio = tipo_servicio  # Ej: "Transporte público", "Turismo", "Escolar"
        self.aire_acondicionado = aire_acondicionado
        self.capacidad_carga = capacidad_carga  # En kg
        self.carga_actual = 0
        self.pasajeros_actuales = 0
    
    def cargar(self, peso):
        """Carga peso en la van"""
        if self.carga_actual + peso <= self.capacidad_carga:
            self.carga_actual += peso
            return f"Cargados {peso} kg. Carga total: {self.carga_actual}/{self.capacidad_carga} kg"
        return f"Capacidad excedida. Solo puede cargar {self.capacidad_carga - self.carga_actual} kg más."
    
    def descargar(self, peso):
        """Descarga peso de la van"""
        if peso <= self.carga_actual:
            self.carga_actual -= peso
            return f"Descargados {peso} kg. Carga actual: {self.carga_actual} kg"
        return "No hay suficiente carga para descargar."
    
    def subir_pasajeros(self, cantidad):
        """Sube pasajeros a la van"""
        if self.pasajeros_actuales + cantidad <= self.capacidad_pasajeros:
            self.pasajeros_actuales += cantidad
            return f"{cantidad} pasajero(s) subieron. Total: {self.pasajeros_actuales}/{self.capacidad_pasajeros}"
        return f"Capacidad excedida. Solo caben {self.capacidad_pasajeros - self.pasajeros_actuales} pasajero(s) más."
    
    def bajar_pasajeros(self, cantidad):
        """Baja pasajeros de la van"""
        if cantidad <= self.pasajeros_actuales:
            self.pasajeros_actuales -= cantidad
            return f"{cantidad} pasajero(s) bajaron. Quedan: {self.pasajeros_actuales} pasajero(s)"
        return "No hay tantos pasajeros a bordo."
    
    def activar_climatizacion(self):
        """Activa el aire acondicionado"""
        if self.aire_acondicionado and self.encendido:
            return f"Climatización activada en {self.modelo}."
        return "Aire acondicionado no disponible o vehículo apagado."
    
    def mostrar_info(self):
        """Muestra información de la van"""
        info_base = super().mostrar_info()
        info_van = f"""Tipo de Servicio: {self.tipo_servicio}
Aire Acondicionado: {'Sí' if self.aire_acondicionado else 'No'}
Capacidad de Carga: {self.capacidad_carga} kg
Carga Actual: {self.carga_actual} kg
Pasajeros a Bordo: {self.pasajeros_actuales}/{self.capacidad_pasajeros}
{'='*50}
"""
        return info_base + info_van
from vehiculo import Vehiculo