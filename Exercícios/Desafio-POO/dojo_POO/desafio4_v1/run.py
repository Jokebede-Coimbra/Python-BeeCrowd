from model.entity import Livro
from model import RepositorioDeLivros

repositorioDeLivros = RepositorioDeLivros()
livro1 = Livro('Anne de Green Gables','L.M',1928)
livro2 = Livro('Anne de Avonlea','L.M',1918)

repositorioDeLivros.adicionar_livro(livro1)
repositorioDeLivros.adicionar_livro(livro2)
repositorioDeLivros.listar_livro()