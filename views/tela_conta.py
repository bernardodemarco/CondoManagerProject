from utils.date_helpers import convert_date
from views.tela import Tela

from datetime import date 


class TelaConta(Tela):
    def __init__(self) -> None:
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONTAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir conta")
        print("        2 - Alterar conta")
        print("        3 - Excluir conta")
        print("        4 - Listar contas")
        print("        5 - Incluir tipo conta")
        print("        6 - Alterar tipo conta")
        print("        7 - Excluir tipo conta")
        print("        8 - Listar tipo conta")
        print("        9 - Gerar relatório das contas por mês")
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(8)

    def pega_dados_contas(self, **kwargs):
        print("<=======<<DADOS CONTA>>=======>")

        valor = float(input("Digite o valor da conta: "))
        print('A conta é referente a qual data?')
        dia = int(input('Digite o dia (de 1 a 31): '))
        mes = int(input('Digite o mês (de 1 a 12): '))
        ano = int(input('Digite o ano: '))
        if kwargs['acao'] == 'alteracao':
            id_conta = kwargs['id_conta']
        else:
            id_conta = int(
                input('Digite um identificador (número inteiro positivo) para a conta: '))

        if (isinstance(valor, float) and
                valor >= 0 and isinstance(mes, int) and
                1 <= mes <= 12 and isinstance(dia, int) and
                1 <= dia <= 31 and isinstance(ano, int) and
                isinstance(id_conta, int) and id_conta > 0):
            data = date(ano, mes, dia)
            return {"valor": valor, 'id': id_conta, 'data': data}
        else:
            raise ValueError('Valores inválidos, tente novamente!')

    def pega_dados_tipo(self, **kwargs):
        print("<=======<<DADOS TIPO DA CONTA>>=======>")

        tipo = input('Digite o nome do tipo da conta: ')
        if kwargs['acao'] == 'alteracao':
            id_tipo = kwargs['id_tipo']
        else:
            id_tipo = int(input(
                'Digite um identificador (número inteiro positivo) para o tipo da conta: '))

        if (isinstance(id_tipo, int) and id_tipo > 0):
            return {'nome_tipo': tipo, 'id': id_tipo}
        raise ValueError('Valores inválidos, tente novamente!')

    def mostra_conta(self, dados):
        print('TIPO DA CONTA:', dados['tipo'])
        print('VALOR DA CONTA:', dados['valor'])
        print('DATA DA CONTA', convert_date(dados['data']))
        print('ID DA CONTA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")

    def mostra_tipo_conta(self, dados):
        print('TIPO DE CONTA:', dados['nome'])
        print('ID DO TIPO DE CONTA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")

    def seleciona_conta(self):
        try:
            id_conta = int(
                input(('SELECIONE A CONTA (digite o identificador): ')))
            if isinstance(id_conta, int) and id_conta > 0:
                return id_conta
            raise ValueError
        except ValueError:
            raise ValueError('Valor do id inválido')

    def seleciona_tipo_conta(self):
        try:
            id_tipo = int(
                input(('SELECIONE O TIPO DE CONTA (digite o identificador): ')))
            if isinstance(id_tipo, int) and id_tipo > 0:
                return id_tipo
            raise ValueError
        except ValueError:
            raise ValueError('Valor do id inválido')
