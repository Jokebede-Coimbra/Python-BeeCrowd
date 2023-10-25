from operadora import Operadora
from estado import Estado
from estado_repository import EstadoRepository


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


def orquestrador() -> None:
    continuar = 's'
    while continuar.lower() == 's':
        try:
            opcao = int(input("Digite o DDD do estado: "))
            estado = operadora.get_codigo_estado(opcao)
            
            if estado is None:
                print("DDD inválido.")
                continue
            
            else:
                print(f"DDD: ({estado.codigo}) >> Estado: {estado.destino}")

        except ValueError:
            print("Opção inválida")

        continuar = input('Deseja verificar outro estado? ("S" ou "N" ): ')
        if continuar.lower() != 's':
           break

orquestrador()
