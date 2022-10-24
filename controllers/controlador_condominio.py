# from views.tela_apartamento import TelaApartamento
from controllers.controlador import Controlador
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio


class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__condominios = []
        self.__tela_condominio = TelaCondominio()
        # self.__tela_apartamento = TelaApartamento()

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

    def alterar_condo(self):
        pass

    def listar_condo(self):
        pass

    def excluir_condo(self):
        pass

    def ir_apartamento(self):
        self.abre_tela_apartamento()

    def abre_tela(self):
        opcoes = {1: self.incluir_condo, 2: self.alterar_condo,
                  3: self.listar_condo, 4: self.excluir_condo,
                  5: self.ir_apartamento, 0: self.retornar}
        
        while True:
            opcoes[int(self.__tela_condominio.mostra_opcoes())]()

    def abre_tela_apartamento(self):
        opcoes = {1: self.incluir_apartamento, 2: self.alterar_apartamento,
                  3: self.listar_apartamento, 4: self.excluir_apartamento,
                  0: self.retornar}

        while True:
            opcoes[int(self.__tela_apartamento.mostra_opcoes())]()


    def forca_incluir_condo(self):
        self.__tela_condominio.forca_incluir_condo()
        self.incluir_condo()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
        