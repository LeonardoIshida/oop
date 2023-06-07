from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, CPF):
        super().__init__(nome, CPF)
        self.salario = None
        
    def calculaSalario(self):
        self.salario = Funcionario.salarioBase * 2