import sys

sys.path.append("../../lib")

from rac_aut.modelo_mundo import ModeloMundo
from psa.util import dirmov
from psa.accao import Avancar
from psa.util import mover

class ModeloProsp(ModeloMundo):
    def __init__(self):
        self._imagem = {}
        self._estado = None
        self._estados = []
        self._accoes = [Avancar(ang) for ang in dirmov()]
        self._alteracao = True

    @property
    def estado(self):
        return self._estado

    @property
    def alteracao(self):
        return self._alteracao

    def assimilar(self, percepcao):
        self._estado = percepcao.posicao
        self._alteracao = self._imagem != percepcao.imagem  # python compara por nos os dicionarios
        # se houver alteracao temos de atualizar a imagem
        if self._alteracao:
            self._imagem = percepcao.imagem

            # Obter todas as posicoes validas, isto e, que nao tem obstaculo
            self._estados = [s for s, elem in self._imagem.items() if elem != 'obst']  # items devolve par chave,valor

    # obter estado
    def obter_elem(self, s):
        return self._imagem.get(s)  # Igual ao acesso por [] mas devolve valor por omissao

    # quais os estados disponveis
    def S(self):
        return self._estados

    # quais as accoes disponiveis
    def A(self, s=None):
       return self._accoes

    # como se simula uma transicao
    def T(self, s, a):
        sn = mover(s, a.ang) # metodo mover faz uma translacao, calculo apenas
        if sn in self.S():
            return sn # por omissao uma funcao em python retorna None