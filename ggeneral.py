# ==========================================
#            CLASE PADRE: BOTELLA
# ==========================================

class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    # ---------- Métodos Generales ----------
    def contener_liquidos(self):
        return "Puede contener líquidos."

    def facilitar_vertido(self):
        return "Facilita el vertido gracias a su diseño."

    def cierre_hermetico(self):
        return "Posee un cierre hermético."

    def transporte(self):
        return "Es apta para transportar líquidos."

    def manejo(self):
        return "Es fácil de manejar."

    def compatibilidad(self):
        return "Compatible con bebidas calientes y frías."

    def reutilizacion(self):
        return "Se puede reutilizar."

    def transparencia(self):
        return "Tiene cierto grado de transparencia."

    # ---------- Getters ----------
    def get_info(self):
        return {
            "Material": self.material,
            "Capacidad": self.capacidad,
            "Forma": self.forma,
            "Diseño": self.diseño,
            "Tapa": self.tapa,
            "Grabados": self.grabados
        }


# ===================================================
#     CLASE HIJA: BOTELLA PLÁSTICA (hereda Botella)
# ===================================================

class BotellaPlastica(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        super().__init__("Plástico", capacidad, forma, diseño, tapa, grabados)
        self.flexible = True
        self.reciclable = True

    def propiedades_plastico(self):
        return "Es liviana, flexible y resistente a golpes."


# ===================================================
#      CLASE HIJA: BOTELLA DE VIDRIO (hereda Botella)
# ===================================================

class BotellaVidrio(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        super().__init__("Vidrio", capacidad, forma, diseño, tapa, grabados)
        self.fragil = True
        self.mantiene_temperatura = True

    def propiedades_vidrio(self):
        return "Mantiene mejor la temperatura y es más frágil."


# ==========================================
#        BASE DE DATOS SIMULADA (LISTA)
# ==========================================

base_datos = []


# ==========================================
#               FUNCIÓN MENÚ
# ==========================================

def menu():
    while True:
        print("\n===== MENÚ BOTELLAS =====")
        print("1. Crear botella plástica")
        print("2. Crear botella de vidrio")
        print("3. Ver base de datos")
        print("4. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            crear_botella_plastica()

        elif opcion == "2":
            crear_botella_vidrio()

        elif opcion == "3":
            mostrar_base_datos()

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida.")


# ==========================================
#     FUNCIONES DEL MENÚ PARA CREAR OBJETOS
# ==========================================

def crear_botella_plastica():
    print("\n--- Crear Botella Plástica ---")
    cap = input("Capacidad: ")
    forma = input("Forma: ")
    diseño = input("Diseño: ")
    tapa = input("Tipo de tapa: ")
    grab = input("Grabados: ")

    obj = BotellaPlastica(cap, forma, diseño, tapa, grab)
    base_datos.append(obj)

    print("✓ Botella plástica añadida a la base de datos.")


def crear_botella_vidrio():
    print("\n--- Crear Botella de Vidrio ---")
    cap = input("Capacidad: ")
    forma = input("Forma: ")
    diseño = input("Diseño: ")
    tapa = input("Tipo de tapa: ")
    grab = input("Grabados: ")

    obj = BotellaVidrio(cap, forma, diseño, tapa, grab)
    base_datos.append(obj)

    print("✓ Botella de vidrio añadida a la base de datos.")


# ==========================================
#        MOSTRAR LA BASE DE DATOS
# ==========================================

def mostrar_base_datos():
    print("\n======= BASE DE DATOS =======")
    
    if not base_datos:
        print("No hay botellas registradas.")
        return

    for i, b in enumerate(base_datos):
        print(f"\nBotella #{i+1}")
        print(b.get_info())

        if isinstance(b, BotellaPlastica):
            print("Tipo: Plástica")
            print("Extra:", b.propiedades_plastico())

        if isinstance(b, BotellaVidrio):
            print("Tipo: Vidrio")
            print("Extra:", b.propiedades_vidrio())


# ==========================================
#            EJECUCIÓN DEL MENÚ
# ==========================================

menu()