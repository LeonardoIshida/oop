from funcionario import Funcionario

class Gerente(Funcionario):
    salario = None
    
    def __init__(self, nome, CPF):
        super().__init__(nome, CPF)
        
    def calculaSalario(self):
        self.salario = Funcionario.salarioBase * 2