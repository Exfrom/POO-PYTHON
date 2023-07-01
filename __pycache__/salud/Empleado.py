from Persona import Persona

class Empleado(Persona):
    cargo = ""
    valorHora = 0
    horasTrabajadas = 0 
    departamento=""
    honorarios = 0
  
    def __init__(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo,cargo,valorHora,horasTrabajadas,departamento ):
        super().__init__(tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo)
        self.cargo= cargo
        self.valorHora= valorHora
        self.horasTrabajadas= horasTrabajadas
        self.departamento= departamento
       
    def pedirDatos(self):
        self.cargo = input("Ingrese su cargo: ")
        self.valorHora = int(input("Ingrese el valor de la hora: "))
        self.horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
        self.departamento = input("Ingrese su Departamento: ")
    def calcularHonorarios(self):
        honorarios = (self.valorHora * self.horasTrabajadas)-0.00966
        return honorarios
        
    def imprimirEmpleado(self):
        print(f"El empleado {self.nombre}{self.apellido} identificado con {self.tipoDoc} numero: {self.documento} del departamento: {self.departamento} en el cargo: {self.cargo} trabajo: {self.horasTrabajadas} a un valor de {self.valorHora} la hora y un total de honorarios a pagar de {self.calcularHonorarios()}")