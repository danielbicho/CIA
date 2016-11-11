# -*- coding: latin-1 -*-
'''
Controlo de aprendizagem por reforço
'''

from psa.accao import Mover
from psa.util import dirmov

from agente_prosp.controlo import  Controlo
from mec_motiv import MecMotiv
from aprend_ref.mec_aprend import MecAprend
#_______________________________________________________________________________

class ControloAprendRef(Controlo):
    def __init__(self):
        accoes = [Mover(ang, ang_abs=True) for ang in dirmov()] # accoes mover com angulo absoluto
        self._mec_motiv = MecMotiv()
        self._mec_aprend = MecAprend(accoes)
        self.s = None   # Estado anterior
        self.a = None   # Accao anterior

 
    def processar(self, percepcao):
        sn = percepcao.posicao                              # Observar novo estado
        if self.s is not None:                              # Se estado válido
            a = self.a                                      # Recordar accao
            r = self._mec_motiv.gerar_reforco(percepcao)    # Gerar reforco
            self._mec_aprend.aprender(self.s, a, r, sn)     # Aprender
        an = self._mec_aprend.seleccionar_accao(sn)          # Selecionar proxima accao
        self.s = sn                                         # Atualizar estado
        self.a = an                                         # Atualizar accao
        return an
