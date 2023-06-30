 
class Persona:
    def __init__(self):
        self.tipoDoc = ""
        self.documento = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirDatos(self):
        self.tipoDoc = input("Tipo de documento: ")
        self.documento = input("Número de documento: ")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.peso = int(input("Peso en kg: "))
        self.estatura = int(input("Estatura en metros: "))
        self.edad = int(input("Edad: "))
        self.sexo = input("Sexo: ")

    def mostrarPersona(self):
        print(f"EL usuario {self.nombre} {self.apellido} con tipo de documento {self.tipoDoc} numero de documento: {self.documento} tiene una edad de: {self.edad} años,Tiene un peso de {self.peso} kg y mide {self.estatura} metros.")

    def calcularImc(self):
        peso = self.peso / (self.estatura ** 2)
        if peso < 20 :
            print("el peso esta por debajo")
        elif peso > 20 and peso < 26 :
            print("el peso es ideal")
        elif peso> 25 :
            print("estas en sobrepeso")
        return peso

    def mayorEdad(self):
        if self.edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")