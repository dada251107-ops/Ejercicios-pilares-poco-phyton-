from animal import Animal
from caballo import Caballo
from caiman import Caiman
from escarabajo import EscarabajoRinoceronte
from pato import Pato
from pez import Pez
# Crear instancias de cada clase


print("=== Animales ===")
animales = [Animal,Caballo, Caiman, EscarabajoRinoceronte, Pato, Pez]
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
        nombre="juan", 
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
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
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
            print("\n Opción inválida! Por favor seleccione una opción del 1 al 5.")


# EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    menu_principal()

