from controllers.controlador import Controlador
from controllers.controlador_condominio import ControladorCondominio
from controllers.controlador_conta import ControladorConta
from controllers.controlador_entrega import ControladorEntrega
from controllers.controlador_pessoa import ControladorPessoa
from controllers.controlador_reserva import ControladorReserva
from views.tela_sistema import TelaSistema


class ControladorSistema(Controlador):

    def __init__(self):
        super().__init__()
        self.__controlador_condominio = ControladorCondominio(self)
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_reserva = ControladorReserva(self)
        self.__tela_sistema = TelaSistema()

    '''
    AINDA PRECISO TERMINAR A CHECAGEM DA PRIMEIRA VEZ ABERTO
    '''

    @property
    def controlador_condominio(self) -> ControladorCondominio:
        return self.__controlador_condominio
    
    def inicializar(self):
        self.abre_tela()

    def ir_condo(self):
        self.__controlador_condominio.abre_tela()
    
    def ir_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def ir_reserva(self):
        self.__controlador_reserva.abre_tela()

    def ir_entrega(self):
        self.__controlador_entrega.abre_tela()

    def ir_conta(self):
        self.__controlador_conta.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.ir_condo, 2: self.ir_pessoa,
                3: self.ir_reserva, 4: self.ir_entrega, 5: self.ir_conta,
                0: self.retornar}

        while True:
            opcoes[self.__tela_sistema.mostra_opcoes()]()

    def retornar(self):
        exit(0)

