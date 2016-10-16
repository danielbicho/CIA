from reaction import Reaction
from psa.actuador import ESQ

class AvoidObstacle(Reaction):
    def activate(self, perception):
        if perception.colisao:
            return (1, ESQ)
        else:
            return (0, ESQ)