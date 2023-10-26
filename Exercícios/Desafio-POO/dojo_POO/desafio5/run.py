from gerenciador_de_destino import GrenciadorDeDestino 
from destinos.belo_horizonte import BeloHorizonte 
from destinos.fortaleza import Fotaleza 
from destinos.niteroi import Niteroi 

gerenciadorDeDestino = GrenciadorDeDestino()

while True:
    destino = None
    
    destino_da_viagem = input('Selecione o destino da viagem: ')
    if (destino_da_viagem == '1') : destino = Niteroi()
    elif (destino_da_viagem == '2') : destino = BeloHorizonte()
    elif (destino_da_viagem == '3') : destino = Fotaleza()
    else: destino = BeloHorizonte()
    
    atividade = gerenciadorDeDestino.viajar(destino)
    print(atividade)
    
    print()