from funcionario import Funcionario

class Assistente(Funcionario):
    
    def __init__(self, nome, CPF):
        super().__init__(nome, CPF)
        
    def calculaSalario(self):
        return Funcionario.salarioBase