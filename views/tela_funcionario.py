from utils.InvalidCPFException import InvalidCPFException
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.validate_cpf import validate_cpf
from views.tela import Tela
import re


class TelaFuncionario(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa

    def mostra_opcoes(self):
        print("<=======<<FUNCIONÁRIOS>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Funcionário")
        print("        2 - Alterar Funcionário")
        print("        3 - Excluir Funcionário")
        print("        4 - Listar Funcionário")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(5)

    def pega_dados_funcionario(self, **kwargs):
        print("<=======<<DADOS FUNCIONÁRIO>>=======>")
        while True:
            try:
                nome = input("Digite o nome do funcionário: ")
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', nome)) == False:
                    raise Exception
                else:
                    nome = nome.title()
                    break
            except Exception:
                print("ERRO!: Nome inválido, por favor, tente novamente")
        while True:
            try:
                telefone = input("Digite o telefone do funcionário: ")
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', telefone)) == False:
                    raise Exception
                else:
                    break
            except Exception:
                print("ERRO!: Telefone inválido, por favor, tente novamente")
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs['cpf']
        else:
            while True:
                cpf = input("Digite o CPF do funcionário: ")
                try:
                    validate_cpf(cpf)
                    if self.__controlador_pessoa.pega_funcionario_por_cpf(cpf):
                        raise ResourceAlreadyExistsException("Funcionário")
                except (InvalidCPFException, ResourceAlreadyExistsException) as err:
                    print(err)
                else:
                    break
        while True:
            try:
                cargo = input("Digite o cargo do funcionário: ")
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', cargo)) == False:
                    raise Exception
                else:
                    cargo = cargo.title()
                    break
            except Exception:
                print("ERRO!: Cargo inválido, por favor, tente novamente")
        while True:
            try:
                salario = float(input("Digite o valor do salário deste funcionário: "))
                if salario <= 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("ERRO!: Valor inválido, por favor, tente novamente")
        print("<=======<<==================>>=======>")
        return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'cargo': cargo, 'salario': salario}


    def mostra_funcionario(self, dados):
        print('NOME DO FUNCIONÁRIO:', dados['nome'])
        print('TELEFONE DO FUNCIONÁRIO:', dados['telefone'])
        print('CPF DO FUNCIONÁRIO:', dados['cpf'])
        print('CARGO DO FUNCIONÁRIO:', dados['cargo'])
        print(f'SALÁRIO DO FUNCIONÁRIO: R${dados["salario"]:.2f}')
        print("<=======<<======================>>=======>")

    def seleciona_funcionario(self):
        while True:
            try:
                cpf_funcionario = input(('SELECIONE O FUNCIONÁRIO (digite o CPF): '))
                validate_cpf(cpf_funcionario)
                if self.__controlador_pessoa.pega_funcionario_por_cpf(cpf_funcionario) is not None:
                    return cpf_funcionario
                else:
                    raise ResourceNotFoundException("Funcionário")
            except InvalidCPFException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None
            except ResourceNotFoundException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None
