from produto import Produto
from produto_repository import ProdutoRepository


def test_deveria_adicionar_produto():
    # arrange
    produto1: Produto = Produto(1, "Coxinha", 8.50)
    produto_repository : ProdutoRepository = ProdutoRepository()
    
    # act
    produto_repository. adicionar_produto(produto1)
    
    # assert
    assert len(produto_repository.produtos) == 1
 
    
def test_deveria_get_produto():
    # arrange 
    produto1: Produto = Produto(1, "Coxinha", 8.50)
    produto_repository : ProdutoRepository = ProdutoRepository()
    produto_repository. adicionar_produto(produto1)
    
    # act
    produto = produto_repository.get_produto(1)
    
    # assert
    assert produto != None
    assert produto.descricao == "Coxinha"
 
