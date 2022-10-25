from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.InvalidCPFException import InvalidCPFException
from utils.validate_cpf import validate_cpf
from views.tela import Tela


class TelaFuncionario(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<FUNCIONÁRIOS>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Funcionário")
        print("        2 - Alterar Funcionário")
        print("        3 - Excluir Funcionário")
        print("        4 - Listar Funcionário")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(5)

    def pega_dados_funcionario(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS FUNCIONÁRIO>>=======>")
        try:
            nome = input("Digite o nome do funcionário: ")
            if kwargs['acao'] == 'alteracao':
                cpf = kwargs['cpf']
            else:
                while True:
                    cpf = input("Digite o CPF do funcionário: ")
                    try:
                        validate_cpf(cpf)
                        if not self.controlador_pessoa.pega_pessoa_por_cpf(cpf) == None:
                            raise ResourceAlreadyExistsException("Funcionário")
                    except InvalidCPFException as err:
                        print(err)
                        print("\033[1;32m")
                        if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR\033[1;36m: ").lower() == 'cancelar':
                            return None
                    except ResourceAlreadyExistsException as err:
                        print(err)
                        print("\033[1;32m")
                        if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR\033[1;36m: ").lower() == 'cancelar':
                            return None
                    else:
                        break
                telefone = input("Digite o telefone do funcionário: ")
                return {"nome": nome, "cpf": cpf, 'telefone': telefone}
        except ValueError:
            print("")
            print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
