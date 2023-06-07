from gerente import Gerente
from funcionario import Funcionario
from vendedor import Vendedor
from assistente import Assistente

def folhaSalarial(arrayFuncionarios):
    total = 0
    for func in arrayFuncionarios:
        func.calculaSalario()
        print('-' * 25)
        print(f'{func.nome} || {func.salario}')

        total += func.salario
    print('-' * 25)

    print(f'Salario total = {total}')

def menu():
    print('1) Criar gerente')
    print('2) Criar assistente')
    print('3) Criar vendedor')
    print('4) Sair')


if __name__ == '__main__':
    lista_func = []
    
    while True:
        
        menu()
        opt = int(input('Digite a opcao: '))

        if opt == 4:
            break
        
        novo_CPF = input('Digite o CPF: ')
        if Funcionario.verificaCPF(novo_CPF) == False:
            print('Nao foi possivel instanciar um novo Objeto')
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
        
    folhaSalarial(lista_func)