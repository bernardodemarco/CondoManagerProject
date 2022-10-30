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

#   GETTERS E SETTERS   #

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

#   CONDOMÍNIO  #

    def abre_tela(self):
        switcher = {
            1: self.alterar_condo,
            2: self.mostra_dados_condo,
            3: self.outras_opcoes,
            4: self.resetar,
            0: self.retornar
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes())]()
       
    def cadastro_inicial(self):
        dados_condo = self.__tela_condominio.pega_dados_condo(acao='criacao')

        condo = Condominio(dados_condo["nome"],
                           dados_condo["cidade"],
                           dados_condo["rua"],
                           dados_condo["numero"],
                           dados_condo["apartamento"])

        self.condominio = condo

        self.__tela_condominio.mostra_mensagem("É necessário o cadastro de um funcionário para o condomínio.")
        self.__controlador_pessoa.incluir_funcionario()
        self.__tela_condominio.mostra_mensagem("Agora, é necessário o cadastro de um morador.")
        self.__controlador_pessoa.incluir_morador(self.condominio.apartamentos)

    def alterar_condo(self):
        dados_alterados = self.__tela_condominio.pega_dados_condo(acao='alteracao')
        self.condominio.nome = dados_alterados["nome"]
        self.condominio.cidade = dados_alterados["cidade"]
        self.condominio.rua = dados_alterados["rua"]
        self.condominio.numero = dados_alterados["numero"]
        self.condominio.apartamentos = dados_alterados["apartamento"]

    def mostra_dados_condo(self):
        apartamentos_str = [str(i) for i in self.condominio.apartamentos]
        self.__tela_condominio.mostra_condo({
            "nome": self.condominio.nome,
            "cidade": self.condominio.cidade,
            "rua": self.condominio.rua,
            "numero": self.condominio.numero,
            "apartamentos": apartamentos_str
        })

    def resetar(self):
        self.controlador_sistema.resetar()

    def retorna_apartamento(self):
        return self.condominio.apartamentos

#   RESERVAVEL  #

    def abre_tela_reservavel(self):
        switcher = {
            1: self.incluir_reservavel,
            2: self.alterar_reservavel,
            3: self.listar_reservaveis,
            4: self.excluir_reservavel,
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
        return self.__tela_condominio.seleciona_reservavel()

    def incluir_reservavel(self):
        dados_reservavel = self.__tela_condominio.pega_dados_reservavel(acao="criacao")

        reservavel = Reservavel(dados_reservavel["nome"],
                           dados_reservavel["id_reservavel"])

        self.__condominio.reservaveis.append(reservavel)


    def ocupar_apartamento(self, apartamento):
        self.condominio.apartamentos.remove(apartamento)

    def desocupar_apartamento(self, apartamento):
        self.condominio.apartamentos.append(apartamento)
        self.condominio.apartamentos.sort()

    def alterar_reservavel(self):
        pass

    def excluir_reservavel(self):
        pass

    def abre_tela_2(self):
        switcher = {
            1: self.ir_morador,
            2: self.ir_funcionario,
            3: self.ir_conta,
            4: self.ir_reservavel,
            5: self.ir_reserva,
            6: self.ir_entrega,
            0: self.abre_tela
        }

        while True:
            switcher[int(self.__tela_condominio.mostra_opcoes_2())]()

#   TELAS   #

    def ir_morador(self):
        self.__controlador_pessoa.abre_tela()

    def ir_funcionario(self):
        self.__controlador_pessoa.abre_tela_funcionario()

    def ir_conta(self):
        self.__controlador_conta.abre_tela()

    def ir_reservavel(self):
        self.abre_tela_reservavel()

    def ir_reserva(self):
        self.__controlador_reserva.abre_tela()

    def ir_entrega(self):
        self.__controlador_entrega.abre_tela()

    def outras_opcoes(self):
        self.abre_tela_2()

    def retornar(self):
        self.__controlador_sistema.retornar()
