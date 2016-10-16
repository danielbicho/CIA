# -*- coding: latin-1 -*-
"""
Primeiro teste de python com a PSA
@author:Paulo Nunes
"""

import psa
from psa.agente import Agente
class AgenteTeste(Agente):
    def executar(self):
        self.actuador.actuar((1,0))#actuar((Velocidade, direção em radianos))

# Iniciar plataforma psa
psa.iniciar("amb/amb1.das")

#Criação do objecto agente
agente = AgenteTeste()

#Executar plataforma
psa.executar(agente)
