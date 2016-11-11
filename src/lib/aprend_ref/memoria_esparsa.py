# -*- coding: latin-1 -*-
'''
Memoria de aprendizagem do tipo memória esparsa
'''

from memoria_aprend import MemoriaAprend

#_______________________________________________________________________________

class MemoriaEsparsa(MemoriaAprend):
    def __init__(self, valor_omissao=0.0):
        self._valor_omissao = valor_omissao
        self._memoria = {}
        
    @property
    def memoria(self):
        return self._memoria
        
    def obter(self, s, a):
        return self._memoria.get((s, a), self._valor_omissao)
    
    def actualizar(self, s, a, q):
        self._memoria[(s, a)] = q
