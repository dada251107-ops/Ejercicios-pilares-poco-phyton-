class AutoDeportivo(Vehiculo):
    """Clase para autos deportivos - Hereda de Vehiculo"""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, 
                 tipo_combustible, velocidad_maxima, tiempo_0_100, sistema_turbo):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        # Atributos únicos del auto deportivo
        self.velocidad_maxima = velocidad_maxima
        self.tiempo_0_100 = tiempo_0_100
        self.sistema_turbo = sistema_turbo
        self.turbo_activado = False
        self.modo_sport = False
    
    def activar_turbo(self):
        """Activa el sistema turbo del auto deportivo"""
        if self.sistema_turbo and self.encendido:
            self.turbo_activado = True
            return f"¡Turbo activado en {self.modelo}! Potencia aumentada."
        return "Sistema turbo no disponible o vehículo apagado."
    
    def desactivar_turbo(self):
        """Desactiva el sistema turbo"""
        self.turbo_activado = False
        return f"Turbo desactivado en {self.modelo}."
    
    def activar_modo_sport(self):
        """Activa el modo deportivo"""
        if self.encendido:
            self.modo_sport = True
            return f"Modo Sport activado en {self.modelo}. ¡Máximo rendimiento!"
        return "Debe encender el vehículo primero."
    
    def acelerar(self, incremento):
        """Sobrescribe el método acelerar con características deportivas"""
        if self.encendido:
            multiplicador = 1.5 if self.turbo_activado else 1.0
            multiplicador *= 1.2 if self.modo_sport else 1.0
            incremento_real = int(incremento * multiplicador)
            self.velocidad = min(self.velocidad + incremento_real, self.velocidad_maxima)
            estado = []
            if self.turbo_activado:
                estado.append("TURBO")
            if self.modo_sport:
                estado.append("SPORT")
            estado_str = f" [{' + '.join(estado)}]" if estado else ""
            return f"{self.modelo} acelerando{estado_str}. Velocidad: {self.velocidad}/{self.velocidad_maxima} km/h"
        return f"Debe arrancar el {self.modelo} primero."
    
    def mostrar_info(self):
        """Muestra información del auto deportivo"""
        info_base = super().mostrar_info()
        info_deportivo = f"""Velocidad Máxima: {self.velocidad_maxima} km/h
0-100 km/h: {self.tiempo_0_100} segundos
Sistema Turbo: {'Sí' if self.sistema_turbo else 'No'}
Turbo Activado: {'Sí' if self.turbo_activado else 'No'}
Modo Sport: {'Activado' if self.modo_sport else 'Desactivado'}
{'='*50}
"""
        return info_base + info_deportivo


from vehiculo import Vehiculo