from views.tela import Tela
from utils.InvalidCPFException import InvalidCPFException
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.validate_cpf import validate_cpf


class TelaMorador(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<MORADORES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Morador")
        print("        2 - Alterar Morador")
        print("        3 - Excluir Morador")
        print("        4 - Listar Moradores")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(5)

    def pega_dados_morador(self, apartamentos, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS MORADOR>>=======>")
        try:
            nome = input("Digite o nome do morador: ")
            telefone = input("Digite o telefone do morador: ")
            if kwargs['acao'] == 'alteracao':
                cpf = kwargs['cpf']
                apartamento = kwargs['apartamento']
            else:
                while True:
                    cpf = input("Digite o CPF do morador: ")
                    try:
                        validate_cpf(cpf)
                    except InvalidCPFException as err:
                        print(err)
                    else:
                        break
                while True:
                    try:
                        apartamento = int(input("Digite o apartamento do morador: "))
                        if apartamento not in apartamentos:
                            raise Exception
                        else:
                            break
                    except Exception:
                        print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
            return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'apartamento': apartamento}
        except ValueError:
            print("")
            print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
    

    def mostra_morador(self, dados):
        print('NOME DO MORADOR:', dados['nome'])
        print('TELEFONE DO MORADOR:', dados['telefone'])
        print('CPF DO MORADOR:', dados['cpf'])
        print('APARTAMENTO: ', dados["apartamento"])
        print("<=======<<======================>>=======> \033[0m")

    def seleciona_morador(self):
        while True:
            try:
                print("\33[1;36m")
                cpf_morador = input(('SELECIONE O MORADOR (digite o CPF): '))
                validate_cpf(cpf_morador)
                if self.__controlador_pessoa.pega_morador_por_cpf(cpf_morador) is not None:
                    return cpf_morador
                else:
                    raise ResourceNotFoundException("Morador")
            except InvalidCPFException as err:
                print(err)
                print("\033[1;32m")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR\033[1;36m: ").lower() == 'cancelar':
                    return None
            except ResourceNotFoundException as err:
                print(err)
                print("\033[1;32m")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR\033[1;36m: ").lower() == 'cancelar':
                    return None
