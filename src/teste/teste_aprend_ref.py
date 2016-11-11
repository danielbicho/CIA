# coding=utf-8
import sys
sys.path.append("../agente_prosp")
sys.path.append("../lib")

import psa

# Definição do agente prospector
from agente_prosp.agente_prospector import AgenteProspector

# Definicao controlo com aprendizagem por reforço
from controlo_aprend.controlo_aprend_ref import ControloAprendRef

#
# Activacao
#_______________________________________________________________________________________________

# Iniciar plataforma psa
psa.iniciar("amb/amb3b.das", alvo_ini=True)

# Executar Agente
psa.executar(AgenteProspector(ControloAprendRef()))
