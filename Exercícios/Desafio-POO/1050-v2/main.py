from operadora import Operadora
from estado import Estado
from estado_repository import EstadoRepository
from facade import Facade
from estado_application import EstadoApplication
from user_interface_console import UserInterfaceConsole

estado_repository = EstadoRepository()

estado1 = Estado(61, "Brasilia")
estado2 = Estado(71, "Salvador")
estado3 = Estado(11, "Sao Paulo")
estado4 = Estado(21, "Rio de Janeiro")
estado5 = Estado(32, "Juiz de Fora")
estado6 = Estado(19, "Campinas")
estado7 = Estado(27, "Vitória")
estado8 = Estado(31, "Belo Horizonte")
estado9 = Estado(81, "Pernambuco")

estado_repository.adiciona_estado(estado1)
estado_repository.adiciona_estado(estado2)
estado_repository.adiciona_estado(estado3)
estado_repository.adiciona_estado(estado4)
estado_repository.adiciona_estado(estado5)
estado_repository.adiciona_estado(estado6)
estado_repository.adiciona_estado(estado7)
estado_repository.adiciona_estado(estado8)
estado_repository.adiciona_estado(estado9)

operadora = Operadora(estado_repository)

estado_application = EstadoApplication(estado_repository)
facade = Facade(estado_application)
user_interface_console = UserInterfaceConsole(facade)


while (True):
    print(estado_repository)
        
    resultado = user_interface_console.obter_codigo_usuario()
       
    if (resultado == "Estado não encontrado..."):
           break


