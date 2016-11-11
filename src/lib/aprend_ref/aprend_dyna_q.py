# -*- coding: latin-1 -*-
'''
Aprendizagem por reforço do tipo Dyna-Q
'''
    
#_______________________________________________________________________________

class AprendDynaQ(AprendQ):
    def __init__(self, mem_aprend, sel_accao, alfa, gama, nsim=100):
        raise NotImplementedError
        
    def iniciar_modelo(self):
        raise NotImplementedError
        
    def actualizar_modelo(self, s, a, r, sn):
        raise NotImplementedError

    def aprender(self, s, a, r, sn):        
        raise NotImplementedError

    def simular(self):
        raise NotImplementedError

