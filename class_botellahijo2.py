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