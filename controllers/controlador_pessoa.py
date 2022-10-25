from controllers.controlador import Controlador


class ControladorPessoa(Controlador):
    
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_funcionario_condo(self):
        print("oi")

    def incluir_funcionario(self):
        pass

    def abre_tela(self):
        pass