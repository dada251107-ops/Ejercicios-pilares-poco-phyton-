from usuario import Usuario
from basedatos import BaseDatos


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

            obj_usuario = Usuario(
                nombre=input("Nombre: "),
                apellido=input("Apellido: "),
                edad=int(input("Edad: ")),
                patrimonio=float(input("Patrimonio: "))
            )

            bd.agregar_usuario(obj_usuario)
            print("Usuario registrado con éxito.\n")

        elif opcion == "2":
            bd.listar_usuarios()

        elif opcion == "3":
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            obj_usuario = bd.buscar_por_nombre(nombre_buscar)

            if obj_usuario:
                print("\nUsuario encontrado:")
                print(obj_usuario, "\n")
            else:
                print("❌ No se encontró un usuario con ese nombre.\n")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.\n")


menu()