from class_botellahijo1 import BotellaVidrio
from class_botellahijo2 import BotellaPlastico
from class_botella import Botella

class_botella= Botella()
Class_botellahijo1 = BotellaVidrio()
Class_botellahijo2 = BotellaPlastico()
def main():
    print("=== SISTEMA DE BOTELLAS ===\n")

    # Crear objetos
    vidrio = BotellaVidrio(1.5, "transparente")
    plastico = BotellaPlastico(1.0, True)

    # Mostrar información de cada una
    print(vidrio.descripcion())
    print(vidrio.contener_liquidos())
    print(vidrio.cierre_hermetico())
    print(vidrio.reutilizacion())
    print(vidrio.cuidado())

    print("\n----------------------------\n")

    print(plastico.descripcion())
    print(plastico.transporte())
    print(plastico.facilitar_vertido())
    print(plastico.compatibilidad())
    print(plastico.cuidado())

if __name__ == "_main_":
    main()
