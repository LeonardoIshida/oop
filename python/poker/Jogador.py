import random
from Deck import Deck
from Carta import Carta

class Jogador:

    def __init__(self):
        self.saldo = 200.0
        self.cartas = []

    def subtrai_saldo(self, dinheiro):
        self.saldo -= dinheiro
        
    def adiciona_saldo(self, dinheiro):
        self.saldo += dinheiro

    def criar_cartas(self, baralho):
        #escolhendo aleatoriamente cinco cartas para iniciar a rodada
        for i in range(5):
            #esolhendo um indice aleatorio
            indice = random.randint(0, baralho.len - 1)
            
            #inserindo a carta na "mao" do jogador
            self.cartas.append(baralho.get_carta_baralho(indice))
            
            #removendo a carta do baralho
            baralho.retira_baralho(indice)

    def printa_cartas(self):
        #cartas na mao vai ser uma matriz, em que cada indice vai ser guardado
        #uma lista com a carta "fragmentada"
        cartas_na_mao = []
        for i in range(5):
            carta = self.cartas[i].to_string().split('\n')
            cartas_na_mao.append(carta)

        carta_to_print = "   1\t   2\t   3\t   4\t   5\n"
        for i in range(5):
            carta_to_print += cartas_na_mao[0][i] + '\t'
            carta_to_print += cartas_na_mao[1][i] + '\t'
            carta_to_print += cartas_na_mao[2][i] + '\t'
            carta_to_print += cartas_na_mao[3][i] + '\t'
            carta_to_print += cartas_na_mao[4][i] + '\n'

        print(carta_to_print)

    def trocar_cartas(self, lista_trocas, deck):
        for pos in lista_trocas:
            # inserindo carta que vai ser trocada no baralho
            deck.insere_carta_baralho(self.cartas[pos-1])
            
            # escolhendo uma carta aleatoria
            indice_carta = random.randint(0, deck.len)
            
            # rettirando do baralho e inserindo na mao do jogador
            self.cartas[pos-1] = deck.get_carta_baralho(indice_carta)
            deck.retira_baralho(indice_carta)
            
    # funcao para devolver as cartas do jogador para o baralho
    def devolver_cartas(self, deck):
        for i in range(5):
            deck.insere_carta_baralho(self.cartas[i])
            
        self.cartas = []
        
    # funcao para testar os casos de ganho
    def manipular_cartas(self):
        self.cartas[0] = Carta(1, 'paus')
        self.cartas[1] = Carta(2, 'paus')
        self.cartas[2] = Carta(4, 'paus')
        self.cartas[3] = Carta(4, 'paus')
        self.cartas[4] = Carta(2, 'ouros')
        
