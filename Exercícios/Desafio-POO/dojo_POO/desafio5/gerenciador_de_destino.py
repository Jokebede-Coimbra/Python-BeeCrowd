from typing import Type
from destinos.interfaces.destinos import DestinoInterface

class GrenciadorDeDestino:
    
    def viajar(self, destino: Type[DestinoInterface]):
        return destino.atividade()