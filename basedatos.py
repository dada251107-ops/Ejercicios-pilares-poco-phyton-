from usuario import Usuario

class BaseDatos:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario: Usuario):
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