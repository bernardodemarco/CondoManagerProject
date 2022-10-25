from views.tela import Tela
from utils.InvalidCPFException import InvalidCPFException


class TelaMorador(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa

    def mostra_opcoes(self):
        pass

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
