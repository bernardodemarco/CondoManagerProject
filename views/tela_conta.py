from views.tela import Tela
import time


class TelaConta(Tela):
    def __init__(self) -> None:
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONTAS>>=======>")
        print("O que você gostaria de fazer?")
        time.sleep(1)
        print("        1 - Incluir conta")
        time.sleep(0.5)
        print("        2 - Alterar conta")
        time.sleep(0.5)
        print("        3 - Excluir conta")
        time.sleep(0.5)
        print("        4 - Listar contas")
        time.sleep(1)
        print("        5 - Incluir tipo conta")
        time.sleep(0.5)
        print("        6 - Alterar tipo conta")
        time.sleep(0.5)
        print("        7 - Excluir tipo conta")
        time.sleep(0.5)
        print("        8 - Listar tipo conta")
        time.sleep(0.5)        
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(8)

    def pega_dados_contas(self, **kwargs):
        print("<=======<<DADOS CONTA>>=======>")

        valor = float(input("Digite o valor da conta: "))
        mes = input('Digite o mês: ')
        if kwargs['acao'] == 'alteracao':
            id_conta = kwargs['id_conta']
        else:
            id_conta = int(
                input('Digite um identificador (número inteiro positivo) para a conta: '))

        if (isinstance(valor, float) and
                valor >= 0 and isinstance(mes, str) and
                isinstance(id_conta, int) and id_conta > 0):
            return {"valor": valor, "mes": mes, 'id': id_conta}
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

        if (isinstance(tipo, str) and
                isinstance(id_tipo, int) and id_tipo > 0):
            return {'nome_tipo': tipo, 'id': id_tipo}
        raise ValueError('Valores inválidos, tente novamente!')

    def mostra_conta(self, dados):
        print('TIPO DA CONTA:', dados['tipo'])
        time.sleep(0.5)
        print('VALOR DA CONTA:', dados['valor'])
        time.sleep(0.5)
        print('MES DA CONTA:', dados['mes'])
        time.sleep(0.5)
        print('ID DA CONTA:', dados['id'])
        time.sleep(0.5)
        print("<=======<<===========>>=======> \033[0m")

    def mostra_tipo_conta(self, dados):
        print('TIPO DE CONTA:', dados['nome'])
        time.sleep(0.5)
        print('ID DO TIPO DE CONTA:', dados['id'])
        time.sleep(0.5)
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
