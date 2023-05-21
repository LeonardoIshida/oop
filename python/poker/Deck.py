import random
from Carta import Carta

class Deck:

    def __init__(self):
        naipes = ['ouros', 'copas', 'paus', 'espadas']
        baralho = []

        for i in range(2, 15):
            for naipe in naipes:
                carta = Carta(i, naipe)
                baralho.append(carta)

        self.baralho = baralho
        self.len = len(baralho)
    
    def embaralha_baralho(self):
        for i in range(len(self.baralho)-1,0,-1):
            r = random.randint(0 , i)
            self.baralho[i]  , self.baralho[r] = self.baralho[r] , self.baralho[i]

    # funcao para debug
    def printa_baralho(self):
        for i in range(len(self.baralho)):
            print(self.baralho[i].to_string())

    # remove do baralho a carta que esta no indice
    def retira_baralho(self, indice):
        del self.baralho[indice]
        self.len -= 1
    
    # retirna a carta que esta no indice
    def get_carta_baralho(self, indice) -> Carta:
        return self.baralho[indice]
    
    def insere_carta_baralho(self, carta):
        self.baralho.append(carta)