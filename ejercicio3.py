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

        