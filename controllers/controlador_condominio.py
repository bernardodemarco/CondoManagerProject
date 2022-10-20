from controllers.controlador import Controlador
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio


class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__condominios = []
        self.__tela_condominio = TelaCondominio()

    @property
    def condominios(self) -> list:
        return self.__condominios

    def pega_condominio_por_num(self, num: int):
        for condo in self.__condominios:
            if(condo.num == num):
                return condo
        return None

    def incluir_condo(self):
        dados_condo = self.__tela_condominio.pega_dados_condo()
        condo = Condominio(dados_condo["nome"],
                           dados_condo["numero"],
                           dados_condo["endereco"],
                           dados_condo["funcionario"])
        self.__condominios.append(condo)


    def abre_tela(self):
        opcoes = {1: self.incluir_condo, 2: self.alterar_condo,
                  3: self.lista_condo, 4: self.excluir_condo,
                  0: self.retornar}
        
        while True:
            opcoes[self.__tela_condominio.mostra_opcoes()]()

    def forca_incluir_condo(self):
        self.__tela_condominio.forca_incluir_condo()
        self.incluir_condo()
