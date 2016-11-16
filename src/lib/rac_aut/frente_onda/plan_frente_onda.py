from rac_frente_onda import RacFrenteOnda

class PlanFrenteOnda(object):
    def __init__(self):
        self._mec_rac = RacFrenteOnda()
        self._V = {}
        self._P = {}
        self._gama = 0.95
        self._valor_max = 1

    def planear(self, objectivos, modelo):
        if objectivos:
            self._V = self._mec_rac.gerar_valor(objectivos, modelo, self._gama, self._valor_max)
            self._P = self._mec_rac.gerar_politica(modelo, self._V)
        else:
            self._V = {}
            self._P = {}

    def obter_accao(self, s):
        return self._P.get(s)