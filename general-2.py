class Usuario:
    def __init__(self, nombre, apellido, edad, patrimonio):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._patrimonio = patrimonio

    # GETTERS
    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_edad(self):
        return self._edad

    def get_patrimonio(self):
        return self._patrimonio

    def __str__(self):
        return f"{self._nombre} {self._apellido} | Edad: {self._edad} | Patrimonio: {self._patrimonio}"


class BaseDatos:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.\n")
        else:
            print("\n--- LISTA DE USUARIOS ---")
            for u in self.usuarios:
                print(u)
            print()

    def buscar_por_nombre(self, nombre):
        for u in self.usuarios:
            if u.get_nombre().lower() == nombre.lower():
                return u
        return None


# ================ MENÚ PRINCIPAL ==================
def menu():
    bd = BaseDatos()

    while True:
        print("""
===== MENÚ DE USUARIOS =====
1. Registrar usuario
2. Listar usuarios
3. Buscar usuario por nombre
4. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO USUARIO ---")

            # Creamos el objeto directamente
            obj_usuario = Usuario(
                nombre=input("Nombre: "),
                apellido=input("Apellido: "),
                edad=int(input("Edad: ")),
                patrimonio=float(input("Patrimonio: "))
            )

            # Agregamos a la base de datos
            bd.agregar_usuario(obj_usuario)
            print(" Usuario registrado con éxito.\n")

        elif opcion == "2":
            bd.listar_usuarios()

        elif opcion == "3":
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            obj_usuario = bd.buscar_por_nombre(nombre_buscar)

            if obj_usuario:
                print("\nUsuario encontrado:")
                print(obj_usuario, "\n")
            else:
                print("No se encontró un usuario con ese nombre.\n")

        elif opcion == "4":
            print("Saliendo====")
            break

        else:
            print("Opción no válida.\n")


menu()