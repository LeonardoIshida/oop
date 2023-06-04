from gerente import Gerente
from funcionario import Funcionario
from vendedor import Vendedor
from assistente import Assistente

if __name__ == '__main__':
    lista_func = []
    
    while True:
        try:
            print("""1) Criar gerente\n2) Criar assistente\n3) Criar vendedor\n14) Alterar salario base""")
            opt = int(input('Digite a opcao: '))
            
            if opt == 4:
                novo_salario_base = float(input('Digite o valor do salario base: '))
                Funcionario.salarioBase
            else:    
                novo_CPF = input('Digite o CPF: ')
                if Funcionario.verificaCPF(novo_CPF) == False:
                    print('Nao foi possivel instanciar uma nova Classe')
                    continue
                
                nome = input('Digite o nome do funcionario: ')
                match opt:
                    case 1:
                        lista_func.append(Gerente(nome, novo_CPF))
                    case 2:
                        lista_func.append(Assistente(nome, novo_CPF))
                    case 3:
                        comissao = float(input('Digite o valor da comissao: '))
                        lista_func.append(Vendedor(nome, novo_CPF, comissao))
            
        except EOFError:
            break
        
    print('-'*20)
    for func in lista_func:
        print(f'{func.nome} | {func.salario}')
        print('-'*20)