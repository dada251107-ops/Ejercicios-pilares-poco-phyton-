class Camion(Vehiculo):
    """Clase para camiones de carga - Hereda de Vehiculo"""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros,
                 tipo_combustible, capacidad_carga_toneladas, num_ejes, tipo_carga):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        # Atributos únicos del camión
        self.capacidad_carga_toneladas = capacidad_carga_toneladas
        self.num_ejes = num_ejes
        self.tipo_carga = tipo_carga  # Ej: "Volteo", "Plataforma", "Refrigerado"
        self.carga_actual = 0
        self.volqueta_levantado = False
    
    def cargar_toneladas(self, toneladas):
        """Carga toneladas en el camión"""
        if self.carga_actual + toneladas <= self.capacidad_carga_toneladas:
            self.carga_actual += toneladas
            return f"Cargadas {toneladas} ton. Carga total: {self.carga_actual}/{self.capacidad_carga_toneladas} ton"
        return f"Capacidad excedida. Solo puede cargar {self.capacidad_carga_toneladas - self.carga_actual} ton más."
    
    def descargar_toneladas(self, toneladas):
        """Descarga toneladas del camión"""
        if toneladas <= self.carga_actual:
            self.carga_actual -= toneladas
            return f"Descargadas {toneladas} ton. Carga actual: {self.carga_actual} ton"
        return "No hay suficiente carga para descargar."
    
    def levantar_volqueta(self):
        """Levanta el volqueta del camión (si aplica)"""
        if self.tipo_carga == "Volteo" and not self.volqueta_levantado and self.velocidad == 0:
            self.volqueta_levantado = True
            return f"Volqueta levantado en {self.modelo}. Listo para descargar."
        elif self.velocidad > 0:
            return "Debe detener el camión antes de levantar el volqueta."
        return "Este camión no tiene sistema de volteo."
    
    def bajar_volqueta(self):
        """Baja el volqueta del camión"""
        if self.volqueta_levantado:
            self.volqueta_levantado = False
            return f"Volqueta bajado en {self.modelo}."
        return "El volqueta ya está abajo."
    
    def acelerar(self, incremento):
        """Sobrescribe acelerar considerando el peso de la carga"""
        if self.encendido:
            # El camión acelera más lento si está cargado
            factor_carga = 1 - (self.carga_actual / self.capacidad_carga_toneladas) * 0.5
            incremento_real = int(incremento * factor_carga)
            self.velocidad += incremento_real
            estado_carga = f"[Carga: {self.carga_actual}t]" if self.carga_actual > 0 else ""
            return f"{self.modelo} acelerando {estado_carga}. Velocidad: {self.velocidad} km/h"
        return f"Debe arrancar el {self.modelo} primero."
    
    def mostrar_info(self):
        """Muestra información del camión"""
        info_base = super().mostrar_info()
        info_camion = f"""Capacidad de Carga: {self.capacidad_carga_toneladas} toneladas
Carga Actual: {self.carga_actual} toneladas
Número de Ejes: {self.num_ejes}
Tipo de Carga: {self.tipo_carga}
Volqueta: {'Levantado' if self.volqueta_levantado else 'Abajo'}
{'='*50}
"""
        return info_base + info_camion
from vehiculo import Vehiculo