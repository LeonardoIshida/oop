import random

class Carta:
    
    def __init__(self, valor, naipe):
        self.naipe = naipe
        self.valor = valor
        
    
    def sorteio_valor(self):
        self.valor = random.randint(2, 14)

    def sorteio_naipe(self):
        naipes = ['ouros', 'copas', 'paus', 'espadas']
        self.naipe = random.choice(naipes)

        
    def to_string(self):
        carta_top = '+-----+\n'
        carta_mid = '|     |\n'

        match self.naipe:
            case 'ouros':
                naipe = "\u2666"
            case 'paus':
                naipe = "\u2663"
            case 'copas':
                naipe = "\u2665"
            case 'espadas':
                naipe = "\u2660"

        valor = self.valor
        #verificando o tamanho do numero para nao quebrar formatacao das cartas
        if valor == 10:
            carta_valor = f'| {valor} {naipe}|\n'

        #valores que nao quebram formatacao, mas tenho que alterar os valores das cartas
        else:
            match self.valor:
                case 11:
                    valor = 'J'
                case 12:
                    valor = 'Q'
                case 13:
                    valor = 'K'
                case 14:
                    valor = 'A'

            carta_valor = f'| {valor}  {naipe}|\n'

        #juntando todas as strings
        carta_completa = carta_top + carta_mid + carta_valor + carta_mid + carta_top

        return carta_completa

class Deck:

    def __init__(self):
        self.baralho = []
        self.len = 0

    def cria_baralho(self):
        naipes = ['ouros', 'copas', 'paus', 'espadas']
        baralho = []

        for i in range(2, 15):
            for naipe in naipes:
                carta = Carta(i, naipe)
                baralho.append(carta)

        self.baralho = baralho
        self.len = len(baralho)
    
    def embaralha_batalho(self):
        for i in range(len(self.baralho)-1,0,-1):
            r = random.randint(0 , i)
            self.baralho[i]  , self.baralho[r] = self.baralho[r] , self.baralho[i]

    def printa_baralho(self):
        for i in range(len(self.baralho)):
            print(self.baralho[i].to_string())

    def retira_baralho(self, indice):
        del self.baralho[indice]
        self.len -= 1
    
    def get_carta_baralho(self, indice) -> Carta:
        return self.baralho[indice]

class Jogador:

    def __init__(self):
        self.saldo = 200
        self.cartas = []

    def subtrai_saldo(self, dinheiro):
        self.saldo -= dinheiro

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

    def trocar_cartas(self, lista_trocas):
        for pos in lista_trocas:
            self.cartas[pos-1].sorteio_naipe()
            self.cartas[pos-1].sorteio_valor()

class Poker:
    def contar_pontuacao(self, player):
        valores = []
        naipes = []

        for carta in player.cartas:
            valores.append(player.cartas.valor)
            naipes.append(player.cartas.naipe)

        valores.sort()
        
    
    def isRoyalStraightFlush(self, valores, naipes):
        # ao ordenar os valores consigo verificar se a listas sao iguais
        if valores != [10, 11, 12, 13, 14]:
            return False

        #varificando a quantidade de naipes, se for maior que 1, n eh royal straight flush
        if len(set(naipes)) != 1:
            return False

        return True
    
    def isStraightFlush(self, valores, naipes):
        # verificando se tenho apenas 1 naipe
        if len(set(naipes) > 1):
            return False
        
        #verificando se a carta na posicao i eh igual a proxima carta + 1
        for i in range(len(valores)-1):
            if valores[i]+1 != valores[i+1]:
                return False
            
        return True
        
    def isQuadra(self, valores):
        # verificando se tenho apenas cartas com dois valores diferentes
        if len(set(valores) != 2):
            return False
        
        # contando quantas vezes a carta do meio aparece, como esta ordenado, para ser uma quadra,
        # ela devera aparecer extamente 4 vezes
        carta_do_meio = valores[len(valores) // 2]
        contador = 0
        for i in range(len(valores)):
            if valores[i] == carta_do_meio:
                contador += 1
            
        if contador != 4:
            return False
        
        return True

    def fullHand(self, valores):
        # se tenho mais que dois tipos de valores, quer dizer que nao 
        # tenho uma trinca e um par
        if len(set(valores)) != 2:
            return False
        
        # como ja verifiquei que nao eh uma quadra anteriormente,
        # eh garantido que se tenho apenas cartas com dois valores
        # diferentes, que tenho um full hand
        return True
        
        
    def isFlush(self, naipes):
        # verificando se tenho apenas um naipe
        if len(set(naipes) == 1):
            return True
        else:
            return False
        
    def isStraight(self, valores):
        #verificando se a carta na posicao i eh igual a proxima carta + 1
        for i in range(len(valores)-1):
            if valores[i]+1 != valores[i+1]:
                return False
            
        return True
    
    def isTrinca(self, valores):
        # verificando se tenho apenas cartas com 2 valores diferentes
        if len(set(valores)) > 3:
            return False
        

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



