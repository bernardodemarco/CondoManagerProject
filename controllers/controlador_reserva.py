from controllers.controlador import Controlador

class ControladorReserva(Controlador):
   
    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio

    def retornar(self):
        self.__controlador_condominio.abre_tela()

    def abre_tela(self):
        pass