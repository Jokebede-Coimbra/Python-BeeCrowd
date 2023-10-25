from estado_repository import EstadoRepository
from estado import Estado

class EstadoApplication:
    def __init__(self, estado_repository:EstadoRepository) -> None:
        self.estado_repository = estado_repository
        
    def get_estado(self, code: int) -> Estado: 
        return self.estado_repository.buscar_estado(code)
         