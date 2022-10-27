class Alumno:
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print("El alumno se ha creado con exito")
    def calificacion(self):
        if self.nota <5: 
            print("El alumno {} ha suspendido".format(self.nombre))
        else: 
            print("El alumno {} ha aprobado ".format(self.nombre)) 
alumno1= Alumno("Irene", 10)
alumno2= Alumno("Daniel", 3)

alumno1.calificacion()
alumno2.calificacion()

        