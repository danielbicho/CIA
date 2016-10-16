# -*- coding: latin-1 -*-
"""
Agente Reactivo: Class AgenteProspector
@author:Paulo Nunes
"""

from psa.agente import Agente

"""
Classe AgenteProspector
Necessita de um objecto Controlo j� instanciado pelo chamador (Dependecy Injection / IoC)
"""
class AgenteProspector(Agente):
    
    def __init__(self,controlo):
        #Agente.__init__(self) -- antes da vers�o 2.7
        super(AgenteProspector, self).__init__()
        self.controlo = controlo
            
    def executar(self):
        self.percepcao=self.sensor_multiplo.detectar()
        self.accao = self.controlo.processar(self.percepcao)
        self.actuador.actuar(self.accao)

