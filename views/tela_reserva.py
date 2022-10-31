from views.tela import Tela

from datetime import timedelta, datetime

from utils.date_helpers import convert_datetime, validate_horario


class TelaReserva(Tela):
    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("")
        print("<=======<<RESERVAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir reserva")
        print("        2 - Alterar reserva")
        print("        3 - Excluir reserva")
        print("        4 - Listar reservas")
        print("        5 - Relatório reservas")
        print("        0 - Retornar")
        print("<=======<<===========>>=======>")
        return self.checa_opcao(5)

    def pega_dados_reserva(self, **kwargs):
        print("")
        print('<=======<<REGISTRO DE RESERVAS>>=======>')
        while True:
            try:
                dia = int(input('Digite o dia (0 a 31): '))
                mes = int(input('Digite o mês (1 a 12): '))
                ano = int(input('Digite o ano: '))
                raw_horario = input('Digite o horário desejado (horas:minutos): ')
                horas, minutos = validate_horario(raw_horario)
                quantidade_horas = int(input('Por quantas horas você deseja reservar? '))
                if kwargs['acao'] == 'alteracao':
                    id_reserva = kwargs['id_reserva']
                else:
                    id_reserva = int(
                        input('Digite um identificador (número inteiro positivo) para a reserva: '))

                horario_inicial = datetime(ano, mes, dia, horas, minutos)
                horario_final = horario_inicial + timedelta(hours=quantidade_horas)
            
                if (isinstance(id_reserva, int) and id_reserva > 0
                    and  (22 > horario_final.hour >= 7 or
                    horario_final.hour == 22 and horario_final.minute == 0)):
                    return {'id': id_reserva, 'horario': (horario_inicial, horario_final), 'quantidade_horas': quantidade_horas}
                else:
                    raise ValueError
            except ValueError:
                print("")
                print('Valores inválidos, tente novamente!')
                print("")

    def seleciona_reserva(self):
        while True:
            try:
                id_reserva = int(
                    input(('SELECIONE A RESERVA (digite o identificador): ')))
                if isinstance(id_reserva, int) and id_reserva > 0:
                    return id_reserva
                raise ValueError
            except ValueError:
                print("")
                print('Valor do id inválido!')       
                print("")

    def mostra_reserva(self, dados):
        print('NOME DO RESERVAVEL:', dados['reservavel'])
        print('NOME DO MORADOR:', dados['morador'])
        (horario_inicial, horario_final) = dados['horario']       
        print('HORÁRIO DA RESERVA:')
        print(f'SUA RESERVA VAI DAS {convert_datetime(horario_inicial)} até as {convert_datetime(horario_final)}!')
        print('ID DA RESERVA:', dados['id'])
        print("<=======<<===========>>=======>")

    def mostra_relatorio(self, total_reservas: int, morador):
        print("")
        print(f'NOS REGISTROS DO CONDOMÍNIO CONSTAM QUE O(A) MORADOR(A) {morador} REALIZOU NO TOTAL {total_reservas} RESERVAS!')