 
class Persona:
    def __init__(self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo):
        self.tipoDoc = tipoDoc
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.estatura = estatura
        self.edad = edad
        self.sexo = sexo

    def pedirDatos(self):
        self.tipoDoc = input("Tipo de documento: ")
        self.documento = input("Número de documento: ")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.peso = float(input("Peso en kg: "))
        self.estatura = float(input("Estatura en metros: "))
        self.edad = int(input("Edad: "))
        self.sexo = input("Sexo: ")

    def mostrarPersona(self):
        print("Datos de la persona:")
        print("Tipo de documento:", self.tipoDoc)
        print("Número de documento:", self.documento)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Peso:", self.peso, "kg")
        print("Estatura:", self.estatura, "m")
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)

    def calcularImc(self):
        peso_actual = self.peso / (self.estatura ** 2)
        return peso_actual

    def mayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False