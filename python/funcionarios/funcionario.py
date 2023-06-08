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
    def verificaCPF(CPF: str):
        try:
            soma_ult = 0
            soma_penult = 0
            mult_penult = [i for i in range(10, 1, -1)]
            mult_ult = [i for i in range(11, 2, -1)]
            for i in range(9):
                soma_ult += (int(CPF[i]) * mult_ult[i])
                soma_penult += (int(CPF[i]) * mult_penult[i])
                
            digitos = int(CPF)
            ultimo_dig = digitos % 10
            penultimo_dig = (digitos // 10) % 10    
            
            soma_ult += (penultimo_dig * 2)
            resto_ult = ((soma_ult * 10) % 11)
            if 10 <= resto_ult <= 11:
                resto_ult = 0
            
            resto_penult = ((soma_penult * 10) % 11)
            if 10 <= resto_penult <= 11:
                resto_penult = 0
            
            return resto_penult == penultimo_dig and resto_ult == ultimo_dig
            
        except:
            print('CPF invalido !!')
            return False
            

    