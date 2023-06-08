from gerente import Gerente
from funcionario import Funcionario
from vendedor import Vendedor
from assistente import Assistente

def folhaSalarial(arrayFuncionarios):
    total = 0
    print('-' * 25)

    for func in arrayFuncionarios:
        try:
            salario_func =  func.calculaSalario()
            total += salario_func

            print(f'{func.nome} || {salario_func}')
            print('-' * 25)
        except:
            continue

    print(f'Folha salarial = {total}')

if __name__ == '__main__':
    n = 7
    lista_func = []
    lista_cpf = []
    lista_nomes = []

    lista_cpf.append("59382082034")
    lista_nomes.append("Lionel Messi")

    lista_cpf.append("47910702086")
    lista_nomes.append("Farid Tari")

    lista_cpf.append("85841264060")
    lista_nomes.append("Cristiano Ronaldo")

    lista_cpf.append("32347464000")
    lista_nomes.append("Lebron James")

    lista_cpf.append("43355267090")
    lista_nomes.append("Lewis Hamilon")

    lista_cpf.append("21198182075")
    lista_nomes.append("Tiger Woods")

    lista_cpf.append("12345678901")
    lista_nomes.append("Nikola Kovac")

    for i in range(n):
        tipo_func = i % 3

        if Funcionario.verificaCPF(lista_cpf[i]):
            match tipo_func:
                case 0:
                    lista_func.append(Gerente(lista_nomes[i], lista_cpf[i]))
                case 1:
                    lista_func.append(Assistente(lista_nomes[i], lista_cpf[i]))
                case 2:
                    lista_func.append(Vendedor(lista_nomes[i], lista_cpf[i], 125.64))
    
    folhaSalarial(lista_func)