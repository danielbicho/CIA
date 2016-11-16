# coding=utf-8
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")

import psa

# Definição do agente prospector
from agente_prosp.agente_prospector import AgenteProspector

# Definicao controlo com aprendizagem por reforço
from agente_prosp.controlo_delib.controlo_delib import ControloDelib


from rac_aut.frente_onda.plan_frente_onda import PlanFrenteOnda
# Activacao
# _______________________________________________________________________________________________

# Iniciar plataforma psa
psa.iniciar("amb/amb3.das", alvo_ini = True)

# Iniciar Controlo
planeador = PlanFrenteOnda()
controlo = ControloDelib(planeador)

# Executar Agente
psa.executar(AgenteProspector(controlo))
