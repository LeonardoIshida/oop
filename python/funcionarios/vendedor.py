from funcionario import Funcionario

class Vendedor(Funcionario):
    
    def __init__(self, nome, CPF, comissao):
        super().__init__(nome, CPF)
        self.comissao = comissao
        
    def calculaSalario(self):
        return Funcionario.salarioBase + self.comissao