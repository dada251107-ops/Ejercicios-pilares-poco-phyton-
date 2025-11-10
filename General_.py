# Sistema de Gestión de Animales - Programación Orientada a Objetos

class Animal:
    """Clase padre que define los atributos y métodos comunes de todos los animales"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        # Atributos comunes (según la imagen)
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
    
    # Métodos comunes (según la imagen)
    def moverse(self):
        return f"{self.nombre} se está moviendo"
    
    def comunicacion(self):
        return f"{self.nombre} puede comunicarse con seres vivios en su entorno"
    
    def reproduccion(self):
        return f"{self.nombre} puede reproducirse"
    
    def alimentarse(self):
        return f"{self.nombre} se está alimentando con {self.dieta}"
    
    def adaptacion(self):
        return f"{self.nombre} se adapta a su entorno"
    
    def instintos(self):
        return f"{self.nombre} sigue sus instintos naturales"
    
    def descanso(self):
        return f"{self.nombre} está descansar en su hábitat"
    
    def sueno(self):
        return f"{self.nombre} puede dormir para recuperar energías"
    
    def interaccion_social(self):
        return f"{self.nombre} interactúa socialmente"
    
    def describir(self):
        """Descripción detallada del animal"""
        return f"{self.nombre} es un animal que habita en {self.habitat}"
    
    def mostrar_info(self):
        """Muestra toda la información del animal"""
        print(f"\n{'='*50}")
        print(f"informacio sobre: {self.nombre.upper()}")
        print(f"{'='*50}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamano}")
        print(f"Color: {self.color}")


class Caballo(Animal):
    """Clase hija - Representa a un caballo con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, raza, velocidad_max):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del caballo
        self.raza = raza
        self.velocidad_max = velocidad_max
        self.tipo = "Mamífero terrestre"
        self.numero_patas = 4
    
    def moverse(self):
        return f"{self.nombre} galopa a una velocidad máxima de {self.velocidad_max} km/h"
    
    def comunicacion(self):
        return f"{self.nombre} relincha para comunicarse con otros caballos"
    
    def trotar(self):
        """Método específico del caballo"""
        return f"{self.nombre} está trotando elegantemente por el campo"
    
    def describir(self):
        """Descripción detallada del caballo"""
        return (f"{self.nombre} es un hermoso caballo de raza {self.raza} con pelaje {self.color}. "
                f"Es un mamífero herbívoro que vive en {self.habitat}. Tiene {self.numero_patas} patas "
                f"fuertes y musculosas que le permiten alcanzar velocidades de hasta {self.velocidad_max} km/h. "
                f"Los caballos son animales sociales que se comunican mediante relinchos y movimientos corporales.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Raza: {self.raza}")
        print(f"Velocidad máxima: {self.velocidad_max} km/h")
        print(f"Número de patas: {self.numero_patas}")


class Caiman(Animal):
    """Clase hija - Representa a un caimán con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, longitud, fuerza_mordida):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del caimán
        self.longitud = longitud
        self.fuerza_mordida = fuerza_mordida
        self.tipo = "Reptil acuático"
        self.numero_dientes = 80
    
    def moverse(self):
        return f"{self.nombre} se desplaza nadando con su poderosa cola y caminando en tierra"
    
    def comunicacion(self):
        return f"{self.nombre} emite gruñidos y silbidos para comunicarse"
    
    def cazar(self):
        """Método específico del caimán"""
        return f"{self.nombre} acecha pacientemente a su presa bajo el agua"
    
    def tomar_sol(self):
        """Método específico del caimán"""
        return f"{self.nombre} está termorregulando su cuerpo tomando el sol en la orilla"
    
    def describir(self):
        """Descripción detallada del caimán"""
        return (f"{self.nombre} es un imponente caimán de {self.longitud} metros de longitud con piel {self.color}. "
                f"Es un reptil carnívoro que habita en {self.habitat}. Su mandíbula puede ejercer una fuerza de "
                f"{self.fuerza_mordida} PSI, siendo uno de los depredadores más temidos de su ecosistema. "
                f"Tiene aproximadamente {self.numero_dientes} dientes afilados. Los caimanes son reptiles de sangre fría "
                f"que pasan tiempo tanto en el agua como en tierra firme.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Longitud: {self.longitud} metros")
        print(f"Fuerza de mordida: {self.fuerza_mordida} PSI")
        print(f"Número de dientes: {self.numero_dientes}")


class Pez(Animal):
    """Clase hija - Representa a un pez con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, especie, profundidad_max):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del pez
        self.especie = especie
        self.profundidad_max = profundidad_max
        self.tipo = "Vertebrado acuático"
        self.numero_aletas = 7
    
    def moverse(self):
        return f"{self.nombre} nada ágilmente usando sus aletas"
    
    def comunicacion(self):
        return f"{self.nombre} se comunica mediante movimientos corporales y señales visuales"
    
    def nadar(self):
        """Método específico del pez"""
        return f"{self.nombre} nada hasta {self.profundidad_max} metros de profundidad"
    
    def respirar_agua(self):
        """Método específico del pez"""
        return f"{self.nombre} respira oxígeno disuelto en el agua mediante sus branquias"
    
    def describir(self):
        """Descripción detallada del pez"""
        return (f"{self.nombre} es un pez {self.especie} de colores {self.color} brillantes. "
                f"Es un vertebrado acuático que vive en {self.habitat} y se alimenta de {self.dieta}. "
                f"Puede sumergirse hasta {self.profundidad_max} metros de profundidad. Tiene {self.numero_aletas} aletas "
                f"que le permiten maniobrar con precisión en el agua. Los peces respiran a través de branquias "
                f"que extraen oxígeno del agua.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Especie: {self.especie}")
        print(f"Profundidad máxima: {self.profundidad_max} metros")
        print(f"Número de aletas: {self.numero_aletas}")


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


class Pato(Animal):
    """Clase hija - Representa a un pato con características específicas"""
    
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_plumaje, puede_volar):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        # Atributos propios del pato
        self.tipo_plumaje = tipo_plumaje
        self.puede_volar = puede_volar
        self.tipo = "Ave acuática"
        self.numero_patas = 2
    
    def moverse(self):
        movimiento = "vuela, nada y camina" if self.puede_volar else "nada y camina"
        return f"{self.nombre} {movimiento} con facilidad"
    
    def comunicacion(self):
        return f"{self.nombre} grazna en diferentes tonos para comunicarse"
    
    def volar(self):
        """Método específico del pato"""
        if self.puede_volar:
            return f"{self.nombre} vuela sobre el agua batiendo sus alas"
        return f"{self.nombre} no puede volar pero es excelente nadador"
    
    def nadar(self):
        """Método específico del pato"""
        return f"{self.nombre} nada en la superficie del agua usando sus patas palmeadas"
    
    def describir(self):
        """Descripción detallada del pato"""
        vuelo = "puede volar largas distancias" if self.puede_volar else "ha perdido la capacidad de vuelo"
        return (f"{self.nombre} es un pato con hermoso plumaje {self.tipo_plumaje} de color {self.color}. "
                f"Es un ave acuática omnívora que habita en {self.habitat} y se alimenta de {self.dieta}. "
                f"{self.nombre} {vuelo}, pero siempre es un excelente nadador gracias a sus patas palmeadas. "
                f"Su plumaje impermeable lo mantiene seco mientras nada. Los patos tienen {self.numero_patas} patas "
                f"y son animales sociales que viven en grupos.")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Tipo de plumaje: {self.tipo_plumaje}")
        print(f"Puede volar: {'Sí' if self.puede_volar else 'No'}")
        print(f"Número de patas: {self.numero_patas}")


# BASE DE DATOS DE ANIMALES
def base_datos():
    """Crea una base de datos con ejemplos de cada tipo de animal"""
    animales = []
    
    # Crear instancias de cada animal con datos realistas
    caballo1 = Caballo(
        nombre="Spirit", 
        edad=7, 
        habitat="Praderas y establos", 
        dieta="Herbívoro (pasto, heno, avena)", 
        tamano="Grande (450-500kg)", 
        color="Castaño oscuro con crines negras", 
        raza="Mustang", 
        velocidad_max=70
    )
    
    caiman1 = Caiman(
        nombre="Croco", 
        edad=15, 
        habitat="Ríos y pantanos tropicales", 
        dieta="Carnívoro (peces, aves, mamíferos)", 
        tamano="Grande (200kg)", 
        color="Verde oscuro con vientre amarillento", 
        longitud=3.5, 
        fuerza_mordida=3700
    )
    
    pez1 = Pez(
        nombre="Nemo", 
        edad=2, 
        habitat="Arrecifes de coral del Océano Pacífico", 
        dieta="Omnívoro (algas, plancton, anémonas)", 
        tamano="Pequeño (0.1kg)", 
        color="Naranja brillante con franjas blancas", 
        especie="Pez payaso (Amphiprioninae)", 
        profundidad_max=15
    )
    
    escarabajo1 = EscarabajoRinoceronte(
        nombre="Hércules", 
        edad=1, 
        habitat="Bosques tropicales y selvas húmedas", 
        dieta="Herbívoro (frutas, savia, madera en descomposición)", 
        tamano="Pequeño (0.05kg)", 
        color="Negro brillante con reflejos verdes", 
        longitud_cuerno=4.5, 
        peso_soportado=850
    )
    
    pato1 = Pato(
        nombre="Donald", 
        edad=3, 
        habitat="Lagos, estanques y humedales", 
        dieta="Omnívoro (semillas, insectos, plantas acuáticas)", 
        tamano="Mediano (1.2kg)", 
        color="Verde esmeralda en cabeza, cuerpo gris y blanco", 
        tipo_plumaje="Impermeable", 
        puede_volar=True
    )
    
    animales.extend([caballo1, caiman1, pez1, escarabajo1, pato1])
    return animales


def mostrar_descripcion_completa(animal):
    """Muestra la descripción narrativa completa de un animal"""
    print("\n" + "="*70)
    print(f"descripcion completa de {animal.nombre.upper()}")
    print("="*70)
    print(f"\n{animal.describir()}")
    print("\n" + "-"*70)


def menu_principal():
    """Sistema interactivo para gestionar y mostrar información de animales"""
    print("\n" + "="*70)
    print("SISTEMA DE GESTIÓN DE ANIMALES - PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("="*70)
    print("Animales disponibles: Caballo, Caimán, Pez, Escarabajo Rinoceronte, Pato")
    
    animales = base_datos()
    
    while True:
        print("\n" + "="*70)
        print("--- MENÚ PRINCIPAL ---")
        print("="*70)
        print("1. Mostrar lista de todos los animales")
        print("2. Ver descripción completa de un animal")
        print("3. Mostrar información técnica de un animal")
        print("4. Ejecutar métodos (acciones) de un animal")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == "1":
            print("\n" + "="*70)
            print("--- LISTA DE ANIMALES REGISTRADOS ---")
            print("="*70)
            for i, animal in enumerate(animales, 1):
                print(f"{i}. {animal.nombre:15} - {animal.__class__.__name__:20} ({animal.tipo})")
        
        elif opcion == "2":
            print("\n" + "="*70)
            print("--- SELECCIONAR ANIMAL PARA DESCRIPCIÓN ---")
            print("="*70)
            for i, animal in enumerate(animales, 1):
                print(f"{i}. {animal.nombre} ({animal.__class__.__name__})")
            
            try:
                seleccion = int(input("\nIngrese el número del animal: ")) - 1
                if 0 <= seleccion < len(animales):
                    mostrar_descripcion_completa(animales[seleccion])
                else:
                    print("\nOpción inválida")
            except ValueError:
                print("\nEntrada inválida! Debe ingresar un número.")
        
        elif opcion == "3":
            print("\n" + "="*70)
            print("--- INFORMACIÓN TÉCNICA DEL ANIMAL ---")
            print("="*70)
            for i, animal in enumerate(animales, 1):
                print(f"{i}. {animal.nombre}")
            
            try:
                seleccion = int(input("\nIngrese el número del animal: ")) - 1
                if 0 <= seleccion < len(animales):
                    animales[seleccion].mostrar_info()
                else:
                    print("\n Opción inválida")
            except ValueError:
                print("\nEntrada inválida")
        
        elif opcion == "4":
            print("\n" + "="*70)
            print("--- EJECUTAR MÉTODOS DEL ANIMAL ---")
            print("="*70)
            for i, animal in enumerate(animales, 1):
                print(f"{i}. {animal.nombre}")
            
            try:
                seleccion = int(input("\nIngrese el número del animal: ")) - 1
                if 0 <= seleccion < len(animales):
                    animal = animales[seleccion]
                    print(f"\n{'='*70}")
                    print(f"acciones sobre {animal.nombre.upper()} ({animal.__class__.__name__})")
                    print(f"{'='*70}")
                    
                    # Métodos comunes
                    print("\n🔹 MÉTODOS COMUNES:")
                    print(f"   • {animal.moverse()}")
                    print(f"   • {animal.comunicacion()}")
                    print(f"   • {animal.alimentarse()}")
                    print(f"   • {animal.descanso()}")
                    print(f"   • {animal.interaccion_social()}")
                    
                    # Métodos específicos según el tipo
                    print("\n🔸 MÉTODOS ESPECÍFICOS:")
                    if isinstance(animal, Caballo):
                        print(f"   • {animal.trotar()}")
                    elif isinstance(animal, Caiman):
                        print(f"   • {animal.cazar()}")
                        print(f"   • {animal.tomar_sol()}")
                    elif isinstance(animal, Pez):
                        print(f"   • {animal.nadar()}")
                        print(f"   • {animal.respirar_agua()}")
                    elif isinstance(animal, EscarabajoRinoceronte):
                        print(f"   • {animal.usar_cuerno()}")
                        print(f"   • {animal.levantar_peso()}")
                    elif isinstance(animal, Pato):
                        print(f"   • {animal.volar()}")
                        print(f"   • {animal.nadar()}")
                else:
                    print("\n Opción inválida")
            except ValueError:
                print("\n Entrada inválida")
        
        elif opcion == "5":
            print("\n" + "="*70)
            print("¡Gracias por usar el Sistema de Gestión de Animales!")
            print("="*70)
            break
        
        else:
            print("\n Opción inválida! Por favor seleccione una opción del 1 al 6.")


# EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    menu_principal()