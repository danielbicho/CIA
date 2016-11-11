# -*- coding: latin-1 -*-
'''
Mecanismo de selec��o de ac��o do tipo e-greedy
'''

from random import random, choice, shuffle

from sel_accao import SelAccao

#_______________________________________________________________________________

class SelAccaoEGreedy(SelAccao):
    def __init__(self, mem_aprend, accoes, epsilon):
        self._mem_aprend = mem_aprend
        self._accoes = accoes
        self._epsilon = epsilon

    def max_accao(self, s):
        shuffle(self._accoes) # Escolha aleat�ria entre ac��es com igual valor
        return max(self._accoes, key=lambda a: self._mem_aprend.obter(s,a))
        
    def explorar(self, _):
        return choice(self._accoes)      # Explora��o aleat�ria

    def seleccionar_accao(self, s):
        if random() > self._epsilon:
            accao = self.max_accao(s)    # Aproveitar conhecimento
        else:
            accao = self.explorar(s)     # Explorar
        return accao
