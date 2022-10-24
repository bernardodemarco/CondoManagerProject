from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from controllers.controlador import Controlador
from controllers.controlador_conta import ControladorConta
from controllers.controlador_entrega import ControladorEntrega
from controllers.controlador_pessoa import ControladorPessoa
from controllers.controlador_reserva import ControladorReserva
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio
# from views.tela_apartamento import TelaApartamento


class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__condominios = []
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__controlador_reserva = ControladorReserva(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_condominio = TelaCondominio()
        # self.__tela_apartamento = TelaApartamento()

    @property
    def condominios(self) -> list:
        return self.__condominios

    def ir_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def ir_reserva(self):
        self.__controlador_reserva.abre_tela()

    def ir_entrega(self):
        self.__controlador_entrega.abre_tela()

    def ir_conta(self):
        self.__controlador_conta.abre_tela()

    def pega_condominio_por_num(self, num: int):
        for condo in self.__condominios:
            if(condo.num == num):
                return condo
        return None

    def incluir_condo(self):
        dados_condo = self.__tela_condominio.pega_dados_condo(acao="criacao")    
        funcionario = self.__controlador_pessoa.incluir_funcionario()

        condo = Condominio(dados_condo["nome"],
                        dados_condo["numero"],
                        dados_condo["endereco"],
                        funcionario)

    def alterar_condo(self):
        pass

    def listar_condo(self):
        for condo in self.__condominios:
            self.__tela_condominio.mostra_condo({
                "nome": condo.nome,
                "num": condo.numero,
                "endereco": condo.endereco
            })

    def excluir_condo(self):
        pass

    def ir_apartamento(self):
        self.abre_tela_apartamento()

    def abre_tela(self):
        switcher = {
            1: self.incluir_condo,
            2: self.alterar_condo,
            3: self.listar_condo,
            4: self.excluir_condo,
            5: self.ir_apartamento,
            0: self.retornar
        }
        
        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes())]()

    def abre_tela_apartamento(self):
        opcoes = {1: self.incluir_apartamento, 2: self.alterar_apartamento,
                  3: self.listar_apartamento, 4: self.excluir_apartamento,
                  0: self.retornar}

        while True:
            opcoes[int(self.__tela_apartamento.mostra_opcoes())]()

    def retornar(self):
        self.__controlador_sistema.retornar()
        