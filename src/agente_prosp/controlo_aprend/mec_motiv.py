# -*- coding: latin-1 -*-
'''
Mecanismo motivacional
'''

#_______________________________________________________________________________

class MecMotiv:
    def __init__(self): 
        self.rmax = 100             # Reforço máximo   
        
    def gerar_reforco(self, percepcao): 
        r = -percepcao.custo_mov    # Custo de movimentação
        if percepcao.carga:
            r += self.rmax          # Carga obtida
        elif percepcao.colisao:
            r += -self.rmax         # Colisão  
        return r
