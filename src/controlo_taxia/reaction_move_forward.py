import reaction

from psa.actuador import ESQ, DIR, FRT
from reaction import Reaction

class ReactionMoveForward(Reaction):
    def activate(self, perception):
        if perception[FRT].pot_alvo > perception[DIR].pot_alvo and perception[FRT].pot_alvo > perception[ESQ].pot_alvo:
            return (1, FRT)
        else:
            return (0, FRT)