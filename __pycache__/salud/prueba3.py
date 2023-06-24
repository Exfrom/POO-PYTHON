from  persona import Persona
from Inicio import Inicio

# Crear una instancia de la clase Persona
persona1 = Persona()

# Acceder a los métodos y atributos de la instancia persona1
persona1.pedirDatos()
persona1.mostrarPersona()
imc_persona1 = persona1.calcularImc()
es_mayor_edad_persona1 = persona1.mayorEdad()

# Crear otra instancia de la clase Persona
persona2 = Persona()

# Acceder a los métodos y atributos de la instancia persona2
persona2.pedirDatos()
persona2.mostrarPersona()
imc_persona2 = persona2.calcularImc()
es_mayor_edad_persona2 = persona2.mayorEdad()

# Crear una instancia de la clase Inicio
inicio = Inicio()

# Acceder a los métodos de la instancia inicio
inicio.ejecutar()