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
    def restar(self, polinomio1, polinomio2): 
        menor= polinomio1 if (polinomio1.grado_mayor< polinomio2.grado_mayor) else polinomio2
        mayor= polinomio2 if (menor==polinomio1) else polinomio1
        self.contenido= mayor.contenido
        for i in range(0, menor.grado_mayor + 1):
            try: 
                mayor_valor= 0 if mayor.existe_grado(i) is False else mayor.obtener_valor(i)
                menor_valor= 0 if menor.existe_grado(i) is False else menor.obtener_valor(i)
                total = mayor_valor - menor_valor
                if self.existe_grado (i):
                    self.elimina_grado(i)
                if total != 0: 
                    self.agregar_termino(i, total)
            except: 
                self.agregar_termino(i, total)
                pass
        
       