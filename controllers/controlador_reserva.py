from controllers.controlador import Controlador

from views.tela_reserva import TelaReserva

from models.reserva import Reserva

from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.date_helpers import convert_date


class ControladorReserva(Controlador):
    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_reserva = TelaReserva()
        self.__reservas = []

    def pega_reserva_por_id(self, id_reserva):
        for reserva in self.__reservas:
            if reserva.id_reserva == id_reserva:
                return reserva
        return None

    def pega_dados_reservas(self):
        dados_reservas = []
        for reserva in self.__reservas:
            dados_reservas.append({
                'reservavel': reserva.reservavel.nome,
                'morador': reserva.morador.nome,
                'horario': reserva.horario,
                'id': reserva.id_reserva
            })
        return dados_reservas

    def checar_disponibilidade_horario(self, horario_inicial_reserva, horario_final_reserva, horarios) -> bool:
        ''' Verifica se determinado horário está disponível '''
        horario_disponivel = True
        if convert_date(horario_inicial_reserva.date()) in horarios:
            for (horario_i, horario_f) in horarios[convert_date(horario_inicial_reserva.date())]:
                if not (horario_inicial_reserva >= horario_f or (horario_inicial_reserva < horario_i and horario_final_reserva <= horario_i)): 
                    horario_disponivel = False
                    break
            else:
                horario_disponivel = True
        else:
            horario_disponivel = True
        return horario_disponivel

    def marcar_horario(self, horario_inicial_reserva, horario_final_reserva, horarios):
        ''' Registra o horário da reserva '''
        if convert_date(horario_inicial_reserva.date()) in horarios:
            horarios[convert_date(horario_inicial_reserva.date())].append((horario_inicial_reserva, horario_final_reserva))
        else:
            horarios[convert_date(horario_inicial_reserva.date())] = [(horario_inicial_reserva, horario_final_reserva)]   

    def lista_reservas(self):
        try:
            if len(self.__reservas) == 0:
                raise ResourceNotFoundException('Reserva')
            dados_reservas = self.pega_dados_reservas()
            self.__tela_reserva.mostra_reserva(dados_reservas)
        except ResourceNotFoundException as err:
            self.__tela_reserva.mostra_mensagem(err)

    def incluir_reserva(self):
        try:    
            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            if morador == None:
                raise ResourceNotFoundException('Morador')

            if len(self.__controlador_condominio.reservaveis) == 0:
                raise ResourceNotFoundException('Reservavel')

            reservavel = self.__controlador_condominio.seleciona_reservavel()
            if reservavel == None:
                raise ResourceNotFoundException('Reservavel')

            dados_reserva = self.__tela_reserva.pega_dados_reserva(acao='criacao')
            horario_inicial, horario_final = dados_reserva['horario']

            if not self.checar_disponibilidade_horario(horario_inicial, horario_final, reservavel.horarios):
                raise ValueError('Horário indisponível')
            self.marcar_horario(horario_inicial, horario_final, reservavel.horarios)
                    
            reserva = Reserva(dados_reserva['id'], (horario_inicial, horario_final), reservavel, morador)
            if reserva in self.__reservas:
                raise ResourceAlreadyExistsException('Reserva')
            self.__reservas.append(reserva)
        except (ResourceAlreadyExistsException, ResourceNotFoundException, ValueError) as err:
            self.__tela_reserva.mostra_mensagem(err)
        except TypeError:
            self.__tela_reserva.mostra_mensagem('Erro, tente novamente!')

    def alterar_reserva(self):
        try:
            if len(self.__reservas) == 0:
                raise Exception('Nenhuma reserva registrada!')

            self.lista_reservas()
            dados_reservas = self.pega_dados_reservas()
            id_reserva = self.__tela_reserva.seleciona_reserva(dados_reservas)
            reserva = self.pega_reserva_por_id(id_reserva)
            if reserva == None:
                raise ResourceNotFoundException('Reserva')
            self.__tela_reserva.mostra_reserva([{
                'reservavel': reserva.reservavel.nome,
                'morador': reserva.morador.nome,
                'horario': reserva.horario,
                'id': reserva.id_reserva
            }])
            
            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            if morador == None:
                raise ResourceNotFoundException('Morador')

            if len(self.__controlador_condominio.reservaveis) == 0:
                raise ResourceNotFoundException('Reservavel')
                
            reserva.reservavel.horarios[convert_date(reserva.horario[0].date())].remove(reserva.horario)
            reservavel = self.__controlador_condominio.seleciona_reservavel()
            if reservavel == None:
                reserva.reservavel.horarios[convert_date(reserva.horario[0].date())].append(reserva.horario)
                raise ResourceNotFoundException('Reservavel')

            dados_alterados_reserva = self.__tela_reserva.pega_dados_reserva(acao='alteracao', id_reserva=reserva.id_reserva)
            horario_inicial, horario_final = dados_alterados_reserva['horario']
            if not self.checar_disponibilidade_horario(horario_inicial, horario_final, reservavel.horarios):
                reserva.reservavel.horarios[convert_date(reserva.horario[0].date())].append(reserva.horario)            
                raise ValueError('Horário indisponível')
            self.marcar_horario(horario_inicial, horario_final, reservavel.horarios)
            
            reserva.id_reserva = dados_alterados_reserva['id']
            reserva.horario = (horario_inicial, horario_final)
            reserva.reservavel = reservavel
            reserva.morador = morador
            self.__tela_reserva.mostra_mensagem('RESERVA ATUALIZADA COM SUCESSO!')
        except (ResourceNotFoundException, ValueError, Exception) as err:
            self.__tela_reserva.mostra_mensagem(err)

    def excluir_reserva(self):
        try:
            if len(self.__reservas) == 0:
                raise Exception('Nenhuma reserva registrada!')

            self.lista_reservas()
            dados_reservas = self.pega_dados_reservas()
            id_reserva = self.__tela_reserva.seleciona_reserva(dados_reservas)
            reserva = self.pega_reserva_por_id(id_reserva)
            if reserva == None:
                raise ResourceNotFoundException('Reserva')
            
            horario_reserva = reserva.horario
            reserva.reservavel.horarios[convert_date(horario_reserva[0].date())].remove(horario_reserva)
            self.__reservas.remove(reserva)
            self.__tela_reserva.mostra_mensagem('RESERVA EXCLUIDA COM SUCESSO!')
        except ValueError as err:
            self.__tela_reserva.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_reserva.mostra_mensagem(err)

    def gerar_relatorio_reservas(self):
        ''' Geração de relatório informando quantas vezes um dado morador realizou reservas '''
        try:
            if len(self.__reservas) == 0:
                raise ResourceNotFoundException('Reserva')   

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            if morador == None:
                raise ResourceNotFoundException('Morador')

            total_reservas = 0
            for reserva in self.__reservas:
                if reserva.morador.cpf == morador.cpf:
                    total_reservas += 1
            self.__tela_reserva.mostra_relatorio(total_reservas, morador.nome)
        except ResourceNotFoundException as err:
            self.__tela_reserva.mostra_mensagem(err)
        
    def retornar(self):
        self.__controlador_condominio.abre_tela_2()

    def abre_tela(self):
        switcher = {
            0: self.retornar,
            1: self.incluir_reserva,
            2: self.alterar_reserva,
            3: self.excluir_reserva,
            4: self.lista_reservas,
            5: self.gerar_relatorio_reservas
        }

        while True:
            switcher[self.__tela_reserva.mostra_opcoes()]()
