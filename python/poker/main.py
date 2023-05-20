import Carta, Poker, Deck, Jogador

if __name__ == '__main__':
    deck = Deck()
    deck.cria_baralho()
    #deck.printa_baralho()
    deck.embaralha_batalho()


    #deck.printa_baralho()
    player1 = Jogador()
    player1.criar_cartas(deck)
    player1.printa_cartas()

    for i in range(3):
        resposta = input('Digite as cartas que quer trocar(digite enter para nao trocar): ')
        if resposta == '':
            break

        trocas = [int(x) for x in resposta.split()]
        player1.trocar_cartas(trocas)
        player1.printa_cartas()
