
import unittest
from unittest.mock import patch
from io import StringIO

from main import orquestrador
from cardapio import Cardapio
from produto import Produto
from produto_repository import ProdutoRepository

class TestOrquestrador(unittest.TestCase):

    def configuracao(self):
        self.produto_repository = ProdutoRepository()
        self.cardapio = Cardapio(self.produto_repository)
        
    @patch("builtins.input", side_effect=["1", "2", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_orquestrador_entrada_valida(self, mock_stdout, mock_input):
        orquestrador()
        resultado = mock_stdout.getvalue()
        self.assertIn("Total a pagar:", resultado)
        self.assertIn("8.00", resultado)

    @patch("builtins.input", side_effect=["1", "1","s","2","2","n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_orquestrador_multiplos_itens(self, mock_stdout, mock_input):
        orquestrador()
        resultado = mock_stdout.getvalue()
        self.assertIn("Total a pagar: R$ 13.00", resultado)  

 
    @patch("builtins.input", side_effect=["1", "abc", "3", "s"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_orquestrador_quantidade_invalida(self, mock_stdout, mock_input):
        orquestrador()
        resultado = mock_stdout.getvalue()
        self.assertIn("Entrada inválida.", resultado)
        
        
    @patch("builtins.input", side_effect=["6", "2", "2","n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_orquestrador_produto_invalido(self, mock_stdout, mock_input):
        orquestrador()
        resultado = mock_stdout.getvalue()
        self.assertIn("Código de produto inválido.", resultado)

