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


# ============================================================
# DEMOSTRACIÓN DEL SISTEMA
# ============================================================

def main():
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE VEHÍCULOS CON HERENCIA")
    print("=" * 60)
    print()
    
    # Crear un Auto Deportivo
    print(">>> CREANDO AUTO DEPORTIVO <<<")
    deportivo = AutoDeportivo(
        modelo="Mazda RX-7",
        color="Azul Metálico",
        motor="3.0L Turbo",
        num_puertas=2,
        capacidad_pasajeros=2,
        tipo_combustible="Gasolina Premium",
        velocidad_maxima=250,
        tiempo_0_100=4.5,
        sistema_turbo=True
    )
    
    print(deportivo.mostrar_info())
    print(deportivo.arranque())
    print(deportivo.acelerar(50))
    print(deportivo.activar_turbo())
    print(deportivo.activar_modo_sport())
    print(deportivo.acelerar(80))
    print()
    
    # Crear una Van
    print(">>> CREANDO VAN <<<")
    van = Van(
        modelo="van Ford Transit",
        color="Blanco",
        motor="1.2L",
        num_puertas=4,
        capacidad_pasajeros=8,
        tipo_combustible="Gasolina",
        tipo_servicio="Transporte Público",
        aire_acondicionado=True,
        capacidad_carga=500
    )
    
    print(van.mostrar_info())
    print(van.arranque())
    print(van.subir_pasajeros(6))
    print(van.cargar(200))
    print(van.activar_climatizacion())
    print(van.acelerar(40))
    print()
    
    # Crear un Camión
    print(">>> CREANDO CAMIÓN <<<")
    camion = Camion(
        modelo="Torton Freightliner",
        color="Blanco",
        motor="6.7L Diesel",
        num_puertas=2,
        capacidad_pasajeros=3,
        tipo_combustible="Diesel",
        capacidad_carga_toneladas=8,
        num_ejes=2,
        tipo_carga="Volteo"
    )
    
    print(camion.mostrar_info())
    print(camion.arranque())
    print(camion.cargar_toneladas(5))
    print(camion.acelerar(30))
    print(camion.frenar(30))
    print(camion.levantar_volqueta())
    print(camion.descargar_toneladas(5))
    print(camion.bajar_volqueta())
    print()
    
    print("=" * 60)
    print("DEMOSTRACIÓN COMPLETADA")
    print("=" * 60)


if __name__== "__main__":
    main()