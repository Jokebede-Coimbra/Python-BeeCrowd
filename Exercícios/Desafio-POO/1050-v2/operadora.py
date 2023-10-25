from estado import Estado
from estado_repository import EstadoRepository

class Operadora:
    def  __init__(self, estado_repository:EstadoRepository) -> None:
      self.estado_repository = estado_repository
     
    def get_codigo_estado(self, opcao) -> Estado:
        return self.estado_repository.buscar_estado(opcao)
       