from .entity import Livro

from typing import Type

class RepositorioDeLivros:
    
    def __init__(self) -> None:
        self.__livros = []
    
    def adicionar_livro(self, livro: Type[Livro]) -> None:
        self.__livros.append(livro)
      
    def listar_livro(self) -> None:
        for livro in self.__livros:
            livro.informacoes_livro()   
            