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