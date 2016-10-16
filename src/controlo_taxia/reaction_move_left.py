from psa.actuador import ESQ, DIR
from reaction import Reaction

class ReactionMoveLeft(Reaction):
    def activate(self, perception):
        if perception[ESQ].pot_alvo > perception[DIR].pot_alvo:
            return (1, ESQ)
        else:
            return (0, ESQ)