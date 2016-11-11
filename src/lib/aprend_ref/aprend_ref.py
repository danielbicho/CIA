# -*- coding: latin-1 -*-
'''
Método geral de aprendizagem por reforço
'''

#_______________________________________________________________________________

class AprendRef(object):
    def __init__(self, mem_aprend, sel_accao):
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao
    
    def aprender(self, s, a, r, sn):
        raise NotImplementedError
