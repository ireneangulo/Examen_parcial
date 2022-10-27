class Alumno:
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print("El alumno se ha creado con exito")
    def __str__(self):
        return "Nombre: {} \n\tNota: {}".format(self.nombre, self.nota)
    def calificacion(self):
        if self.nota <5: 
            print("El alumno {} ha suspendido".format(self.nombre))
        else: 
            print("El alumno {} ha aprobado ".format(self.nombre)) 
alumno1= Alumno("Irene", 10)
alumno2= Alumno("Daniel", 3)

print(alumno1)
print(alumno2)
        