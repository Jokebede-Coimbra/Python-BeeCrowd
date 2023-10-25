from produto import Produto


class ProdutoRepository:
    def __init__(self) -> None:
        self.produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def get_produto(self, opcao: int) -> Produto:
        for produto in self.produtos:
            if produto.codigo == opcao:
                return produto

    def __str__(self) -> str:
        menu: str = "Codigo Descricao Preco\n"

        for produto in self.produtos:
            menu += f'{produto.codigo} - {produto.descricao}, {produto.preco:.2f}\n'

        return menu