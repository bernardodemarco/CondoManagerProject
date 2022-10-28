from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from controllers.controlador import Controlador
from controllers.controlador_conta import ControladorConta
from controllers.controlador_entrega import ControladorEntrega
from controllers.controlador_pessoa import ControladorPessoa
from controllers.controlador_reserva import ControladorReserva
from models.reservavel import Reservavel
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio



class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__condominio = None
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__controlador_reserva = ControladorReserva(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_condominio = TelaCondominio(self)

    @property
    def condominio(self) -> list:
        return self.__condominio

    @condominio.setter
    def condominio(self, condo):
        self.__condominio = condo

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def controlador_pessoa(self) -> ControladorPessoa:
        return self.__controlador_pessoa

    def incluir_condo(self):
        dados_condo = self.__tela_condominio.pega_dados_condo(acao="criacao")
        self.__tela_condominio.mostra_mensagem("É necessário o cadastro de um funcionário para o condomínio.")
        funcionario = self.__controlador_pessoa.incluir_funcionario()

        condo = Condominio(dados_condo["nome"],
                           dados_condo["numero"],
                           dados_condo["endereco"],
                           dados_condo["apartamento"],
                           funcionario)

        self.condominio = condo
        self.__tela_condominio.mostra_mensagem("Agora, é necessário o cadastro de um morador.")
        self.__controlador_pessoa.incluir_morador(self.condominio.apartamentos)


    def alterar_condo(self):
        dados_alterados = self.__tela_condominio.pega_dados_condo(
            acao="alteracao", numero=self.condominio.numero)
        self.condominio.nome = dados_alterados["nome"]
        self.condominio.num = dados_alterados["numero"]
        self.condominio.endereco = dados_alterados["endereco"]

    def listar_condo(self):
        self.__tela_condominio.mostra_condo({
            "nome": self.condominio.nome,
            "numero": self.condominio.numero,
            "endereco": self.condominio.endereco,
            "apartamentos": self.condominio.apartamentos
        })

    def ocupar_apartamento(self, apartamento):
        self.condominio.apartamentos.remove(apartamento)

    def excluir_condo(self):
        pass

    def ir_morador(self):
        self.__controlador_pessoa.abre_tela()

    def ir_funcionario(self):
        self.__controlador_pessoa.abre_tela_funcionario()
    
    def ir_reserva(self):
        self.__controlador_reserva.abre_tela()

    def ir_entrega(self):
        self.__controlador_entrega.abre_tela()

    def ir_conta(self):
        self.__controlador_conta.abre_tela()

    def ir_reservavel(self):
        self.abre_tela_reservavel()

    def ir_apartamento(self):
        self.abre_tela_apartamento()

    def outras_opcoes(self):
        self.abre_tela_2()

    def abre_tela(self):
        switcher = {
            1: self.incluir_condo, ## SUMIR
            2: self.alterar_condo,
            3: self.excluir_condo, ## RESET
            4: self.listar_condo, ## MOSTRAR DADOS
            5: self.outras_opcoes,
            0: self.retornar, ## DESLIGAR
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes())]()

    def abre_tela_apartamento(self):
        switcher = {
            1: self.incluir_apartamento,
            2: self.alterar_apartamento,
            3: self.listar_apartamento,
            4: self.excluir_apartamento,
            0: self.abre_tela_2
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes_apartamento())]()

    def incluir_apartamento(self):
        pass

    def alterar_apartamento(self):
        pass

    def listar_apartamento(self):
        pass

    def excluir_apartamento(self):
        pass

    def abre_tela_reservavel(self):
        switcher = {
            1: self.incluir_reservavel,
            2: self.alterar_reservavel,
            3: self.excluir_reservavel,
            4: self.listar_reservaveis,
            0: self.abre_tela_2
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes_reservavel())]()

    def pega_reservavel_por_id(self, id: str):
        for reservavel in self.condominio.reservaveis:
            if (reservavel.id_reservavel == id):
                return reservavel
        return None
    
    def listar_reservaveis(self):
        for reservavel in self.condominio.reservaveis:
            self.__tela_condominio.mostra_reservavel({
                'nome': reservavel.nome,
                'id': reservavel.id_reservavel,
            })

    def seleciona_reservavel(self):
        self.listar_reservaveis()
        return self.pega_reservavel_por_id(self.__tela_condominio.seleciona_reservavel())

    def incluir_reservavel(self):
        dados_reservavel = self.__tela_condominio.pega_dados_reservavel(acao="criacao")

        reservavel = Reservavel(dados_reservavel["nome"],
                           dados_reservavel["id_reservavel"])

        self.__condominio.reservaveis.append(reservavel)


    def alterar_reservavel(self):
        pass


    def excluir_reservavel(self):
        pass

    def abre_tela_2(self):
        switcher = {
            1: self.ir_apartamento,
            2: self.ir_morador,
            3: self.ir_funcionario,
            4: self.ir_conta,
            5: self.ir_reservavel,
            6: self.ir_reserva,
            7: self.ir_entrega,
            0: self.abre_tela
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes_2())]()

    def ir_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def ir_reserva(self):
        self.__controlador_reserva.abre_tela()

    def ir_entrega(self):
        self.__controlador_entrega.abre_tela()

    def ir_conta(self):
        self.__controlador_conta.abre_tela()

    def retornar(self):
        self.__controlador_sistema.retornar()
