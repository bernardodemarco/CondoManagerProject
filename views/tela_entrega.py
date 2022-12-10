import PySimpleGUI as sg

from views.tela import Tela

from utils.date_helpers import convert_datetime

class TelaEntrega(Tela):
    def __init__(self) -> None:
        super().__init__()
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        layout = [
            [sg.Text('-------- ENTREGAS ----------', font=("Helvica", 25))],
            [sg.Text('O que você gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir entrega', "RD1", key='1')],
            [sg.Radio('Alterar entrega', "RD1", key='2')],
            [sg.Radio('Excluir entrega', "RD1", key='3')],
            [sg.Radio('Listar entregas', "RD1", key='4')],
            [sg.Radio('Listar entregas pendentes', "RD1", key='5')],
            [sg.Radio('Incluir um tipo de entrega', "RD1", key='6')],
            [sg.Radio('Alterar um tipo de entrega', "RD1", key='7')],
            [sg.Radio('Excluir um tipo de entrega', "RD1", key='8')],
            [sg.Radio('Listar os tipos de entregas', "RD1", key='9')],
            [sg.Radio('Registrar recebimento da entrega pelo morador', "RD1", key='10')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Contas').Layout(layout)
    
    def mostra_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def pega_dados_entrega(self):
        while True:
            layout = [
                [sg.Text('-------- CADASTRO DE ENTREGAS ----------', font=("Helvica", 25))],
                [sg.Text('ID (número inteiro positivo) para a entrega:', size=(30, 1)), sg.InputText('', key='id_entrega')],
                [sg.Button('Cadastrar Entrega')]
            ]
            self.__window = sg.Window('Cadastro de entregas').Layout(layout)
            button, values = self.open()
            try:
                if button is None:
                    raise ValueError
                id_entrega = int(values['id_entrega'])
                self.close()
                if (id_entrega > 0):
                    return {'id': id_entrega}
                else:
                    raise ValueError
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos tente novamente!')

    def pega_dados_tipo(self, **kwargs):
        while True:
            layout = [
                [sg.Text('-------- CADASTRO TIPOS DE ENTREGAS ----------', font=("Helvica", 25))],
                [sg.Text('Digite o nome do tipo da entrega:', size=(50, 1)), sg.InputText('', key='tipo')],
                [sg.Button('Cadastrar Tipo De Entrega')]
            ]
            if kwargs['acao'] == 'alteracao':
                id_tipo = kwargs['id_tipo']
            else:
                layout.insert(
                    2, [sg.Text('Digite um identificador (número inteiro positivo) para o tipo de entrega:', size=(50, 1)), sg.InputText('', key='id_tipo')]
                )
            self.__window = sg.Window('Cadastro de tipos de entregas').Layout(layout)
            button, values = self.open()
            try:
                if button is None:
                    raise ValueError
                if 'id_tipo' in values:
                    id_tipo = int(values['id_tipo'])
                self.close()
                if (id_tipo > 0):
                    return {'nome_tipo': values['tipo'], 'id': id_tipo}
                raise ValueError
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos, tente novamente!')

    def seleciona_entrega(self, dados_entregas):
        while True:
            layout = [
                [sg.Text('SELECIONE A ENTREGA', font=('Helvica, 25'))]
            ]
            for entrega in dados_entregas:
                tipo = entrega['tipo']
                destinatario = entrega['destinatario']
                data = convert_datetime(entrega['data_recebimento_condominio'])
                layout.append(
                    [sg.Radio(f'{tipo} ao morador(a) {destinatario} recebida pelo condomínio na data: {data}', 'entregas', key=str(entrega['id']))]
                )
            layout.append([sg.Button('Confirmar')])
            self.__window = sg.Window('Seleção de entregas').Layout(layout)

            button, values = self.open()
            for id_entrega in values:
                if values[id_entrega]:
                    self.close()
                    return int(id_entrega)
            if button in ('Confirmar', None):
                self.mostra_mensagem('Valores inválidos')
                self.close()

    def seleciona_tipo_entrega(self, dados_tipos):
        while True:
            layout = [
                [sg.Text('SELECIONE O TIPO DA ENTREGA', font=('Helvica, 25'))]
            ]
            for tipo in dados_tipos:
                nome = tipo['nome']
                layout.append(
                    [sg.Radio(f'{nome}', 'tipos_entregas', key=str(tipo['id']))]
                )
            layout.append([sg.Button('Confirmar')])
            self.__window = sg.Window('Seleção de tipos de entregas').Layout(layout)

            button, values = self.open()
            for id_tipo in values:
                if values[id_tipo]:
                    self.close()
                    return int(id_tipo)
            if button in ('Confirmar', None):
                self.mostra_mensagem('Valores inválidos')
                self.close()

    def mostra_entrega(self, dados_entregas):
        todas_entregas = ''
        for entrega in dados_entregas:
            todas_entregas += 'Tipo da entrega: ' + entrega['tipo'] + '\n'
            todas_entregas += 'Destinatário da entrega: ' + entrega['destinatario'] + '\n'
            todas_entregas += 'Data da entrega ao condomínio: ' + convert_datetime(entrega['data_recebimento_condominio']) + '\n'
            if entrega['data_recebimento_morador'] == None:
                todas_entregas += entrega['destinatario'] + ' ainda não coletou a sua entrega!\n'
            else:
                todas_entregas += 'Data da entrega ao morador: ' + convert_datetime(entrega['data_recebimento_morador']) + '\n'
            if entrega['tempo'] != None:
                todas_entregas += 'Morador demorou: ' + str(entrega['tempo']).split('.')[0] + ' (HORAS:MINUTOS:SEGUNDOS) para coletar a entrega \n'
            todas_entregas += 'ID da entrega: ' + str(entrega['id']) + '\n\n'         
        sg.Popup('LISTA DE TODAS AS ENTREGAS CADASTRADAS', todas_entregas)

    def mostra_tipo_entrega(self, dados_tipos):
        todos_tipos = ''
        for tipo in dados_tipos:
            todos_tipos += 'Nome do tipo de entrega: ' + tipo['nome'] + '\n'
            todos_tipos += 'O identificador do tipo é: ' + str(tipo['id']) + '\n\n'
        sg.Popup('LISTA DE TODAS OS TIPOS DE ENTREGAS CADASTRADOS', todos_tipos)

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
