from controllers.controlador import Controlador

from views.tela_reserva import TelaReserva

from models.reserva import Reserva

from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException


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

    def lista_reservas(self):
        try:
            if len(self.__reservas) == 0:
                raise ResourceNotFoundException('Reserva')

            self.__tela_reserva.mostra_mensagem(
                '<=======<<TODAS RESERVAS CADASTRADAS>>=======>'
            )
            for reserva in self.__reservas:
                self.__tela_reserva.mostra_reserva({
                    'reservavel': reserva.reservavel.nome,
                    'morador': reserva.morador.nome,
                    'horario': reserva.horario,
                    'id': reserva.id_reserva
                })
        except ResourceNotFoundException as err:
            self.__tela_reserva.mostra_mensagem(err)

    def incluir_reserva(self):
        try:    
            self.__tela_reserva.mostra_mensagem('<=======<<DADOS DAS RESERVAS>>=======>')

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            if morador == None:
                raise ResourceNotFoundException('Morador')

            reservavel = self.__controlador_condominio.seleciona_reservavel()
            if reservavel == None:
                raise ResourceNotFoundException('Reservavel')

            dados_reserva = self.__tela_reserva.pega_dados_reserva(acao='criacao')
            reserva = Reserva(dados_reserva['id'], dados_reserva['horario'], reservavel, morador)
            
            if reserva in self.__reservas:
                raise ResourceAlreadyExistsException('Reserva')
            self.__reservas.append(reserva)

        except ValueError as err:
            self.__tela_reserva.mostra_mensagem(err)
        except ResourceAlreadyExistsException as err:
            self.__tela_reserva.mostra_mensagem(err)
        except ResourceNotFoundException as err:
            self.__tela_reserva.mostra_mensagem(err)

    def alterar_reserva(self):
        try:
            if len(self.__reservas) == 0:
                raise Exception('Nenhuma reserva registrada!')

            self.__tela_reserva.mostra_mensagem(
                "<=======<<EDITAR RESERVA>>=======>")
            self.lista_reservas()
            id_reserva = self.__tela_reserva.seleciona_reserva()
            reserva = self.pega_reserva_por_id(id_reserva)
            if reserva == None:
                raise ResourceNotFoundException('Conta')
            self.__tela_reserva.mostra_reserva({
                'reservavel': reserva.reservavel.nome,
                'morador': reserva.morador.nome,
                'horario': reserva.horario,
                'id': reserva.id_reserva
            })
            
            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            if morador == None:
                raise ResourceNotFoundException('Morador')

            reservavel = self.__controlador_condominio.seleciona_reservavel()
            if reservavel == None:
                raise ResourceNotFoundException('Reservavel')

            dados_alterados_reserva = self.__tela_reserva.pega_dados_reserva(acao='alteracao', id_reserva=reserva.id_reserva)
            # reserva = Reserva(dados_alterados_reserva['id'], dados_alterados_reserva['horario'], reservavel, morador)
            reserva.id_reserva = dados_alterados_reserva['id']
            reserva.horario = dados_alterados_reserva['horario']
            reserva.reservavel = reservavel
            reserva.morador = morador
            self.__tela_reserva.mostra_mensagem('RESERVA ATUALIZADA COM SUCESSO!')

        except ValueError as err:
            self.__tela_reserva.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_reserva.mostra_mensagem(err)

    def excluir_reserva(self):
        try:
            if len(self.__reservas) == 0:
                raise Exception('Nenhuma reserva registrada!')

            self.__tela_reserva.mostra_mensagem(
                "<=======<<REMOVER RESERVA>>=======>")
            self.lista_reservas()
            id_reserva = self.__tela_reserva.seleciona_reserva()
            reserva = self.pega_reserva_por_id(id_reserva)
            if reserva == None:
                raise ResourceNotFoundException('Reserva')
            self.__reservas.remove(reserva)

        except ResourceNotFoundException as err:
            self.__tela_reserva.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_reserva.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_reserva.mostra_mensagem(err)
            
    def retornar(self):
        self.__controlador_condominio.abre_tela_2()

    def abre_tela(self):
        switcher = {
            0: self.retornar,
            1: self.incluir_reserva,
            2: self.alterar_reserva,
            3: self.excluir_reserva,
            4: self.lista_reservas
        }

        while True:
            switcher[self.__tela_reserva.mostra_opcoes()]()