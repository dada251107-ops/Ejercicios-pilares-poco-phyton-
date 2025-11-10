class Animal:
    def __init__(self,  nombre, edad, habitat, dieta, tamaño,color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color
    def moverse(self):
        "el animal esta moviendose"
        if not self.moverse:
            self.moverse
            return f" {self,Animal.nombre} se esta moviendo"
    
    def comunicacion(self):
        "el animal esta comunicandose"
        if not self.comunicacion:
            self.comunicacion
            return f" {self,Animal.nombre} puede comunicarse"
    def alimentacion(self):
        "el animal esta alimentandose"
        if not self.alimentacion:
            self.alimentacion
            return f" {self,Animal.nombre} se peude alimentar"
    
    def reproducirse(self):
        "el animal se esta reproduciendo"
        if not self.reproducirse:
            self.reproducirse
            return f" {self,Animal.nombre} se puede reproducir"

    def adaptaccion(self):
        "el animal se esta adaptando"
        if not self.adaptaccion:
            self.adaptaccion
            return f" {self,Animal.nombre} se puede adaptar a su entorno"
    def dormir(self):
        "el animal esta durmiendo"
        if not self.dormir:
            self.dormir
            return f" {self,Animal.nombre} pede descansar durmiendo"
    def instintos(self):
        "el animal esta siguiendo sus instintos"
        if not self.instintos:
            self.instintos
            return f" {self,Animal.nombre} sigue sus instintos naturales"
    def sentidos(self):
        "el animal esta usando sus sentidos"
        if not self.sentidos:
            self.sentidos
            return f" {self,Animal.nombre} usa sus sentidos para interactuar con el entorno"
    def descanso(self):
        "el animal esta descansando"
        if not self.descanso:
            self.descanso
            return f" {self,Animal.nombre} esta descansando para recuperar energias"
    def interaccion(self):
        "el animal esta interactuando"
        if not self.interaccion:
            self.interaccion
            return f" {self,Animal.nombre} interactua con otros seres vivos y su entorno"
        
def mostrar_info(self):
       "muestra informacion del animal "
       info=f"""n
nombre: {self.nombre}
edad: {self.edad}
habitat: {self.habitat}
dieta: {self.dieta}
tamaño: {self.tamaño}
color: {self.color}
"""
       return info  

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño,color, tipo_pelo, periodo_gestacion):
        super().__init__(nombre, edad, habitat, dieta, tamaño,color)
        self.tipo_pelo = tipo_pelo
        self.periodo_gestacion = periodo_gestacion
    