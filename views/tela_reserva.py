import PySimpleGUI as sg

from views.tela import Tela

from datetime import timedelta, datetime

from utils.date_helpers import convert_datetime, validate_horario
from utils.InvalidTimeException import InvalidTimeException


class TelaReserva(Tela):
    def __init__(self):
        super().__init__()
        self.init_opcoes()

    def init_opcoes(self):
        layout = [
            [sg.Text('-------- RESERVAS ----------', font=("Helvica", 25))],
            [sg.Text('O que você gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir reserva', "RD1", key='1')],
            [sg.Radio('Alterar reserva', "RD1", key='2')],
            [sg.Radio('Excluir reserva', "RD1", key='3')],
            [sg.Radio('Listar reservas', "RD1", key='4')],
            [sg.Radio('Gerar relatório de reservas', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.window = sg.Window('Sistema de reservas').Layout(layout)

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

    def pega_dados_reserva(self, **kwargs):
        while True:
            layout = [
                [sg.Text('-------- REGISTRO DE RESERVAS ----------', font=("Helvica", 25))],
                [sg.Text('Dia:', size=(50, 1)), sg.InputText('', key='dia')],
                [sg.Text('Mês:', size=(50, 1)), sg.InputText('', key='mes')],
                [sg.Text('Ano:', size=(50, 1)), sg.InputText('', key='ano')],
                [sg.Text('Horário (horas:minutos):', size=(50, 1)), sg.InputText('', key='raw_horario')],
                [sg.Text('Por quantas horas você deseja reservar?', size=(50, 1)), sg.InputText('', key='quantidade_horas')],
                [sg.Button('Registrar Reserva')]
            ]
            if kwargs['acao'] == 'alteracao':
                id_reserva = kwargs['id_reserva']
            else:
                layout.insert(
                    6, [sg.Text('Digite um identificador (número inteiro positivo) para a reserva:', size=(50, 1)), sg.InputText('', key='id_reserva')]
                )
            self.window = sg.Window('Registro de reservas').Layout(layout)

            button, values = self.open()
            try:
                dia = int(values['dia'])
                mes = int(values['mes'])
                ano = int(values['ano'])
                if 'id_reserva' in values:
                    id_reserva = int(values['id_reserva'])
                quantidade_horas = int(values['quantidade_horas'])
                horas, minutos = validate_horario(values['raw_horario'].strip())
                horario_inicial = datetime(ano, mes, dia, horas, minutos)
                horario_final = horario_inicial + timedelta(hours=quantidade_horas)
                self.close()
                if (isinstance(id_reserva, int) and id_reserva > 0
                        and  (22 > horario_final.hour >= 7 or
                        horario_final.hour == 22 and horario_final.minute == 0)):
                    return {'id': id_reserva, 'horario': (horario_inicial, horario_final)}
                else:
                    raise ValueError
            except ValueError:
                self.close()
                self.mostra_mensagem('Valores inválidos, tente novamente!')
            except InvalidTimeException as err:
                self.close()
                self.mostra_mensagem(err)

    def seleciona_reserva(self, dados_reservas):
        layout = [
            [sg.Text('SELECIONE A RESERVA', font=('Helvica, 25'))]
        ]
        for reserva in dados_reservas:
            horario_inicial, horario_final = reserva['horario']
            nome_reservavel = reserva['reservavel']
            nome_morador = reserva['morador']
            layout.append(
                [sg.Radio(f'Reserva do {nome_reservavel} feita pelo {nome_morador} das {horario_inicial} até às {horario_final}', 'reservas', key=str(reserva['id']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.window = sg.Window('Seleção de reserva').Layout(layout)

        button, values = self.open()
        for id_reserva in values:
            if values[id_reserva]:
                self.close()
                return int(id_reserva)

    def mostra_reserva(self, dados_reservas):
        todas_reservas = ''
        for reserva in dados_reservas:
            (horario_inicial, horario_final) = reserva['horario']
            todas_reservas += 'Nome do reservável: ' + reserva['reservavel'] + '\n'
            todas_reservas += 'Nome do morador: ' + reserva['morador'] + '\n'
            todas_reservas += f'A reserva vai das {convert_datetime(horario_inicial)} até as {convert_datetime(horario_final)}!\n'
            todas_reservas += 'O identificador da reserva é: ' + str(reserva['id']) + '\n\n'
        sg.Popup('LISTA DE TODAS AS RESERVAS REGISTRADAS', todas_reservas)

    def mostra_relatorio(self, total_reservas: int, morador: str):
        sg.Popup(f'NOS REGISTROS DO CONDOMÍNIO CONSTAM QUE O(A) MORADOR(A) {morador} REALIZOU NO TOTAL {total_reservas} RESERVAS!')

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)
