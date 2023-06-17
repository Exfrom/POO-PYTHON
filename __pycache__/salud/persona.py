 
class Persona:

#Metodos

    def __init__():
        """
        self.tipoDoc = tipoDoc
        self.documento= documento
        self.nombre = nombre
        self.apellidos =apellidos
        self.peso =peso
        self.estatura = estatura
        self.edad = edad
        self.genero = genero"""

    def pedirDatos(self):
        self.tipoDoc = input("Tipo de documento: ")
        self.documento = input("Número de documento: ")
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos")
        self.peso = int(input("Peso en kg: "))
        self.estatura = int(input("Estura en metros: "))
        self.edad = int(input("edad: "))
        self.genero = int("genero: ")
    
    """def mostrarPersona(self):
        print("Tipo de documento:", self.tipoDoc)
        print("Nombre de documento:", self.nombre)
        print("Apellidos de documento:", self.apellidos)
        print("Peso en kg:", self.peso)
        print("Estatura en metros:", self.estatura)
        print("Edad de documento: ", self.edad)
        print("Genero: ",self.genero)"""