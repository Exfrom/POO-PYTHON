
class Inicio:
    def __init__(self):
        self.persona1 = Persona()
        self.persona2 = Persona()

    def ejecutar(self):
        print("Datos de la Persona 1:")
        self.persona1.pedirDatos()
        print()
        print("Datos de la Persona 2:")
        self.persona2.pedirDatos()
        print()

        print("Mostrando datos de las personas:")
        self.persona1.mostrarPersona()
        print()
        self.persona2.mostrarPersona()
        print()

        print("Calculando el IMC de las personas:")
        imc_persona1 = self.persona1.calcularImc()
        imc_persona2 = self.persona2.calcularImc()
        print("IMC de la Persona 1:", imc_persona1)
        print("IMC de la Persona 2:", imc_persona2)
        print()

        print("Verificando si las personas son mayores de edad:")
        if self.persona1.mayorEdad():
            print("La Persona 1 es mayor de edad.")
        else:
            print("La Persona 1 no es mayor de edad.")

        if self.persona2.mayorEdad():
            print("La Persona 2 es mayor de edad.")
        else:
            print("La Persona 2 no es mayor de edad.")

        print()

        print("Verificando el estado de peso de las personas:")
        if imc_persona1 < 20:
            print("La Persona 1 tiene el peso por debajo de lo ideal.")
        elif 20 <= imc_persona1 <= 25:
            print("La Persona 1 tiene el peso ideal.")
        else:
            print("La Persona 1 tiene sobrepeso.")

        if imc_persona2 < 20:
            print("La Persona 2 tiene el peso por debajo de lo ideal.")
        elif 20 <= imc_persona2 <= 25:
            print("La Persona 2 tiene el peso ideal")