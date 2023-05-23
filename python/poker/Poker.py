import random
from Deck import Deck
from Jogador import Jogador

class Poker:
    
    def contar_pontuacao(self, player, valor_aposta):
        valores = []
        naipes = []
        qtd = [0 for _ in range(14)]

        # criando listas para auxiliar na verificacao dos ganhos
        for carta in player.cartas:
            valores.append(carta.valor)
            naipes.append(carta.naipe)
            qtd[carta.valor-2] += 1

        # ordenando os valores para ajudar na comparacao
        valores.sort()
        
        if self.isRoyalStraightFlush(valores, naipes):
            return valor_aposta * 200
        
        if self.isStraightFlush(valores, naipes):
            return valor_aposta * 100
        
        if self.isQuadra(valores):
            return valor_aposta * 50
        
        if self.isFullHand(valores):
            return valor_aposta * 20
        
        if self.isFlush(naipes):
            return valor_aposta * 10
        
        if self.isStraight(valores):
            return valor_aposta * 5
        
        if self.isTrinca(qtd):
            return valor_aposta * 2
        
        if self.isDupla(qtd):
            return valor_aposta
        
        return 0
    
    def jogar(self, jogador, deck):
        
        while jogador.saldo > 0:
            print(f'Saldo atual: {jogador.saldo}')
            
            # laco para aceitar um valor valido do usuario ou F para sair
            while True:
                resposta = (input('Digite o valor que quer apostar ou para "F" sair: '))
                if resposta == 'F':
                    return
                
                # verificando se o valor digitado eh valido
                try:
                    vlr_aposta = int(resposta)
                    if 0 < vlr_aposta <= jogador.saldo:
                        jogador.subtrai_saldo(vlr_aposta)
                        break
                    else:
                        print('Valor invalido!')
                        
                # entrada nao eh o caracter F e nem numerico
                except ValueError:
                    print(f'Entrada nao valida!')
            
            # embaralhando a cada rodada
            deck.embaralha_baralho()
            
            # pegando uma "mao" nova na rodada
            jogador.criar_cartas(deck)
            jogador.printa_cartas()
            
            #fazendo ate 3 trocas de cartas
            for i in range(2):
                resposta = input('Digite as cartas que quer trocar(digite enter para nao trocar): ')
                if resposta == '':
                    break

                trocas = [int(x) for x in resposta.split()]
                jogador.trocar_cartas(trocas, deck)
                jogador.printa_cartas()
                
            
            vlr_ganho = self.contar_pontuacao(jogador, vlr_aposta)
            jogador.adiciona_saldo(vlr_ganho)
            print(f'Parabens vc ganhou {vlr_ganho} !!!')
            
            # resetando as cartas do jogador
            jogador.devolver_cartas(deck)
            
    
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
        if len(set(valores)) != 2:
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
    
    def isTrinca(self, qtd):
        return qtd.count(3) == 1
    
    def isDupla(self, qtd):
        return qtd.count(2) == 2
        
