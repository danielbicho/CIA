# -*- coding: latin-1 -*-
'''
Mecanismo de selec��o de ac��o
'''

#_______________________________________________________________________________

class SelAccao(object):
    """Interface de selec��o de ac��o"""
    def seleccionar_accao(self, s):
        raise NotImplementedError
