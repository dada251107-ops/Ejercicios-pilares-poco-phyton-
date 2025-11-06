class Botella:
    """Clase principal (Padre) que representa una botella genérica"""
    
    def __init__(self, capacidad, forma, diseno, tapa, grabados="Sin grabados"):
        # Atributos comunes a todas las botellas
        self.capacidad = capacidad  # en ml
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados
        self.contenido_actual = 0
        self.esta_cerrado = True
        self.veces_reutilizado = 0
        self.temperatura_contenido = 20  
        # temperatura en °C
        
    def contener_liquidos(self, cantidad, tipo_liquido="agua"):
        """Llenar la botella con líquidos"""
        if cantidad <= self.capacidad:
            self.contenido_actual = cantidad
            return f" Botella llenada con {cantidad}ml de {tipo_liquido}"
        else:
            return f" Error: Capacidad máxima es {self.capacidad}ml"
    
    def facilitar_vertido(self):
        """Permite verter el contenido de la botella"""
        if not self.esta_cerrado and self.contenido_actual > 0:
            cantidad = self.contenido_actual
            self.contenido_actual = 0
            return f" Se vertieron {cantidad}ml"
        elif self.esta_cerrado:
            return " Error: La botella está cerrada"
        else:
            return " La botella está vacía"
    
    def cierre_hermetico(self, accion):
        """Controla el cierre hermético de la botella"""
        if accion == "cerrar":
            self.esta_cerrado = True
            return " Botella cerrada herméticamente"
        elif accion == "abrir":
            self.esta_cerrado = False
            return " Botella abierta"
    
    def transporte(self, destino):
        """Simula el transporte de la botella"""
        if self.esta_cerrado:
            return f" Botella transportada exitosamente a {destino}"
        else:
            return " Error: Cerrar la botella antes de transportar"
    
    def manejo(self):
        """Información sobre el manejo adecuado"""
        return f"Manejo: Sostener por la parte media de la botella"
    
    def reutilizacion(self):
        """Incrementa el contador de reutilización"""
        self.veces_reutilizado += 1
        return f" Botella reutilizada {self.veces_reutilizado} veces"
    
    def transparencia(self):
        """Método que será sobreescrito por las subclases"""
        return "Verificar transparencia según material"
    
    def mostrar_info(self):
        """Muestra toda la información de la botella"""
        info = f"""
========================================
=    INFORMACIÓN DE LA BOTELLA        =
========================================
  Capacidad: {self.capacidad}ml
  Forma: {self.forma}
  Diseño: {self.diseno}
  Tapa: {self.tapa}
  Grabados: {self.grabados}
  Contenido actual: {self.contenido_actual}ml
  Estado: {' Cerrado' if self.esta_cerrado else '🔓 Abierto'}
  Veces reutilizado: {self.veces_reutilizado}
  Temperatura: {self.temperatura_contenido}°C
        """
        return info


class BotellaPlastico(Botella):
   # """Subclase (Hijo) para botellas de plástico"""
    
    def __init__(self, capacidad, tipo_plastico="PET", color="Transparente", marca=""):
        # Llamar al constructor de la clase padre
        super().__init__(
            capacidad=capacidad,
            forma="Ergonómica con relieve",
            diseno=f"Botella plástica {color}",
            tapa="Rosca con seguridad",
            grabados=marca if marca else "Símbolo de reciclaje"
        )
        # Atributos específicos de botella de plástico
        self.material = "Plástico"
        self.tipo_plastico = tipo_plastico
        self.color = color
        self.reciclable = True
        self.peso = capacidad * 0.03  # gramos aproximados
        
    def compatibilidad_bebidas(self, tipo_bebida, temperatura):
        """Verifica compatibilidad específica para plástico"""
        bebidas_frias = ["agua", "jugo", "refresco", "té frío", "bebida deportiva"]
        
        if temperatura > 40:
            return f" Advertencia: No recomendado para {tipo_bebida} caliente en plástico"
        elif tipo_bebida in bebidas_frias:
            self.temperatura_contenido = temperatura
            return f" Compatible: {tipo_bebida} a {temperatura}°C"
        else:
            return f" Verificar: {tipo_bebida} - usar con precaución"
    
    def transparencia(self):
        """Transparencia específica para plástico"""
        if self.color == "Transparente":
            return " Botella transparente: contenido totalmente visible"
        else:
            return f" Botella {self.color}: contenido parcialmente visible"
    
    def resistencia_impacto(self):
        """Método específico de botellas plásticas"""
        return " Alta resistencia a impactos - No se rompe fácilmente"
    
    def reciclar(self):
        """Método específico para reciclaje de plástico"""
        if self.reciclable:
            codigo = "PET-1" if self.tipo_plastico == "PET" else "HDPE-2"
            return f" Botella reciclable - Código: {codigo}\n  Depositar en contenedor azul/amarillo"
        else:
            return " Consultar normativa de reciclaje local"
    
    def mostrar_info(self):
        """Sobreescribe el método del padre con info adicional"""
        info_base = super().mostrar_info()
        info_extra = f"""
  ═══ INFO ESPECÍFICA PLÁSTICO ═══
  Material: {self.material} ({self.tipo_plastico})
  Color: {self.color}
  Peso: {self.peso}g
  Reciclable: {'Sí' if self.reciclable else 'No'}
        """
        return info_base + info_extra


class BotellaVidrio(Botella):
    """Subclase (Hijo) para botellas de vidrio"""
    
    def __init__(self, capacidad, color_vidrio="Transparente", grosor="Estándar", marca=""):
        # Llamar a la clase padre
        super().__init__(
            capacidad=capacidad,
            forma="Cilíndrica clásica",
            diseno=f"Botella de vidrio {color_vidrio}",
            tapa="Corcho o tapa metálica",
            grabados=marca if marca else "Relieve en vidrio"
        )
        # Atributos específicos de botella de vidrio
        self.material = "Vidrio"
        self.color_vidrio = color_vidrio
        self.grosor = grosor
        self.peso = capacidad * 0.5
          # gramos aproximados (más pesado que plástico)
        self.resistente_calor = True
        
    def compatibilidad_bebidas(self, tipo_bebida, temperatura):
        """Verifica compatibilidad específica para vidrio"""
        if temperatura <= 100:
            self.temperatura_contenido = temperatura
            return f" Totalmente compatible: {tipo_bebida} a {temperatura}°C\n  El vidrio es apto para bebidas frías y calientes"
        else:
            return f" Temperatura muy alta ({temperatura}°C) - Riesgo de quemaduras al manipular"
    
    def transparencia(self):
        """Transparencia específica para vidrio"""
        colores_transparentes = ["Transparente", "Cristal"]
        if self.color_vidrio in colores_transparentes:
            return " Vidrio transparente: contenido completamente visible con claridad"
        else:
            return f" Vidrio {self.color_vidrio}: contenido protegido de la luz"
    
    def resistencia_impacto(self):
        """Método específico de botellas de vidrio"""
        if self.grosor == "Reforzado":
            return " Resistencia moderada - Vidrio reforzado, manipular con cuidado"
        else:
            return " Frágil - Puede romperse con impactos fuertes"
    
    def esterilizacion(self, temperatura_esterilizacion):
        """Método específico para vidrio - permite esterilización"""
        if temperatura_esterilizacion <= 120:
            return f" Botella esterilizada a {temperatura_esterilizacion}°C\n  El vidrio soporta altas temperaturas"
        else:
            return " Temperatura muy alta - riesgo de rotura térmica"
    
    def conservacion_sabor(self):
        """Ventaja específica del vidrio"""
        return "✓ Excelente: El vidrio no altera el sabor de las bebidas"
    
    def reciclar(self):
        """Método específico para reciclaje de vidrio"""
        return f"♻ Botella 100% reciclable indefinidamente\n  Depositar en contenedor verde (vidrio)"
    
    def mostrar_info(self):
        """Sobreescribe el método del padre con info adicional"""
        info_base = super().mostrar_info()
        info_extra = f"""
  ═══ INFO ESPECÍFICA VIDRIO ═══
  Material: {self.material}
  Color: {self.color_vidrio}
  Grosor: {self.grosor}
  Peso: {self.peso}g
  Resistente al calor: {'Sí' if self.resistente_calor else 'No'}
        """
        return info_base + info_extra


# ═══════════════════════════════════════════════════════
#     DEMOSTRACIÓN DEL ALGORITMO CON HERENCIA
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" + "═" * 60 + "=")
    print("=" + " " * 10 + "SISTEMA DE GESTIÓN DE BOTELLAS - POO" + " " * 14 + "=")
    print("=" + " " * 15 + "Clase Padre + 2 Clases Hijas" + " " * 18 + "=")
    print("=" + "═" * 60 + "=\n")
    
    # ============ BOTELLA DE PLÁSTICO ============
    print("\n" + "="*60)
    print("BOTELLA DE PLÁSTICO (Clase Hija 1)")
    print("="*60)
    
    botella_plastico = BotellaPlastico(
        capacidad=500,
        tipo_plastico="PET",
        color="Azul",
        marca="AquaPure Premium"
    )
    
    print(botella_plastico.mostrar_info())
    print("\n--- Operaciones con Botella de Plástico ---")
    print(botella_plastico.compatibilidad_bebidas("agua", 5))
    print(botella_plastico.contener_liquidos(500, "agua mineral"))
    print(botella_plastico.transparencia())
    print(botella_plastico.resistencia_impacto())
    print(botella_plastico.cierre_hermetico("cerrar"))
    print(botella_plastico.transporte("Gimnasio"))
    print(botella_plastico.reutilizacion())
    print(botella_plastico.reciclar())
    
    # ============ BOTELLA DE VIDRIO ============
    print("\n\n" + "="*60)
    print("BOTELLA DE VIDRIO (Clase Hija 2)")
    print("="*60)
    
    botella_vidrio = BotellaVidrio(
        capacidad=750,
        color_vidrio="Verde",
        grosor="Reforzado",
        marca="Viñedos Premium"
    )
    
    print(botella_vidrio.mostrar_info())
    print("\n--- Operaciones con Botella de Vidrio ---")
    print(botella_vidrio.compatibilidad_bebidas("vino tinto", 18))
    print(botella_vidrio.contener_liquidos(750, "vino tinto"))
    print(botella_vidrio.transparencia())
    print(botella_vidrio.resistencia_impacto())
    print(botella_vidrio.esterilizacion(100))
    print(botella_vidrio.conservacion_sabor())
    print(botella_vidrio.reciclar())
    
    # ============ COMPARACIÓN ============
    print("\n\n" + "="*60)
    print(" COMPARACIÓN DE BOTELLAS")
    print("="*60)
    
    print(f"\nPeso: Plástico={botella_plastico.peso}g vs Vidrio={botella_vidrio.peso}g")
    print(f"Material: Plástico={botella_plastico.material} vs Vidrio={botella_vidrio.material}")
    print(f"\nPolimorfismo - Método transparencia():")
    print(f"  Plástico: {botella_plastico.transparencia()}")
    print(f"  Vidrio: {botella_vidrio.transparencia()}")
    
    # ============ CICLO DE VIDA COMPLETO ============
    print("\n\n" + "="*60)
    print("CICLO DE EXPLICACION COMPLETO")
    print("="*60)
    
    botella_deportiva = BotellaPlastico(600, "HDPE", "Negro", "SpeedMax")
    print("\n  Creación:", "Botella de 600ml creada")
    print("  Llenado:", botella_deportiva.contener_liquidos(600, "bebida con gas"))
    print("  Verificación:", botella_deportiva.compatibilidad_bebidas("bebida isotónica", 10))
    print("  Cierre:", botella_deportiva.cierre_hermetico("cerrar"))
    print("  Transporte:", botella_deportiva.transporte("Parque"))
    print("  Apertura:", botella_deportiva.cierre_hermetico("abrir"))
    print("  Consumo:", botella_deportiva.facilitar_vertido())
    print("  Reutilización:", botella_deportiva.reutilizacion())
    print("  Reciclaje:", botella_deportiva.reciclar())
    
    print("\n" + "="*60)
    print(" DEMOSTRACIÓN COMPLETADA")
    print("="*60)