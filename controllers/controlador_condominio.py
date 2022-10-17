from controlador import Controlador
from controlador_sistema import ControladorSistema
from models.condominio import Condominio


class ControladorCondominio(Controlador):
    def __init__(self, condominio: Condominio,
                 controlador_sistema: ControladorSistema):
        super().__init__()
        self.__condominio = condominio
        self.__controlador_sistema = controlador_sistema
