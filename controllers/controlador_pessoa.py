from models.funcionario import Funcionario
from models.morador import Morador
from controllers.controlador import Controlador
from views.tela_funcionario import TelaFuncionario
from views.tela_morador import TelaMorador


class ControladorPessoa(Controlador):

    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_morador = TelaMorador(self)
        self.__tela_funcionario = TelaFuncionario(self)
        self.__pessoas = []

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def moradores(self):
        return self.__moradores

    def pega_pessoa_por_cpf(self, cpf: str):
        for pessoa in self.__pessoas:
            if (pessoa.cpf == cpf):
                return pessoa
        return None

    def incluir_morador(self):
        dados_morador = self.__tela_morador.pega_dados_morador(acao="criacao")
        morador = Morador(dados_morador["nome"],
                          dados_morador["cpf"],
                          dados_morador["telefone"])

        self.__pessoas.append(morador)

    def alterar_morador(self):
        pass

    def excluir_morador(self):
        pass

    def listar_moradores(self):
        for pessoa in self.__pessoas:
            if isinstance(pessoa, Morador):
                self.__tela_morador.mostra_morador({
                    'nome': pessoa.nome,
                    'cpf': pessoa.cpf,
                    'telefone': pessoa.telefone,
                })

    def seleciona_morador(self):
        self.listar_moradores()
        return self.pega_pessoa_por_cpf(self.__tela_morador.seleciona_morador())

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
            switcher[int(self.__tela_morador.mostra_opcoes())]()

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario(
            acao="criacao")
        if dados_funcionario == None:
            return None
        funcionario = Funcionario(dados_funcionario["nome"],
                                  dados_funcionario["cpf"],
                                  dados_funcionario["telefone"])

        self.__pessoas.append(funcionario)

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
