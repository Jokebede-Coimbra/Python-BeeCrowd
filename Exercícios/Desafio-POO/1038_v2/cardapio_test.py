
import unittest
from cardapio import Cardapio
from produto import Produto
from produto_repository import ProdutoRepository

class TestCardapio(unittest.TestCase):

    def configuracao(self):
        self.produto_repository = ProdutoRepository()
        self.cardapio = Cardapio(self.produto_repository)

    def test_get_valor_produto(self):
        produto1 = Produto(1, 'Hot Dog', 4)
        self.produto_repository.adicionar_produto(produto1)
        self.assertEqual(self.cardapio.get_valor_produto(1), 4.0)

    def test_get_valor_produto_invalido(self):
        self.assertEqual(self.cardapio.get_valor_produto(100), 0.0)



    