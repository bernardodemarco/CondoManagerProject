from views.tela import Tela

from utils.date_helpers import convert_datetime

class TelaEntrega(Tela):
    def __init__(self) -> None:
        super().__init__()

    def mostra_opcoes(self):
        print("")
        print("<=======<<ENTREGAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir entrega")
        print("        2 - Alterar entrega")
        print("        3 - Excluir entrega")
        print("        4 - Listar entregas")
        print("        5 - Listar entregas pendentes")
        print("        6 - Incluir tipo de entrega")
        print("        7 - Alterar tipo de entrega")
        print("        8 - Excluir tipo de entrega")
        print("        9 - Listar tipos de entregas")
        print("        10 - Registrar recebimento da entrega pelo morador")
        print("        0 - Retornar")
        print("<=======<<===========>>=======>")
        return self.checa_opcao(10)

    def pega_dados_entrega(self, **kwargs):
        print("")
        print("<=======<<DADOS ENTREGA>>=======>")
        while True:
            try:
                if kwargs['acao'] == 'alteracao':
                    id_entrega = kwargs['id_entrega']
                else:
                    id_entrega = int(
                        input('Digite um identificador (número inteiro positivo) para a entrega: '))

                if (isinstance(id_entrega, int) and id_entrega > 0):
                    return {'id': id_entrega}
                else:
                    raise ValueError
            except ValueError:
                print("")
                print('Valores inválidos tente novamente!')
                print("")

    def pega_dados_tipo(self, **kwargs):
        print("")
        print("<=======<<DADOS TIPO DA ENTREGA>>=======>")
        while True:
            try:
                tipo = input('Digite o nome do tipo da entrega: ')
                if kwargs['acao'] == 'alteracao':
                    id_tipo = kwargs['id_tipo']
                else:
                    id_tipo = int(input(
                        'Digite um identificador (número inteiro positivo) para o tipo de entrega: '))

                if (isinstance(id_tipo, int) and id_tipo > 0):
                    return {'nome_tipo': tipo, 'id': id_tipo}
                raise ValueError
            except ValueError:
                print("")
                print('Valores inválidos, tente novamente!')
                print("")

    def mostra_entrega(self, dados):
        print('TIPO DA ENGTREGA:', dados['tipo'])
        print('DESTINATARIO DA ENGTREGA:', dados['destinatario'])
        print('DATA DA ENGTREGA AO CONDOMINIO:',
              convert_datetime(dados['data_recebimento_condominio']))
        
        if dados['data_recebimento_morador'] == None:
            print(dados['destinatario'], 'AINDA NÃO COLETOU A SUA ENTREGA!')
        else:
            print('DATA DA ENGTREGA AO MORADOR:',
                  convert_datetime(dados['data_recebimento_morador']))

        if dados['tempo'] != None:
            print('MORADOR DEMOROU:', dados['tempo'], '(horas:minutos:segundos) para coletar a entrega')
        
        print('ID DA ENGTREGA:', dados['id'])
        print("<=======<<===========>>=======>")

    def mostra_tipo_entrega(self, dados):
        print('TIPO DE ENTREGA:', dados['nome'])
        print('ID DO TIPO DE ENTREGA:', dados['id'])
        print("<=======<<===========>>=======>")

    def seleciona_entrega(self):
        while True:
            try:
                id_entrega = int(
                    input(('SELECIONE A ENTREGA (digite o identificador): ')))
                if isinstance(id_entrega, int) and id_entrega > 0:
                    return id_entrega
                raise ValueError
            except ValueError:
                print("")
                print('Valor do id inválido')
                print("")

    def seleciona_tipo_entrega(self):
        while True:
            try:
                id_tipo = int(
                    input(('SELECIONE O TIPO DE ENTREGA (digite o identificador): ')))
                if isinstance(id_tipo, int) and id_tipo > 0:
                    return id_tipo
                raise ValueError
            except ValueError:
                print("")
                print('Valor do id inválido')
                print("")
