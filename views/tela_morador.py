from views.tela import Tela
from utils.InvalidCPFException import InvalidCPFException
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.validate_cpf import validate_cpf
import re


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
        print("        5 - Visitas")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(5)

    def pega_dados_morador(self, apartamentos, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS MORADOR>>=======>")
        while True:
            try:
                nome = input("Digite o nome do morador: ")
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', nome)) == False:
                    raise Exception
                else:
                    nome = nome.title()
                    break
            except Exception:
                print("\033[0;31m")
                print("ERRO!: Nome inválido, por favor, tente novamente")
                print("\033[1;36m")
        while True:
            try:
                telefone = input("Digite o telefone do morador: ")
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', telefone)) == False:
                    raise Exception
                else:
                    break
            except Exception:
                print("\033[0;31m")
                print("ERRO!: Telefone inválido, por favor, tente novamente")
                print("\033[1;36m")
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs['cpf']
            apartamento = kwargs['apartamento']
        else:
            while True:
                cpf = input("Digite o CPF do morador: ")
                try:
                    validate_cpf(cpf)
                    if self.__controlador_pessoa.pega_morador_por_cpf(cpf):
                        raise ResourceAlreadyExistsException("Morador")
                except (InvalidCPFException, ResourceAlreadyExistsException) as err:
                    print("\033[0;31m")
                    print(err)
                    print("\033[1;36m")
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
                    print("\033[0;31m")
                    print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
                    print("\033[1;36m")
        print("<=======<<==================>>=======>")        
        return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'apartamento': apartamento}

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
                morador = self.__controlador_pessoa.pega_morador_por_cpf(cpf_morador)
                if morador is not None:
                    return morador
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

#   VISITANTES  #

    def mostra_opcoes_visitantes(self):
        print("\033[1;36m")
        print("<=======<<VISITANTES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Visitante")
        print("        2 - Alterar Visitante")
        print("        3 - Excluir Visitante")
        print("        4 - Listar Visitante")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(4)

    def pega_dados_visitante(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS VISITANTE>>=======>")
        while True:
            try:
                nome = input("Digite o nome do visitante: ")
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', nome)) == False:
                    raise Exception
                else:
                    nome = nome.title()
                    break
            except Exception:
                print("\033[0;31m")
                print("ERRO!: Nome inválido, por favor, tente novamente")
                print("\033[1;36m")
        while True:
            try:
                telefone = input("Digite o telefone do visitante: ")
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', telefone)) == False:
                    raise Exception
                else:
                    break
            except Exception:
                print("\033[0;31m")
                print("ERRO!: Telefone inválido, por favor, tente novamente")
                print("\033[1;36m")
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs['cpf']
        else:
            while True:
                cpf = input("Digite o CPF do visitante: ")
                try:
                    validate_cpf(cpf)
                except InvalidCPFException as err:
                    print("\033[0;31m")
                    print(err)
                    print("\033[1;36m")
                else:
                    break
        print("<=======<<==================>>=======>")        
        return {"nome": nome, "cpf": cpf, 'telefone': telefone}