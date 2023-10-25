from cardapio import Cardapio
from produto import Produto
from produto_repository import ProdutoRepository

produto_repository = ProdutoRepository()
produto1 = Produto(1, 'Hot Dog', 4)
produto2 = Produto(2, 'X-Salada', 4.50)
produto3 = Produto(3, 'X-Bacon', 5)
produto4 = Produto(4, 'Simple Toast', 2)
produto5 = Produto(5, 'Refrigerante', 1.50)

produto_repository.adicionar_produto(produto1)
produto_repository.adicionar_produto(produto2)
produto_repository.adicionar_produto(produto3)
produto_repository.adicionar_produto(produto4)
produto_repository.adicionar_produto(produto5)

cardapio = Cardapio(produto_repository)

def orquestrador() -> None:
    total_pedido: float = 0
    continuar: str = 's'

    while continuar.lower() == 's':
        try:
            opcao = int(input('Digite o código do produto desejado: '))
            valor_produto = cardapio.get_valor_produto(opcao)

            if valor_produto == 0:
                print("Código de produto inválido.")
                continue

            quantidade = int(input('Digite a quantidade: '))

            total_pedido += valor_produto * quantidade

        except ValueError:
            print("Entrada inválida.")

        continuar = input('Deseja adicionar outro produto? ("S" para "sim"): ')

    print(f"Total a pagar: R$ {total_pedido:.2f}")

orquestrador()
