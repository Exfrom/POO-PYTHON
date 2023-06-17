 
class persona:

#Metodo
    def __init__(self,tipoDoc,nombre,apellidos,peso,estatura,edad,genero):
        self.tipoDoc = tipoDoc
        self.nombre = nombre
        self.apellidos =apellidos
        self.peso =peso
        self.estatura = estatura
        self.edad = edad
        self.genero = genero

    def pedirDatos(self):
        self.tipoDoc = input("Tipo de documento: ")
        self.documento = input("Número de documento: ")
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos")
        self.peso = float(input("Peso en kg: "))
        self.estatura = float(input("Estura en metros: "))
        self.edad = int(input("edad: "))
        self.genero = int("genero: ")