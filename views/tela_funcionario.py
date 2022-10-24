from utils.InvalidCPFException import InvalidCPFException
from utils.validate_cpf import validate_cpf
from views.tela import Tela


class TelaFuncionario(Tela):
    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def pega_dados_funcionario(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS FUNCIONÁRIO>>=======>")
        try:
            nome = input("Digite o nome do funcionário: ")
            if kwargs['acao'] == 'alteracao':
                cpf = kwargs['cpf']
            else:
                while True:
                    cpf = int(input("Digite o CPF do funcionário: "))
                    try:
                        validate_cpf(cpf)
                    except InvalidCPFException as err:
                        print(err)
                    else:
                        break
                telefone = input("Digite o telefone do funcionário: ")
                return {"nome": nome, "cpf": cpf, 'telefone': telefone}
        except ValueError:
            print("")
            print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
