# -*- coding: latin-1 -*-
'''
Memória de aprendizagem
'''

#_______________________________________________________________________________

class MemoriaAprend(object):
    """Interface de memória de aprendizagem"""   
    def obter(self, s, a):
        raise NotImplementedError    
        
    def actualizar(self, s, a, q):
        raise NotImplementedError
