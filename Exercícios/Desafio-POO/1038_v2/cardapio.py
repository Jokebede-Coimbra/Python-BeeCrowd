from produto import Produto
from produto_repository import ProdutoRepository


class Cardapio:
    def __init__(self, produto_repository: ProdutoRepository) -> None:
        self.produto_repository = produto_repository
        
    def get_valor_produto(self, opcao) -> float:
        produto = self.produto_repository.get_produto(opcao)
        if produto == None:
            return 0
        
        return produto.preco