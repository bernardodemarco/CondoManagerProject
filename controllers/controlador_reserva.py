from controllers.controlador import Controlador

class ControladorReserva(Controlador):
   
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        pass