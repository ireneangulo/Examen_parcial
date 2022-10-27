class Nodo(object):
    info, sig= None, None
class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor= valor
        self.termino= termino
class Polinonio(object): 
    def __init__(self):
        self.grado_mayor= 0
        self.contenido= {}
    def agregar_termino(self, grado, valor): 
        self.contenido[grado]= valor
        if self.grado_mayor < grado: 
            self.grado_mayor= grado
    def obtener_valor(self, grado):
        return self.contenido[int(grado)] 

        
       