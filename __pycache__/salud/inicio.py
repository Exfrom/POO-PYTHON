from Persona import Persona
from Empleado import Empleado
#Salud
#Instancio 
Persona1 = Persona()

Persona1.pedirDatos()
Persona1.mostrarPersona()
Persona1.calcularImc()
Persona1.mayorEdad()

#Persona2 = Persona()

#Persona2.pedirDatos()
#Persona2.mostrarPersona()
#Persona2.calcularImc()
#Persona2.mayorEdad()

#Empleado:

empleado1 = Empleado("cedula", 20897871,"diana","celis",45,38,"femenini","enfermera",3000,4, "enfermeria")

empleado1.pedirDatos()
empleado1.calcularHonorarios()
empleado1.imprimirEmpleado()
 
 

