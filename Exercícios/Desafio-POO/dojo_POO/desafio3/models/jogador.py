import random

class Jogador:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__vitorias = 0
        self.__jogadas = ['pedra', 'papel', 'tesoura']
        
    def fazer_jogada(self):
        return random.choice(self.__jogadas)
    
    def incrementar_vitorias(self):
        self.__vitorias += 1
        
    def apresentar_vitorias(self):
        return (f'{self.__nome}: {self.__vitorias} vitórias')
        