class Vehiculo:
    "Clase base para todos los vehículos"
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.encendido = False
        self.velocidad = 0
    
    def arranque(self):
        "Método para arrancar el vehículo"
        if not self.encendido:
            self.encendido = True
            return f"{self.modelo} ha sido arrancado."
        return f"{self.modelo} ya está encendido."
    
    def apagado(self):
        "Método para apagar el vehículo"
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.modelo} ha sido apagado."
        return f"{self.modelo} ya está apagado."
    
    def acelerar(self, incremento):
        "Método para acelerar el vehículo"
        if self.encendido:
            self.velocidad += incremento
            return f"{self.modelo} acelerando. Velocidad actual: {self.velocidad} km/h"
        return f"Debe arrancar el {self.modelo} primero."
    
    def frenar(self, decremento):
        "Método para frenar el vehículo"
        if self.velocidad > 0:
            self.velocidad = max(0, self.velocidad - decremento)
            return f"{self.modelo} frenando. Velocidad actual: {self.velocidad} km/h"
        return f"{self.modelo} ya está detenido."
    
    def mostrar_info(self):
        "Muestra información general del vehículo"
        info = f"""
{'='*50}
Información del Vehículo
{'='*50}
Modelo: {self.modelo}
Color: {self.color}
Motor: {self.motor}
Número de Puertas: {self.num_puertas}
Capacidad de Pasajeros: {self.capacidad_pasajeros}
Tipo de Combustible: {self.tipo_combustible}
Estado: {'Encendido' if self.encendido else 'Apagado'}
Velocidad: {self.velocidad} km/h
"""
        return info