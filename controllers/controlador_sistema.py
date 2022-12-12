from controllers.controlador import Controlador
from controllers.controlador_condominio import ControladorCondominio
from controllers.controlador_pessoa import ControladorPessoa
from views.tela_sistema import TelaSistema


class ControladorSistema(Controlador):
    def __init__(self):
        super().__init__()
        self.__tela_sistema = TelaSistema()
        self.__controlador_condominio = ControladorCondominio(self)
        self.__controlador_pessoa = ControladorPessoa(self)

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    @property
    def controlador_condominio(self):
        return self.__controlador_condominio

    def inicializar(self):
        if len(self.controlador_condominio.condominio_dao.get_all()) == 0:
            self.abre_tela()
            self.__controlador_condominio.cadastro_inicial()
            self.ir_condo()
        else:
            self.ir_condo()

    def ir_condo(self):
        self.controlador_condominio.abre_tela()

    def resetar(self):
        if self.tela_sistema.aviso_resetar():
            path = os.path.join(os.path.dirname(__file__), f'..\\pickle_files')
            for file in os.listdir(path):
                path_to_file = os.path.join(path, file)
                os.remove(path_to_file)
            exit(0)
        else:
            return None

    def retornar(self):
        self.tela_sistema.aviso_desligar()
        exit(0)

    def abre_tela(self):
        self.tela_sistema.tutorial_cadastro()  # RETIRADO PARA TESTES
