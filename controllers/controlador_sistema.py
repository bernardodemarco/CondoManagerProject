from views.tela_sistema import TelaSistema
from controlador import Controlador
from controlador_condominio import ControladorCondominio
from controlador_conta import ControladorConta
from controlador_entrega import ControladorEntrega
from controlador_pessoa import ControladorPessoa
from controlador_reserva import ControladorReserva


class ControladorSistema(Controlador):

    def __init___(self):
        self.__controlador_condominio = ControladorCondominio(self)
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_reserva = ControladorReserva(self)
        self.__tela_sistema = TelaSistema()
 
    def inicializar():
        self.abre_tela_sistema()

    def ir_condominio():
        self.__controlador_condominio.abre_tela()
    
    def ir_pessoa():
        self.__controlador_pessoa.abre_tela()

    def ir_reserva():
        self.__controlador_reserva.abre_tela()

    def ir_entrega():
        self.__controlador_entrega.abre_tela()

    def ir_conta():
        self.__controlador_conta.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.ir_condominio, 2: self.ir_pessoa,
                  3: self.ir_reserva, 4: self.ir_entrega, 5: self.ir_conta}

        while True:
            opcao_selecionada = self.__tela_sistema.mostra_opcoes()
            funcao = opcoes[opcao_selecionada]
            funcao()

    #No sistema, serve para encerrar o próprio
    def retornar():
        exit(0) 
