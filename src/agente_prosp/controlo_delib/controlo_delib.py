import sys

sys.path.append("../../lib")

from agente_prosp.controlo import Controlo


class ControloDelib(Controlo):
    def __init__(self, percepcao, modelo, planeador):
        self.percepcao = percepcao
        self._modelo = modelo
        self._planeador = planeador

    def processar(self, percepcao):
        self.assimilar(self.percepcao)
        self.deliberar()
        self.planear()
        return self.executar()

    def assimilar(self, percepcao):
        self._modelo.assimilar()

    def deliberar(self):
        self._objectivos = [s for s in self._modelo.S() if self._modelo.obter_elem(s) == 'alvo']

    def planear(self):
        self._planeador.planear(self._objectivos, self._modelo)

    def executar(self):
        return self._planeador.obter_accao()
