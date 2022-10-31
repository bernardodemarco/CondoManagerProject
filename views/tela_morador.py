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
        print("<=======<<MORADORES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Morador")
        print("        2 - Alterar Morador")
        print("        3 - Excluir Morador")
        print("        4 - Listar Moradores")
        print("        5 - Visitas")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(5)

    def pega_dados_morador(self, apartamentos, **kwargs):
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
                print("ERRO!: Nome inválido, por favor, tente novamente")
        while True:
            try:
                telefone = input("Digite o telefone do morador: ")
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', telefone)) == False:
                    raise Exception
                else:
                    break
            except Exception:
                print("ERRO!: Telefone inválido, por favor, tente novamente")
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
                    print("ERRO!: Número inválido! Por favor, tente novamente!")
        print("<=======<<==================>>=======>")        
        return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'apartamento': apartamento}

    def mostra_morador(self, dados):
        print('NOME DO MORADOR:', dados['nome'])
        print('TELEFONE DO MORADOR:', dados['telefone'])
        print('CPF DO MORADOR:', dados['cpf'])
        print('APARTAMENTO:', dados["apartamento"])
        print("<=======<<======================>>=======>")

    def seleciona_morador(self):
        while True:
            try:
                cpf_morador = input(('SELECIONE O MORADOR (digite o CPF): '))
                validate_cpf(cpf_morador)
                if self.__controlador_pessoa.pega_morador_por_cpf(cpf_morador) is not None:
                    return cpf_morador
                else:
                    raise ResourceNotFoundException("Morador")
            except InvalidCPFException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None
            except ResourceNotFoundException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None

#   VISITANTES  #

    def mostra_opcoes_visitantes(self):
        print("<=======<<VISITANTES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Visitante")
        print("        2 - Alterar Visitante")
        print("        3 - Excluir Visitante")
        print("        4 - Listar Visitante")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(4)

    def pega_dados_visitante(self, morador, **kwargs):
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
                print("ERRO!: Nome inválido, por favor, tente novamente")
        while True:
            try:
                telefone = input("Digite o telefone do visitante: ")
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
                cpf = input("Digite o CPF do visitante: ")
                try:
                    validate_cpf(cpf)
                    if self.__controlador_pessoa.pega_visitante_por_cpf(morador, cpf) and self.__controlador_pessoa.pega_morador_por_cpf(cpf):
                        raise ResourceAlreadyExistsException
                except (InvalidCPFException, ResourceAlreadyExistsException)as err:
                    print(err)
                else:
                    break
        print("<=======<<==================>>=======>")        
        return {"nome": nome, "cpf": cpf, 'telefone': telefone}
    
    def seleciona_visitante(self, morador):
        while True:
            try:
                cpf_visitante = input(('SELECIONE O VISITANTE (digite o CPF): '))
                validate_cpf(cpf_visitante)
                if self.__controlador_pessoa.pega_visitante_por_cpf(morador, cpf_visitante) is not None:
                    return cpf_visitante
                else:
                    raise ResourceNotFoundException("Visitante")
            except InvalidCPFException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None
            except ResourceNotFoundException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    return None
    
    def mostra_visitante(self, dados):
        print('NOME DO VISITANTE:', dados['nome'])
        print('TELEFONE DO VISITANTE:', dados['telefone'])
        print('CPF DO VISITANTE:', dados['cpf'])
        print("<=======<<======================>>=======>")
        