from views.tela import Tela


class TelaReserva(Tela):
    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<RESERVAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir reserva")
        print("        2 - Alterar reserva")
        print("        3 - Excluir reserva")
        print("        4 - Listar reservas")
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(4)

    def pega_dados_reserva(self, **kwargs):
        horario = input('Digite o horario desejado para a reserva: ')
        if kwargs['acao'] == 'alteracao':
            id_reserva = kwargs['id_reserva']
        else:
            id_reserva = int(
                input('Digite um identificador (número inteiro positivo) para a reserva: '))

        if (isinstance(id_reserva, int) and id_reserva > 0):
            return {'id': id_reserva, 'horario': horario}
        else:
            raise ValueError('Valores inválidos, tente novamente!')

    def seleciona_reserva(self):
        try:
            id_reserva = int(
                input(('SELECIONE A RESERVA (digite o identificador): ')))
            if isinstance(id_reserva, int) and id_reserva > 0:
                return id_reserva
            raise ValueError
        except ValueError:
            raise ValueError('Valor do id inválido')        

    def mostra_reserva(self, dados):
        print('NOME DO RESERVAVEL:', dados['reservavel'])
        print('NOME DO MORADOR:', dados['morador'])
        print('HORÁRIO DA RESERVA:', dados['horario'])
        print('ID DA RESERVA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")
