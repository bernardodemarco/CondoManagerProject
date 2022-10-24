from models.funcionario import Funcionario
from controllers.controlador import Controlador
from views.tela_funcionario import TelaFuncionario
from views.tela_morador import TelaMorador


class ControladorPessoa(Controlador):
    
    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_morador = TelaMorador()
        self.__tela_funcionario = TelaFuncionario()


    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario(acao="criacao")
        funcionario = Funcionario(dados_funcionario["nome"],
                                  dados_funcionario["cpf"],
                                  dados_funcionario["telefone"])
        
        return funcionario

    def retornar(self):
        self.__controlador_condominio.abre_tela()

    def abre_tela(self):
        pass
