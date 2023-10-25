from facade import Facade


class UserInterfaceConsole:
    def __init__(self, facade: Facade) -> None:
        self.facade = facade
        
    def obter_codigo_usuario(self) -> None:
        codigo = int(input("Digite o DDD do estado: "))
        
        resultado = self.facade.coder(codigo)
        print(f"Código DDD inserido: {codigo}")
        print(f"Resultado obtido: {resultado}")
        return resultado
        
        