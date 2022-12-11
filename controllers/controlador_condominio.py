from utils.ResourceNotFoundException import ResourceNotFoundException
from controllers.controlador import Controlador
from controllers.controlador_conta import ControladorConta
from controllers.controlador_entrega import ControladorEntrega
from controllers.controlador_pessoa import ControladorPessoa
from controllers.controlador_reserva import ControladorReserva
from models.reservavel import Reservavel
from models.condominio import Condominio
from views.tela_condominio import TelaCondominio
from DAOs.condominio_dao import CondominioDAO
from DAOs.reservavel_dao import ReservavelDAO
import time



class ControladorCondominio(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__reservavel_dao = ReservavelDAO()
        self.__controlador_reserva = ControladorReserva(self, self.__reservavel_dao)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_condominio = TelaCondominio(self)
        self.__condominio_dao = CondominioDAO()

#   GETTERS E SETTERS   #

    @property
    def condominio_dao(self):
        return self.__condominio_dao

    @property
    def reservaveis(self):
        return self.__reservavel_dao.get_all()

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

        self.__condominio_dao.add(condo)
        self.__tela_condominio.mostra_mensagem("É necessário o cadastro de um funcionário para o condomínio.")
        self.__controlador_pessoa.incluir_funcionario()
        self.__tela_condominio.mostra_mensagem("Agora, é necessário o cadastro de um morador.")
        self.__controlador_pessoa.incluir_morador(condo.apartamentos)
        self.__tela_condominio.mostra_mensagem("Tudo certo para a utilização do CondoManager")

    def alterar_condo(self):
        condo = self.__condominio_dao.get_all()[0]
        dados_alterados = self.__tela_condominio.pega_dados_condo(acao='alteracao')
        condo.nome = dados_alterados["nome"]
        condo.cidade = dados_alterados["cidade"]
        condo.rua = dados_alterados["rua"]
        condo.numero = dados_alterados["numero"]
        condo.apartamentos = dados_alterados["apartamento"]
        self.__condominio_dao.update(condo)

    def mostra_dados_condo(self):
        apartamentos_ocupado_str = []
        condo = self.__condominio_dao.get_all()[0]
        for i in range(1, condo.num_max_ap+1):
            if not i in (condo.apartamentos):
                apartamentos_ocupado_str.append(str(i))
        self.__tela_condominio.mostra_condo({
            "nome": condo.nome,
            "cidade": condo.cidade,
            "rua": condo.rua,
            "numero": condo.numero,
            "total_ap": condo.num_max_ap,
            "apartamentos": apartamentos_ocupado_str
        })

    def resetar(self):
        self.controlador_sistema.resetar()

    def retorna_apartamento(self):
        condo = self.__condominio_dao.get_all()[0]
        return condo.apartamentos

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

    def pega_reservavel_por_id(self, id):
        reservaveis = self.__reservavel_dao.get_all()
        for reservavel in reservaveis:
            if (reservavel.id_reservavel == id):
                return reservavel
        return None

    def seleciona_reservavel(self):
        self.listar_reservaveis()
        return self.__tela_condominio.seleciona_reservavel(self.pega_dados_reservavel())

    def incluir_reservavel(self):
        dados_reservavel = self.__tela_condominio.pega_dados_reservavel(acao="criacao")

        reservavel = Reservavel(dados_reservavel["nome"],
                                dados_reservavel["id_reservavel"])

        self.__reservavel_dao.add(reservavel)
    
    def listar_reservaveis(self):
        reservaveis = self.__reservavel_dao.get_all()
        if len(reservaveis) == 0:
            self.__tela_condominio.mostra_mensagem("Não existem nenhum reservável cadastrado!")
        dados_reservaveis = self.pega_dados_reservavel()
        self.__tela_condominio.mostra_reservavel(dados_reservaveis)

    def alterar_reservavel(self):
        try:
            reservaveis = self.__reservavel_dao.get_all()
            if len(reservaveis) == 0:
                raise Exception('Nenhum reservável registrado!')
            self.listar_reservaveis()
            dados_reservavel = self.pega_dados_reservavel()
            id_reservavel = self.__tela_condominio.seleciona_reservavel(dados_reservavel)
            reservavel = self.pega_reservavel_por_id(id_reservavel)
            if reservavel == None:
                raise ResourceNotFoundException('Reservável')

            self.__tela_condominio.mostra_reservavel([{
                'nome': reservavel.nome,
                'id_reservavel': reservavel.id_reservavel,
            }])

            dados_alterados = self.__tela_condominio.pega_dados_reservavel(acao='alteracao', id_reservavel = reservavel.id_reservavel)
            reservavel.nome = dados_alterados['nome']
            reservavel.id_reservavel = dados_alterados["id_reservavel"]
            self.__reservavel_dao.update(reservavel)
        except ValueError as err:
            self.__tela_condominio.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_condominio.mostra_mensagem(err)
            

    def excluir_reservavel(self):
        try:
            reservaveis = self.__reservavel_dao.get_all()            
            if len(reservaveis) == 0:
                raise Exception('Nenhum reservável registrado!')
            self.listar_reservaveis()
            dados_reservavel = self.pega_dados_reservavel()
            id_reservavel = self.__tela_condominio.seleciona_reservavel(dados_reservavel)
            reservavel = self.pega_reservavel_por_id(id_reservavel)
            if reservavel == None:
                raise ResourceNotFoundException('Reservável')
            self.__reservavel_dao.remove(reservavel)
        except ResourceNotFoundException as err:
            self.__tela_condominio.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_condominio.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_condominio.mostra_mensagem(err)

    def pega_dados_reservavel(self):
        reservaveis = self.__reservavel_dao.get_all()
        dados_reservavel = []
        for reservavel in reservaveis:
            dados_reservavel.append({
                "nome": reservavel.nome,
                "id_reservavel": reservavel.id_reservavel
            })
        return dados_reservavel

    def ocupar_apartamento(self, apartamento):
        condo = self.__condominio_dao.get_all()[0]
        condo.apartamentos.remove(apartamento)

    def desocupar_apartamento(self, apartamento):
        condo = self.__condominio_dao.get_all()[0]
        condo.apartamentos.append(apartamento)
        condo.apartamentos.sort()

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
