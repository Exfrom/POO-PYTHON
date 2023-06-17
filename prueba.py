#crear objetos desde otros archivos , ojo importacion
from Animal import Animal
panda=animal()
panda.nombre="Bambu"
panda.edad=7

panda.registraranimal()
panda.mostrarAnimal()
print("la edad duplicada es",panda.duplicarEdad(panda.edad))
