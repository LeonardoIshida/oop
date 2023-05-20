import random

class Poker:
    def contar_pontuacao(self, player):
        valores = []
        naipes = []
        qtd = [0 for _ in range(14)]

        for carta in player.cartas:
            valores.append(player.cartas.valor)
            naipes.append(player.cartas.naipe)
            qtd[player.cartas.valor-2] += 1

        valores.sort()
        
    
    def isRoyalStraightFlush(self, valores, naipes):
        if self.isStraightFlush(valores, naipes) == False:
            return False
        
        # ao ordenar os valores consigo verificar se a listas sao iguais
        return valores == [10, 11, 12, 13, 14]
        
    
    def isStraightFlush(self, valores, naipes):
        # verificando se tenho apenas 1 naipe
        if self.isStraight(valores) == False:
           return False
       
        if self.isFlush(naipes) == False:
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

    def isFullHand(self, valores):
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
        return len(set(naipes)) == 1
        
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
        




