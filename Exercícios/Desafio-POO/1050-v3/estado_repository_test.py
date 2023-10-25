from estado import Estado
from estado_repository import EstadoRepository

def test_deveria_adicionar_estado():
    # arrange
    estado1: Estado = Estado(81, "Pernambuco")
    estado_repository : EstadoRepository = EstadoRepository()
    
    # act
    estado_repository.adiciona_estado(estado1)
    
    # assert
    assert len(estado_repository.estados) == 1
    

def test_deveria_buscar_estado():
    # arrange 
    estado1: Estado = Estado(81, "Pernambuco")
    estado_repository : EstadoRepository = EstadoRepository()
    estado_repository. adiciona_estado(estado1)
    
    # act
    estado = estado_repository.buscar_estado(81)
    
    # assert
    assert estado != None
    assert estado.destino == "Pernambuco"    
