# -*- coding: latin-1 -*-
"""
Agente Reactivo: Class ControloTaxia
@author:Paulo Nunes
"""
import sys

from agente_prosp.controlo import Controlo
from reaction_move_forward import ReactionMoveForward
from reaction_move_left import ReactionMoveLeft
from reaction_move_right import ReactionMoveRight
from avoid_obstacle import AvoidObstacle
from psa.actuador import ESQ, FRT, DIR #para obter as constantes de direc��o

class ControloTaxia(Controlo):
    """
    M�todo Processar
    Retorna uma accao de acordo com a percep��o
    Ac��o � resposta directa ao campo de potencial
    """
    def __init__(self):
        self.rl = ReactionMoveLeft()
        self.rd = ReactionMoveRight()
        self.rf = ReactionMoveForward()
        self.ac = AvoidObstacle()

    def processar(self, percepcao):
        #Verificar qual a direc��o de m�ximo potencial
        #list_pot = [percepcao.per_dir[FRT].pot_alvo,percepcao.per_dir[ESQ].pot_alvo,percepcao.per_dir[DIR].pot_alvo]
        #Avan�ar nessa direc��o
        #action = ReactionMoveForward().activate(percepcao)
        reaction1 = self.rf.activate(percepcao)
        reaction2 = self.rd.activate(percepcao)
        reaction3 = self.rl.activate(percepcao)
        reaction4 = self.ac.activate(percepcao)

        if reaction4[0] > 0:
            return reaction4
        elif reaction1[0] > 0:
            return reaction1
        elif reaction2[0] > 0:
            return reaction2
        else:
            return reaction3
