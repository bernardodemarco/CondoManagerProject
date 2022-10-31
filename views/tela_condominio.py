from multiprocessing.sharedctypes import Value
from views.tela import Tela

from utils.ResourceNotFoundException import ResourceNotFoundException


class TelaCondominio(Tela):

    def __init__(self, controlador_condo):
        super().__init__()
        self.__controlador_condo = controlador_condo

    @property
    def controlador_condo(self):
        return self.__controlador_condo

    def mostra_opcoes(self):
        print("<=======<<CONDOMÍNIO>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Alterar Condomínio")
        print("        2 - Mostrar Dados")
        print("        3 - Outras opções")
        print("        4 - Resetar")
        print("        0 - Desligar")
        print("<=======<<==========>>=======>")
        return self.checa_opcao(4)

    def mostra_opcoes_2(self):
        print("<=======<<OUTRAS OPÇÕES>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Moradores")
        print("        2 - Funcionários")
        print("        3 - Contas")
        print("        4 - Reservável")
        print("        5 - Reservas")
        print("        6 - Entregas")
        print("        0 - Condomínios")
        print("<=======<<=============>>=======>")
        return self.checa_opcao(6)

    def mostra_opcoes_reservavel(self):
        print("<=======<<RESERVÁVEL>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Incluir Reservável")
        print("        2 - Alterar Reservável")
        print("        3 - Listar Reservável")
        print("        4 - Excluir Reservável")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(4)

    def mostra_condo(self, dados):
        print("<=======<<DADOS DO CONDOMÍNIO>>=======>")
        print('NOME DO CONDOMÍNIO:', dados['nome'])
        print('CIDADE DO CONDOMÍNIO:', dados['cidade'])
        print('RUA DO CONDOMÍNIO:', dados['rua'])
        print('NÚMERO DO CONDOMÍNIO:', dados['numero'])
        print('APARTAMENTOS DISPONÍVEIS:', ", ".join(dados["apartamentos"]))
        print("<=======<<===================>>=======>")

    def seleciona_condo(self):
        while True:
            try:
                numero = int(
                    input("SELECIONE O CONDOMÍNIO (digite o numero): "))
                if isinstance(numero, int) and numero > 0:
                    return numero
                raise ValueError
            except ValueError:
                print(
                    "ERRO!: Número inválido, por favor, tente novamente:")

    def pega_dados_condo(self, **kwargs):
        print("<=======<<DADOS CONDOMÍNIO>>=======>")
        nome = input("Digite o nome do condomínio: ")
        while True:
            try:
                cidade = input("Digite a cidade do condomínio: ")
                if not cidade.isalpha():
                    raise ValueError
            except ValueError:
                print("ERRO!: Cidade inválida! Por favor, tente novamente!")
            else:
                break
        while True:
            try:
                rua = input("Digite a rua do condomínio: ")
                if rua.isdigit():
                    raise ValueError
            except ValueError:
                print("ERRO!: Rua inválida! Por favor, tente novamente!")
            else:
                break
        while True:
            try:
                numero = int(
                    input("Digite o número do condomínio: "))
                if numero <= 0:
                    raise ValueError
            except ValueError:
                print("ERRO!: Número inválido! Por favor, tente novamente!")
            else:
                break
        while True:
            try:
                apartamento = int(input("Digite o número de apartamentos deste condomínio: "))         
                if kwargs['acao'] == 'alteracao':
                    for i in range(1, self.__controlador_condo.condominio.apartamentos[-1]):
                        if i not in self.__controlador_condo.condominio.apartamentos:
                            if int(apartamento) < i:
                                raise ValueError
            except ValueError:
                print("ERRO!: Número inválido! Por favor, tente novamente!")
            else:
                break
        return {"nome": nome, "cidade": cidade, "rua": rua, "numero": numero,  "apartamento": apartamento}

    def pega_dados_reservavel(self, **kwargs):
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
                        "ERRO!: Número inválido! Por favor, tente novamente!")
                else:
                    break
        return {"nome": nome, "id_reservavel": id_reservavel}

    def mostra_reservavel(self, dados):
        print("<=======<<LISTAGEM DOS RESERVÁVEL>>=======>") 
        print('NOME DO RESERVÁVEL:', dados['nome'])
        print('ID DO RESERVÁVEL:', dados['id'])
        print("<=======<<=======================>>=======>")

    def seleciona_reservavel(self):
        while True:
            try:
                id_reservavel = int(input(('SELECIONE O RESERVÁVEL (digite o ID): ')))
                reservavel = self.__controlador_condo.pega_reservavel_por_id(id_reservavel)
                if reservavel is not None:
                    return reservavel
                else:
                    raise ResourceNotFoundException("Reservável")
            except ResourceNotFoundException as err:
                print(err)
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR: ").lower() == 'cancelar':
                    return None