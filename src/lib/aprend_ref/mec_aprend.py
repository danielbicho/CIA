# -*- coding: latin-1 -*-
'''
Mecanismo de aprendizagem por reforço
'''

import psa
from memoria_esparsa import MemoriaEsparsa as MemAprend
from aprend_q import AprendQ as AprendRef
from sel_accao_egreedy import SelAccaoEGreedy as SelAccao

class MecAprend:
    def __init__(self, accoes, alfa=1, gama=0.9, epsilon=0.01, nsim=100): 
        self._accoes = accoes
        self._mem_aprend = MemAprend()
        self._sel_accao = SelAccao(self._mem_aprend, self._accoes, epsilon)
        self._aprend_ref = AprendRef(self._mem_aprend, self._sel_accao, alfa, gama)
 
    def aprender(self, s, a, r, sn):
        self._aprend_ref.aprender(s, a, r, sn)
        self.mostrar(sn)

    def seleccionar_accao(self, s):
        return self._sel_accao.seleccionar_accao(s)
        
    def mostrar(self, s):
        psa.vis(1).limpar()
        psa.vis(1).aprendref(self._aprend_ref)
        psa.vis(2).accoesestado(s, self._accoes, self._mem_aprend.memoria)
        
