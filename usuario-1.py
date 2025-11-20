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