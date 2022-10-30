from controllers.controlador import Controlador
from controllers.controlador_condominio import ControladorCondominio
from views.tela_sistema import TelaSistema


class ControladorSistema(Controlador):

    def __init__(self):
        super().__init__()
        self.__tela_sistema = TelaSistema()
        self.__controlador_condominio = ControladorCondominio(self)

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    @property
    def controlador_condominio(self):
        return self.__controlador_condominio

    def inicializar(self):
        if not self.__controlador_condominio.condominio:
            self.abre_tela()
            self.__controlador_condominio.cadastro_inicial()
            self.ir_condo()
        else:
            self.ir_condo()

    def ir_condo(self):
        self.controlador_condominio.abre_tela()

    def resetar(self):
        if self.tela_sistema.aviso_resetar():
            exit(0)
        else:
            return None

    def retornar(self):
        self.tela_sistema.aviso_desligar()
        exit(0)

    def abre_tela(self):
        self.tela_sistema.tutorial_cadastro()  # RETIRADO PARA TESTES
