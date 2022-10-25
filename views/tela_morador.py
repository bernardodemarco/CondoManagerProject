from views.tela import Tela
from utils.InvalidCPFException import InvalidCPFException
from utils.validate_cpf import validate_cpf


class TelaMorador(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<MORADORES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Funcionário")
        print("        2 - Alterar Funcionário")
        print("        3 - Excluir Funcionário")
        print("        4 - Listar Funcionário")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(5)

    def pega_dados_morador(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS MORADOR>>=======>")
        try:
            nome = input("Digite o nome do morador: ")
            if kwargs['acao'] == 'alteracao':
                cpf = kwargs['cpf']
            else:
                while True:
                    cpf = input("Digite o CPF do morador: ")
                    try:
                        validate_cpf(cpf)
                    except InvalidCPFException as err:
                        print(err)
                    else:
                        break
                telefone = input("Digite o telefone do morador: ")
                return {"nome": nome, "cpf": cpf, 'telefone': telefone}
        except ValueError:
            print("")
            print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")

    def mostra_morador(self, dados):
        print("\33[1;36m")
        print("<=======<<LISTAGEM DOS MORADORES>>=======>")
        print('NOME DO MORADOR:', dados['nome'])
        print('CPF DO MORADOR:', dados['cpf'])
        print('TELEFONE DO MORADOR:', dados['telefone'])
        print("<=======<<======================>>=======> \033[0m")

    def seleciona_morador(self):
        try:
            print("\33[1;36m")
            cpf_morador = input(('SELECIONE O MORADOR (digite o CPF): '))
            if validate_cpf(cpf_morador):
                return cpf_morador
        except InvalidCPFException as err:
            print(err)
