class Animal:
    #Atributos
    nombre=""#Atrubuto estatico
    edad=0

    #Metodo
    def __init__(self,n,e):
        self.nombre = n
        self.edad = e
    #Metodos propios clase
    def registroAnimal(self):
        self.nombre=input("Ingrese el nombre del animal")
        self.edad=int(input("Ingrese la edad del animal"))
    def mostrarAnimal(self):
        print("El nombre de animal es:",self.nombre,"la edad del animal es",self.edad)
        #
    def cambiarNombre(self):
        cambiarNombre:input("Digite el nuevo nombre: ")
        self.nombre=cambiarNombre
        print("El nuevo nombre es",self.nombre)
#metodo retorno y que tenga parametro
# duplicar edad, pedir la edad, retornar la edad duplicada
    def duplicarEdad(self,edad):
        duplicar=edad*2
        return duplicar


#crear objeto o instancia clase
 
#tigre =Animal()
#tigre.nombre="Tony"
#tigre.edad = 1
#print("El nombre del animal es ",tigre.nombre, "y su edad es",tigre.edad)


#tigre.nombre="panda"
#tigre.edad = 7
#print("El nombre del animal es ",tigre.nombre, "y su edad es",tigre.edad)
 