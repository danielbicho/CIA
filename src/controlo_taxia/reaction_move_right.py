import reaction

from psa.actuador import ESQ, DIR, FRT
from reaction import Reaction

class ReactionMoveRight(Reaction):
    def activate(self, perception):
        if perception[DIR].pot_alvo > perception[ESQ].pot_alvo:
            return (1, DIR)
        else:
            return (0, DIR)