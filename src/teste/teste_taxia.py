# coding=utf-8
import sys

import psa

# Iniciar plataforma psa
psa.iniciar("amb/amb4.das")

sys.path.append("..")

from controlo_taxia.controlo_taxia import ControloTaxia

#Criação do objecto controlo
controlo_taxia = ControloTaxia()

from agente_prosp.agente_prospector import AgenteProspector

#Criação do objecto agente
agente = AgenteProspector(controlo_taxia)

#Executar plataforma
psa.executar(agente)
