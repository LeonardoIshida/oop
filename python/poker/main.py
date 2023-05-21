from Jogador import Jogador
from Poker import Poker
from Deck import Deck

if __name__ == '__main__':
    poker = Poker()
    deck = Deck()
    player1 = Jogador()
    
    poker.jogar(player1, deck)