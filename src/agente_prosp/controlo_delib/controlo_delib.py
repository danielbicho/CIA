import sys

sys.path.append("../../lib")

from agente_prosp.controlo import Controlo
from agente_prosp.controlo_delib.modelo_prosp import ModeloProsp

class ControloDelib(Controlo):
    def __init__(self, planeador):
        self._modelo = ModeloProsp()
        self._planeador = planeador

    def processar(self, percepcao):
        self.assimilar(percepcao)
        self.deliberar()
        self.planear()
        return self.executar()

    def assimilar(self, percepcao):
        self._modelo.assimilar(percepcao)

    def deliberar(self):
        self._objectivos = [s for s in self._modelo.S() if self._modelo.obter_elem(s) == 'alvo']

    def planear(self):
        self._planeador.planear(self._objectivos, self._modelo)

    def executar(self):
        return self._planeador.obter_accao(self._modelo.estado)