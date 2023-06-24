
class Inicio:
    def __init__(self):
        self.persona1 = Persona("", "", "", "", 0, 0, 0, "")
        self.persona2 = Persona("", "", "", "", 0, 0, 0, "")

    def ejecutar(self):
        print("Ingrese los datos de la persona 1:")
        self.persona1.pedirDatos()
        print("Ingrese los datos de la persona 2:")
        self.persona2.pedirDatos()

        print("\nDatos de la persona 1:")
        self.persona1.mostrarPersona()
        print("\nDatos de la persona 2:")
        self.persona2.mostrarPersona()

        print("\nPersona 1:")
        peso_actual_persona1 = self.persona1.calcularImc()
        if peso_actual_persona1 < 20:
            print("El peso está por debajo de lo ideal")
        elif 20 <= peso_actual_persona1 <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")

        print("\nPersona 2:")
        peso_actual_persona2 = self.persona2.calcularImc()
        if peso_actual_persona2 < 20:
            print("El peso está por debajo de lo ideal")
        elif 20 <= peso_actual_persona2 <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")


