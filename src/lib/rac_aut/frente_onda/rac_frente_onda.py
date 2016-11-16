from math import pow

from psa.util import dist

# racicionio frente de onda
class RacFrenteOnda(object):
    def adjacentes(self, s, modelo):
        adj = []
        for a in modelo.A(s):
            sn = modelo.T(s, a)

            # condicoes que e considerado adjacente
            if sn is not None and sn != s:
                adj.append(sn)
        return adj

    def gerar_valor(self, objectivos, modelo, gama, valor_max):
        V = {}
        frente_onda = []
        for s in objectivos:
            V[s] = valor_max
            frente_onda.append(s)
        while frente_onda:
            s = frente_onda.pop(0)
            for sn in self.adjacentes(s, modelo):
                # v = V[s] * gama**dist(s, sn)
                v = V[s] * pow(gama, dist(s, sn))
                if v > V.get(sn, float("-inf")):
                    V[sn] = v
                    frente_onda.append(sn)
        return V

    def gerar_politica(self, modelo, V):
        P = {}
        for s in modelo.S():
            P[s] = max(modelo.A(s), key= lambda a: V.get(modelo.T(s, a), 0))
        return P
