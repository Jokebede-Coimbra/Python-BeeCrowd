from estado import Estado

class EstadoRepository:
    def __init__(self) -> None:
        self.estados: list[Estado] = []

    def adiciona_estado(self, estado: Estado):
        self.estados.append(estado)

    def buscar_estado(self, opcao: int) -> Estado:
        for estado in self.estados:
            if estado.codigo == opcao:
                return estado
        return None 
    
    def __str__(self) -> str:
        display: str = "DDD | Destino\n"  
        for estado in self.estados:
            display += f"{estado.codigo} | {estado.destino}\n"   
        return display              
