from controllers.controlador import Controlador
from controllers.controlador_condominio import ControladorCondominio
from views.tela_sistema import TelaSistema


class ControladorSistema(Controlador):

    def __init__(self):
        super().__init__()
        self.__tela_sistema = TelaSistema()
        self.__controlador_condominio = ControladorCondominio(self)

    def inicializar(self):
        if not self.__controlador_condominio.condominios:
            self.abre_tela()
            self.__controlador_condominio.incluir_condo()
            self.ir_condo()
        else:
            self.ir_condo()

    def ir_condo(self):
        self.__controlador_condominio.abre_tela()

    def retornar(self):
        self.__tela_sistema.desligar()
        exit(0)

    def abre_tela(self):
        self.__tela_sistema.tutorial_cadastro  # RETIRADO PARA TESTES
