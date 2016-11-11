# -*- coding: latin-1 -*-
'''
Mecanismo motivacional
'''

#_______________________________________________________________________________

class MecMotiv:
    def __init__(self): 
        self.rmax = 100             # Refor�o m�ximo   
        
    def gerar_reforco(self, percepcao): 
        r = -percepcao.custo_mov    # Custo de movimenta��o
        if percepcao.carga:
            r += self.rmax          # Carga obtida
        elif percepcao.colisao:
            r += -self.rmax         # Colis�o  
        return r
