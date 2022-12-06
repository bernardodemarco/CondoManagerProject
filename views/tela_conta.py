import PySimpleGUI as sg

from utils.date_helpers import convert_date
from views.tela import Tela

from datetime import date 


class TelaConta(Tela):
    def __init__(self) -> None:
        super().__init__()
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        layout = [
            [sg.Text('-------- CONTAS ----------', font=("Helvica", 25))],
            [sg.Text('O que você gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir conta', "RD1", key='1')],
            [sg.Radio('Alterar conta', "RD1", key='2')],
            [sg.Radio('Excluir conta', "RD1", key='3')],
            [sg.Radio('Listar contas', "RD1", key='4')],
            [sg.Radio('Incluir um tipo de conta', "RD1", key='5')],
            [sg.Radio('Alterar um tipo de conta', "RD1", key='6')],
            [sg.Radio('Excluir um tipo de conta', "RD1", key='7')],
            [sg.Radio('Listar os tipos de contas', "RD1", key='8')],
            [sg.Radio('Gerar relatório das contas por mês', "RD1", key='9')],
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

    def pega_dados_contas(self, **kwargs):
        while True:
            layout = [
                [sg.Text('-------- CADASTRO DE CONTAS ----------', font=("Helvica", 25))],
                [sg.Text('Digite o valor da conta:', size=(30, 1)), sg.InputText('', key='valor')],
                [sg.Text('A conta é referente a qual data?:', size=(30, 1))],
                [sg.Text('Dia:', size=(30, 1)), sg.InputText('', key='dia')],
                [sg.Text('Mês:', size=(30, 1)), sg.InputText('', key='mes')],
                [sg.Text('Ano:', size=(30, 1)), sg.InputText('', key='ano')],
                [sg.Button('Cadastrar Conta')]
            ]
            if kwargs['acao'] == 'alteracao':
                id_conta = kwargs['id_conta']
            else:
                layout.insert(
                    6, [sg.Text('ID (número inteiro positivo) para a conta:', size=(30, 1)), sg.InputText('', key='id_conta')]
                )
            self.__window = sg.Window('Registro de contas').Layout(layout)
            button, values = self.open()
            try:
                valor = float(values['valor'])
                dia = int(values['dia'])
                mes = int(values['mes'])
                ano = int(values['ano'])
                if 'id_conta' in values:
                    id_conta = int(values['id_conta'])
                self.close()
                if (valor >= 0 and 1 <= mes <= 12 and
                        1 <= dia <= 31 and id_conta > 0):
                    data = date(ano, mes, dia)
                    return {"valor": valor, 'id': id_conta, 'data': data}
                else:
                    raise ValueError
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos, tente novamente!')

    def pega_dados_tipo(self, **kwargs):
        while True:
            layout = [
                [sg.Text('-------- CADASTRO TIPOS DE CONTAS ----------', font=("Helvica", 25))],
                [sg.Text('Digite o nome do tipo da conta:', size=(50, 1)), sg.InputText('', key='tipo')],
                [sg.Button('Cadastrar Tipo De Conta')]
            ]
            if kwargs['acao'] == 'alteracao':
                id_tipo = kwargs['id_tipo']
            else:
                layout.insert(
                    2, [sg.Text('Digite um identificador (número inteiro positivo) para o tipo de conta:', size=(50, 1)), sg.InputText('', key='id_tipo')]
                )
            self.__window = sg.Window('Cadastro de tipos de contas').Layout(layout)
            button, values = self.open()
            try:
                if 'id_tipo' in values:
                    id_tipo = int(values['id_tipo'])
                self.close()
                if (id_tipo > 0):
                    return {'nome_tipo': values['tipo'], 'id': id_tipo}
                raise ValueError
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos, tente novamente!')

    def pega_dados_relatorio(self):
        while True:
            layout = [
                [sg.Text('DADOS PARA GERAÇÃO DO RELATÓRIO DE CONTAS', font=("Helvica", 25))],
                [sg.Text('Digite o mês:', size=(10, 1)), sg.InputText('', key='mes')],
                [sg.Text('Digite o ano:', size=(10, 1)), sg.InputText('', key='ano')],
                [sg.Button('Enviar')]
            ]
            self.__window = sg.Window('Dados relatório de contas').Layout(layout)
            button, values = self.open()
            try:
                mes = int(values['mes'])
                ano = int(values['ano'])
                self.close()
                if not (1 <= mes <= 12):
                    raise ValueError
                return {'mes': mes, 'ano': ano}
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos, tente novamente!')

    def seleciona_conta(self, dados_contas):
        layout = [
            [sg.Text('SELECIONE A CONTA', font=('Helvica, 25'))]
        ]
        for conta in dados_contas:
            valor = conta['valor']
            tipo = conta['tipo']
            data = conta['data']
            layout.append(
                [sg.Radio(f'{tipo} de R${valor} da data: {data}', 'contas', key=str(conta['id']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.__window = sg.Window('Seleção de contas').Layout(layout)

        button, values = self.open()
        for id_conta in values:
            if values[id_conta]:
                self.close()
                return int(id_conta)

    def seleciona_tipo_conta(self, dados_tipos):
        layout = [
            [sg.Text('SELECIONE O TIPO DA CONTA', font=('Helvica, 25'))]
        ]
        for tipo in dados_tipos:
            nome = tipo['nome']
            layout.append(
                [sg.Radio(f'{nome}', 'tipos_contas', key=str(tipo['id']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.__window = sg.Window('Seleção de tipos de contas').Layout(layout)

        button, values = self.open()
        for id_tipo in values:
            if values[id_tipo]:
                self.close()
                return int(id_tipo)

    def mostra_conta(self, dados_contas):
        todas_contas = ''
        for conta in dados_contas:
            todas_contas += 'Valor da conta = R$' + str(conta['valor']) + '\n'
            todas_contas += 'Tipo da conta: ' + conta['tipo'] + '\n'
            todas_contas += 'Data da conta: ' + convert_date(conta['data']) + '\n'
            todas_contas += 'O identificador da conta é = ' + str(conta['id']) + '\n\n'
        sg.Popup('LISTA DE TODAS AS CONTAS CADASTRADAS', todas_contas)

    def mostra_tipo_conta(self, dados_tipos):
        todos_tipos = ''
        for tipo in dados_tipos:
            todos_tipos += 'Nome do tipo de conta: ' + tipo['nome'] + '\n'
            todos_tipos += 'O identificador do tipo é: ' + str(tipo['id']) + '\n\n'
        sg.Popup('LISTA DE TODAS OS TIPOS DE CONTAS CADASTRADOS', todos_tipos)

    def mostra_relatorio(self, dados_relatorio):
        mes = dados_relatorio['mes']
        ano = dados_relatorio['ano']
        del dados_relatorio['mes']
        del dados_relatorio['ano']

        todos_dados = f'RELATÓRIO DAS CONTAS ({mes}/{ano}) \n'
        for key, val in dados_relatorio.items():
            todos_dados += f'{key} -> R${val:.2f} \n'
        sg.Popup(todos_dados)

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
