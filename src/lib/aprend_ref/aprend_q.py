# -*- coding: latin-1 -*-
'''
Aprendizagem por reforço do tipo Q-Learning
'''

from aprend_ref import AprendRef

#_______________________________________________________________________________

class AprendQ(AprendRef):
    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        super(AprendQ, self).__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama
        
    def aprender(self, s, a, r, sn):
        # Implementar Q(s,a) ? Q(s,a) + ?[r + ? max a? Q(s?,a?) ? Q(s,a)]
        an = self._sel_accao.max_accao(sn)
        qsa = self._mem_aprend.obter(s, a)
        qsnan = self._mem_aprend.obter(sn, an)
        q = qsa + self._alfa * (r + self._gama * qsnan - qsa)
        self._mem_aprend.actualizar(s, a, q)
