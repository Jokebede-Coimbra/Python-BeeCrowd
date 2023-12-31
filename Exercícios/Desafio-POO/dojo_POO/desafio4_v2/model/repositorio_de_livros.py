from .entity import Livro

class RepositorioDeLivros:
    
    def __init__(self) -> None:
        self.__livros = []
    
    def registrar_livro(self, titulo, autor, ano):
      livro = Livro(titulo, autor, ano)  
      self.__livros.append(livro)
      print('Livro cadastrado!')
      print()
    
    def listar_livros(self):
        for livro in self.__livros:
            print(f'id: {livro.id}, Livro: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}')
            print() 
            