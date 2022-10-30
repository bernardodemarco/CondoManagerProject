from models.funcionario import Funcionario
from models.morador import Morador
from controllers.controlador import Controlador
from views.tela_funcionario import TelaFuncionario
from views.tela_morador import TelaMorador
from collections import Counter
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException

class ControladorPessoa(Controlador):

    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_morador = TelaMorador(self)
        self.__tela_funcionario = TelaFuncionario(self)
        self.__moradores = []
        self.__funcionarios = []

    @property
    def controlador_condominio(self):
        return self.__controlador_condominio

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def moradores(self):
        return self.__moradores

    def pega_morador_por_cpf(self, cpf):
        for morador in self.moradores:
            if morador.cpf == cpf:
                return morador
            return None

    def pega_funcionario_por_cpf(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
            return None
    
    def pega_apartamento(self):
        apartamentos = self.controlador_condominio.retorna_apartamento()
        return apartamentos

    def incluir_morador(self, apartamentos):
        dados_morador = self.__tela_morador.pega_dados_morador(apartamentos, acao="criacao")

        morador = Morador(dados_morador["nome"],
                          dados_morador["cpf"],
                          dados_morador["telefone"],
                          dados_morador["apartamento"])

        self.moradores.append(morador)
        self.controlador_condominio.ocupar_apartamento(morador.apartamento)

    def alterar_morador(self, apartamentos):
        try:
            if len(self.moradores) == 0:
                raise Exception('Nenhum morador registrado!')

            self.__tela_morador.mostra_mensagem("\33[1;36m")
            self.__tela_morador.mostra_mensagem(
                "<=======<<EDITAR MORADOR>>=======>")
            self.listar_moradores()
            cpf = self.__tela_morador.seleciona_morador()
            morador = self.pega_morador_por_cpf(cpf)
            if morador == None:
                raise ResourceNotFoundException('Morador')

            self.__tela_morador.mostra_morador({
                'nome': morador.nome,
                'telefone': morador.telefone,
                'cpf': morador.cpf,
                'apartamento': morador.apartamento
            })

            dados_alterados = self.__tela_morador.pega_dados_morador(apartamentos, acao='alteracao', cpf = morador.cpf, apartamento = morador.apartamento)
            morador.nome = dados_alterados['nome']
            morador.telefone = dados_alterados['telefone']

        except ValueError as err:
            self.__tela_morador.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_morador.mostra_mensagem(err)
            
    def excluir_morador(self):
        try:
            if len(self.moradores) == 0:
                raise Exception('Nenhum morador registrado!')
            self.__tela_morador.mostra_mensagem("\33[1;36m")
            self.__tela_morador.mostra_mensagem(
                "<=======<<REMOVER MORADOR>>=======>")
            self.listar_moradores()
            cpf = self.__tela_morador.seleciona_morador()
            morador = self.pega_morador_por_cpf(cpf)
            if morador == None and not isinstance(morador, Morador):
                raise ResourceNotFoundException('Morador')
            self.controlador_condominio.desocupar_apartamento(morador.apartamento)
            self.moradores.remove(morador)

        except ResourceNotFoundException as err:
            self.__tela_morador.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_morador.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_morador.mostra_mensagem(err)

    def listar_moradores(self):
        self.__tela_morador.mostra_mensagem("\33[1;36m")
        self.__tela_morador.mostra_mensagem("<=======<<LISTAGEM DOS MORADORES>>=======>")
        for pessoa in self.moradores:
            self.__tela_morador.mostra_morador({
                'nome': pessoa.nome,
                'cpf': pessoa.cpf,
                'telefone': pessoa.telefone,
                'apartamento': pessoa.apartamento
            })

    def seleciona_morador(self):
        self.listar_moradores()
        return self.pega_morador_por_cpf(self.__tela_morador.seleciona_morador())

    def abre_tela(self):
        switcher = {
            1: self.incluir_morador,
            2: self.alterar_morador,
            3: self.excluir_morador,
            4: self.listar_moradores,
            5: self.seleciona_morador,
            0: self.retornar
        }

        while True:
            opcao = int(self.__tela_morador.mostra_opcoes())
            if opcao == 1:
                switcher[1](self.pega_apartamento())
            elif opcao == 2:
                switcher[2](self.pega_apartamento())
            else:
                switcher[opcao]()

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario(
            acao="criacao")
        if dados_funcionario == None:
            return None
        funcionario = Funcionario(dados_funcionario["nome"],
                                  dados_funcionario["cpf"],
                                  dados_funcionario["telefone"])

        self.funcionarios.append(funcionario)

    def alterar_funcionario(self):
        pass

    def excluir_funcionario(self):
        pass

    def listar_funcionarios(self):
        pass

    def abre_tela_funcionario(self):
        switcher = {
            1: self.incluir_funcionario,
            2: self.alterar_funcionario,
            3: self.excluir_funcionario,
            4: self.listar_funcionarios,
            0: self.retornar
        }

        while True:
            switcher[int(self.__tela_funcionario.mostra_opcoes())]()

    def retornar(self):
        self.__controlador_condominio.abre_tela()
