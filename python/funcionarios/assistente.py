from funcionario import Funcionario

class Assistente(Funcionario):
    def __init__(self, nome, CPF):
        super().__init__(nome, CPF)
        self.salario
        
    def calculaSalario(self):
        self.salario = Funcionario.salarioBase