# -*- coding: latin-1 -*-
'''
Mem�ria de aprendizagem
'''

#_______________________________________________________________________________

class MemoriaAprend(object):
    """Interface de mem�ria de aprendizagem"""   
    def obter(self, s, a):
        raise NotImplementedError    
        
    def actualizar(self, s, a, q):
        raise NotImplementedError
