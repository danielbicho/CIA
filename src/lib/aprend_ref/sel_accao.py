# -*- coding: latin-1 -*-
'''
Mecanismo de selecção de acção
'''

#_______________________________________________________________________________

class SelAccao(object):
    """Interface de selecção de acção"""
    def seleccionar_accao(self, s):
        raise NotImplementedError
