from Persona import Persona

class Empleado(Persona):
    
    def __init__(self):
        self.cargo = ""
        self.valorHora = ""
        self.horasTrabajadas = ""
        self.departamento = ""
        
    def pedirDatos(self):
        self.cargo = input("Ingrese su cargo: ")
        self.valorHora = int(input("Ingrese el valor de la hora: "))
        self.horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
        self.departamento = input("Ingrese su Departamento: ")
    def calcularHonorarios(self):
        honorarios = (self.valorHora * self.horasTrabajadas)-0.00966
        return honorarios
    
    def imprimirEmpleado(self):
        print(f"El empleado {self.nombre}{self.apellido} identificado con {self.tipoDoc} numero: {self.documento} del departamento: {self.departamento} en el cargo: {self.cargo} trabajo: {self.horasTrabajadas} a un valor de {self.valorHora} la hora.")