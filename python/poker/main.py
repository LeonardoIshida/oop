#   Jogo de Video Poker
#
#   Leonardo Ishida - 12873424
#   Rafael Conrado - 

from Jogador import Jogador
from Poker import Poker
from Deck import Deck

if __name__ == '__main__':
    
    poker = Poker()
    deck = Deck()
    player1 = Jogador()
    
    poker.jogar(player1, deck)
    print(f'Voce terminou o jogo com {player1.saldo}')