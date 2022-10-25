from views.tela import Tela


class TelaEntrega(Tela):
    def __init__(self) -> None:
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<ENTREGAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir entrega")
        print("        2 - Alterar entrega")
        print("        3 - Excluir entrega")
        print("        4 - Listar entregas")
        print("        5 - Incluir tipo de entrega")
        print("        6 - Alterar tipo de entrega")
        print("        7 - Excluir tipo de entrega")
        print("        8 - Listar tipos de entregas")
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(8)

    def pega_dados_entrega(self, **kwargs):
        print("<=======<<DADOS ENTREGA>>=======>")     
        # LEMBRAR DE ARRUMAR DESTINATARIO
        destinatario = input('Digite o nome do destinatário:')
        if kwargs['acao'] == 'alteracao':
            id_entrega = kwargs['id_entrega']
        else:
            id_entrega = int(input('Digite um identificador (número inteiro positivo) para a entrega: '))
        
        if (isinstance(id_entrega, int) and id_entrega > 0):
            return {"destinatario": destinatario, 'id': id_entrega}
        else:
            raise ValueError('Valores inválidos, tente novamente!')

    def pega_dados_tipo(self, **kwargs):
        print("<=======<<DADOS TIPO DA ENTREGA>>=======>")

        tipo = input('Digite o nome do tipo da entrega: ')
        if kwargs['acao'] == 'alteracao':
            id_tipo = kwargs['id_tipo']
        else:
            id_tipo = int(input('Digite um identificador (número inteiro positivo) para o tipo de entrega: '))        
        
        if (isinstance(tipo, str) and
                isinstance(id_tipo, int) and id_tipo > 0):
            return {'nome_tipo': tipo, 'id': id_tipo}
        raise ValueError('Valores inválidos, tente novamente!')

    def mostra_entrega(self, dados):
        print('TIPO DA ENGTREGA:', dados['tipo'])
        print('DESTINATARIO DA ENGTREGA:', dados['destinatario'])
        print('DATA DA ENGTREGA AO CONDOMINIO:', dados['data_recebimento_condominio'])
        if dados['data_recebimento_morador'] == None:
            print('MORADOR AINDA NÃO PEGOU A ENTREGA!')
        else:
            print('DATA DA ENGTREGA AO MORADOR:', dados['data_recebimento_morador'])
        print('ID DA ENGTREGA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")

    def mostra_tipo_entrega(self, dados):
        print('TIPO DE ENTREGA:', dados['nome'])
        print('ID DO TIPO DE ENTREGA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")

    def seleciona_entrega(self):
        try:
            id_entrega = int(input(('SELECIONE A ENTREGA (digite o identificador): ')))
            if isinstance(id_entrega, int) and id_entrega > 0:
                return id_entrega
            raise ValueError
        except ValueError:
            raise ValueError('Valor do id inválido')

    def seleciona_tipo_entrega(self):
        try:
            id_tipo = int(input(('SELECIONE O TIPO DE ENTREGA (digite o identificador): ')))
            if isinstance(id_tipo, int) and id_tipo > 0:
                return id_tipo
            raise ValueError
        except ValueError:
            raise ValueError('Valor do id inválido')
