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
