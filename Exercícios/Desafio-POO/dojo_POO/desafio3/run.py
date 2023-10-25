from models import Jogador
from controller  import GerenciadorDeJogo

jogador1 = Jogador('Jayanne') 
jogador2 = Jogador('Josué') 

gerenciadorDeJogo = GerenciadorDeJogo(jogador1, jogador2)

while True:
    input()
    resultado = gerenciadorDeJogo.apostarRodada()
    print(resultado)
    print()