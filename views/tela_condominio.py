from cmath import exp
from views.tela import Tela
import time


class TelaCondominio(Tela):

    def __init__(self, controlador_condo):
        super().__init__()
        self.__controlador_condo = controlador_condo

    @property
    def controlador_condo(self):
        return self.__controlador_condo

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONDOMÍNIOS>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Condomínio")
        print("        2 - Alterar Condomínio")
        print("        3 - Excluir Condomínio")
        print("        4 - Listar Condomínios")
        print("        5 - Outras opções")
        print("        0 - Desligar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(5)

    def mostra_opcoes_2(self):
        print("\033[1;36m")
        print("<=======<<OUTRAS OPÇÕES>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Apartamentos")
        print("        2 - Moradores")
        print("        3 - Funcionários")
        print("        4 - Contas")
        print("        5 - Reservável")
        print("        6 - Reservas")
        print("        7 - Entregas")
        print("        0 - Condomínios")
        print("<=======<<=============>>=======> \033[0m")
        return self.checa_opcao(7)

    def mostra_opcoes_apartamento(self):
        print("\033[1;36m")
        print("<=======<<APARTAMENTOS>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Incluir Apartamento")
        print("        2 - Alterar Apartamento")
        print("        3 - Excluir Apartamento")
        print("        4 - Listar Apartamentos")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(4)

    def mostra_opcoes_reservavel(self):
        print("\033[1;36m")
        print("<=======<<RESERVÁVEL>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Incluir Reservável")
        print("        2 - Alterar Reservável")
        print("        3 - Excluir Reservável")
        print("        4 - Listar Reservável")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(4)

    def mostra_condo(self, dados):
        print("\033[1;36m")
        print("<=======<<LISTA DE CONDOMINIOS>>=======>")
        print('NOME DO CONDOMÍNIO:', dados['nome'])
        print('NÚMERO DO CONDOMÍNIO:', dados['numero'])
        print('ENDEREÇO DO CONDOMÍNIO:', dados['endereco'])
        print('APARTAMENTOS DISPONÍVEIS: ', ", ".join(dados["apartamentos"]))
        print("<=======<<====================>>=======> \033[0m")

    def seleciona_condo(self):
        while True:
            try:
                print("\033[1;36m")
                numero = int(
                    input("SELECIONE O CONDOMÍNIO (digite o numero): "))
                if isinstance(numero, int) and numero > 0:
                    return numero
                raise ValueError
            except ValueError:
                print(
                    "\033[0;31mERRO!: Número inválido, por favor, tente novamente: \033[1;36m")

    def pega_dados_condo(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS CONDOMÍNIO>>=======>")
        nome = input("Digite o nome do condomínio: ")
        if kwargs['acao'] == 'alteracao':
            numero = kwargs['numero']
        else:
            while True:
                try:
                    numero = int(
                        input("Digite um número único (positivo) pro condomínio: "))
                    if numero <= 0:
                        raise ValueError
                except ValueError:
                    print("")
                    print(
                        "\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
                else:
                    break
        endereco = input("Digite o endereço do condomínio: ")
        apartamento = input("Digite o número de apartamentos deste condomínio: ")
        return {"nome": nome, "numero": numero, 'endereco': endereco, "apartamento": apartamento}

    def pega_dados_reservavel(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS RESERVAVEL>>=======>")
        nome = input("Digite o nome do reservável: ")
        if kwargs['acao'] == 'alteracao':
            id_reservavel = kwargs['id_reservavel']
        else:
            while True:
                try:
                    id_reservavel = int(
                        input("Digite um número único (positivo) pro reservável: "))
                    if id_reservavel <= 0:
                        raise ValueError
                except ValueError:
                    print("")
                    print(
                        "\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
                else:
                    break
        return {"nome": nome, "id_reservavel": id_reservavel}

    def mostra_reservavel(self, dados):
        print("\33[1;36m")
        print("<=======<<LISTAGEM DOS RESERVÁVEL>>=======>") 
        print('NOME DO RESERVÁVEL:', dados['nome'])
        print('ID DO RESERVÁVEL:', dados['id_reservavel'])
        print("<=======<<=======================>>=======> \033[0m")

    def seleciona_reservavel(self):
        while True:
            try:
                print("\33[1;36m")
                id_reservavel = input(('SELECIONE O RESERVÁVEL (digite o ID): '))
                if self.__controlador_condo.pega_reservavel_por_id(id_reservavel) is not None:
                    return id_reservavel
                else:
                    raise ResourceNotFoundException("Reservável")
            except ResourceNotFoundException as err:
                print(err)
                print("\033[1;32m")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR\033[1;36m: ").lower() == 'cancelar':
                    return None