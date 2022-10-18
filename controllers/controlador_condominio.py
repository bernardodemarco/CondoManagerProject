from controlador import Controlador
from controlador_sistema import ControladorSistema
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio


class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema: ControladorSistema):
        super().__init__(controlador_sistema)
        self.__condominios = []
        self.__tela_condominio = TelaCondominio()

    def pega_condominio_por_num(self, num: int):
        for condo in self.__condominios:
            if(condo.num == num):
                return condo
        return None

    def incluir_condo(self):
