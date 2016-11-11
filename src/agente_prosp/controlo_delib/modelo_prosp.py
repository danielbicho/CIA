import sys

sys.path.append("../../lib")

from lib.rac_aut.modelo_mundo import ModeloMundo

class ModeloProsp(ModeloMundo):
    def __init__(self, percepcao):
        self.percepcao = percepcao

    def assimilar(self, percepcao):
        pass
