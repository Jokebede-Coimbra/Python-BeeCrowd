from estado_application import EstadoApplication


class Facade:
    def __init__(self, estado_application:EstadoApplication) -> None:
        self.estado_application = estado_application
        
    
    def coder(self, code: int) -> str:
        estado = self.estado_application.get_estado(code) 
        
        if (estado is None):
            return "Estado não encontrado..."
        return f"{estado.codigo} | {estado.destino}"
       # return self.estado_application.get_estado(estado)