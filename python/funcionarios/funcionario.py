from abc import ABC, abstractmethod

class Funcionario:
    salarioBase = 5000.00
    
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF
    
    @abstractmethod    
    def calculaSalario(self):
        pass
        
    @staticmethod
    def verificaCPF(numero: str):
        try:
            primeiros_dig, resto_dig_str = numero.split('-')
            resto_dig = int(resto_dig_str)
            
            soma_ult = 0
            soma_penult = 0
            mult_penult = [i for i in range(10, 1, -1)]
            mult_ult = [i for i in range(11, 2, -1)]
            for i in range(9):
                soma_ult += (int(primeiros_dig[i]) * mult_ult[i])
                soma_penult += (int(primeiros_dig[i]) * mult_penult[i])
                
            ultimo_dig = resto_dig % 10
            penultimo_dig = resto_dig // 10      
            
            soma_ult += (penultimo_dig * 2)
            resto_ult = ((soma_ult * 10) % 11) % 10
            
            resto_penult = ((soma_penult * 10) % 11) % 10
            
            return resto_penult == penultimo_dig and resto_ult == ultimo_dig
            
        except:
            print('CPF invalido !!')
            return False
            

    