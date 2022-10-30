from models.funcionario import Funcionario
from models.morador import Morador
from models.visitante import Visitante
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

#   GETTERS E SETTERS   #

    @property
    def controlador_condominio(self):
        return self.__controlador_condominio

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def moradores(self):
        return self.__moradores

#   MORADOR #

    def pega_morador_por_cpf(self, cpf):
        for morador in self.moradores:
            if morador.cpf == cpf:
                return morador
            return None

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
        return self.__tela_morador.seleciona_morador()
     
    def abre_tela(self):
        switcher = {
            1: self.incluir_morador,
            2: self.alterar_morador,
            3: self.excluir_morador,
            4: self.listar_moradores,
            5: self.abre_tela_visitantes,
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

#   VISITANTE #

    def incluir_visitante(self):
        morador = self.seleciona_morador()
        dados_visitante = self.__tela_morador.pega_dados_visitante(acao="criacao")

        visitante = Visitante(dados_visitante["nome"],
                          dados_visitante["cpf"],
                          dados_visitante["telefone"])

        morador.visitantes.append(visitante)

    def alterar_visitante(self):
        pass

    def excluir_visitante(self):
        pass

    def listar_visitante(self):
        pass

    def abre_tela_visitantes(self):
        switcher = {
            1: self.incluir_visitante,
            2: self.alterar_visitante,
            3: self.excluir_visitante,
            4: self.listar_visitante,
            0: self.abre_tela
        }

        while True:
            switcher[int(self.__tela_morador.mostra_opcoes_visitantes())]()

#   FUNCIONARIO #

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario(
            acao="criacao")
        if dados_funcionario == None:
            return None
        funcionario = Funcionario(dados_funcionario["nome"],
                                  dados_funcionario["cpf"],
                                  dados_funcionario["telefone"],
                                  dados_funcionario["cargo"],
                                  dados_funcionario["salario"])

        self.funcionarios.append(funcionario)

    def alterar_funcionario(self):
        try:
            if len(self.funcionarios) == 0:
                raise Exception('Nenhum funcionário registrado!')

            self.__tela_funcionario.mostra_mensagem("\33[1;36m")
            self.__tela_funcionario.mostra_mensagem(
                "<=======<<EDITAR FUNCIONÁRIO>>=======>")
            self.listar_funcionarios()
            cpf = self.__tela_funcionario.seleciona_funcionario()
            funcionario = self.pega_funcionario_por_cpf(cpf)
            if funcionario == None:
                raise ResourceNotFoundException('Funcionário')

            self.__tela_funcionario.mostra_funcionario({
                'nome': funcionario.nome,
                'telefone': funcionario.telefone,
                'cpf': funcionario.cpf,
                'cargo': funcionario.cargo,
                'salario': funcionario.salario
            })

            dados_alterados = self.__tela_funcionario.pega_dados_funcionario(acao='alteracao', cpf = funcionario.cpf)
            funcionario.nome = dados_alterados['nome']
            funcionario.telefone = dados_alterados['telefone']
            funcionario.cargo = dados_alterados['cargo']
            funcionario.salario = dados_alterados['salario']

        except ValueError as err:
            self.__tela_funcionario.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_funcionario.mostra_mensagem(err)
            

    def excluir_funcionario(self):
        try:
            if len(self.funcionarios) >= 1:
                raise Exception('Não é possível excluir nenhum funcionário! O condomínio não pode funcionar sem funcionários!')
            self.__tela_funcionario.mostra_mensagem("\33[1;36m")
            self.__tela_funcionario.mostra_mensagem(
                "<=======<<REMOVER FUNCIONÁRIO>>=======>")
            self.listar_funcionarios()
            cpf = self.__tela_funcionario.seleciona_funcionario()
            funcionario = self.pega_funcionario_por_cpf(cpf)
            if funcionario == None:
                raise ResourceNotFoundException('Funcionario')
            self.funcionarios.remove(funcionario)

        except ResourceNotFoundException as err:
            self.__tela_funcionario.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_funcionario.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_funcionario.mostra_mensagem(err)

    def listar_funcionarios(self):
        self.__tela_funcionario.mostra_mensagem("\33[1;36m")
        self.__tela_funcionario.mostra_mensagem("<=======<<LISTAGEM DOS FUNCIONÁRIOS>>=======>")
        for funcionario in self.funcionarios:
            self.__tela_funcionario.mostra_funcionario({
                'nome': funcionario.nome,
                'telefone': funcionario.telefone,
                'cpf': funcionario.cpf,
                'cargo': funcionario.cargo,
                'salario': funcionario.salario
            })

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

    def pega_funcionario_por_cpf(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
            return None

    def pega_apartamento(self):
        apartamentos = self.controlador_condominio.retorna_apartamento()
        return apartamentos
    