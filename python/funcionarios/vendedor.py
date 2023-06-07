from funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, CPF, comissao):
        super().__init__(nome, CPF)
        self.comissao = comissao
        self.salario
        
    def calculaSalario(self):
        self.salario = Funcionario.salarioBase + self.comissao