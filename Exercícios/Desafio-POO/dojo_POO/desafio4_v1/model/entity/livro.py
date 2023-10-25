import random

class Livro:
    
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__identificacao = random.randint(0, 100000)

        
    def informacoes_livro(self) -> None:
        print(f'Título: {self.__titulo}, Autor: {self.__autor}, Ano: {self.__ano}, Identificação: {self.__identificacao}')            