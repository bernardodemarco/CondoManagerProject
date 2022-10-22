from controllers.controlador import Controlador
from views.tela_conta import TelaConta
from models.conta import Conta
from models.tipo_conta import TipoConta
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.ResourceNotFoundException import ResourceNotFoundException

class ControladorConta(Controlador):
    
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema
        self.__tela_conta = TelaConta()
        self.__contas = []
        self.__tipos_conta = []

    def pega_conta_por_id(self, id_conta):
        for conta in self.__contas:
            if conta.id_conta == id_conta:
                return conta
            return None

    def lista_contas(self):
        self.__tela_conta.mostra_mensagem('TODAS AS CONTAS CADASTRADAS:')
        for conta in self.__contas:
            self.__tela_conta.mostra_conta({
                'valor': conta.valor,
                'tipo': conta.tipo.nome,
                'mes': conta.mes,
                'id': conta.id_conta
            })

    def incluir_conta(self):
        try:
            dados = self.__tela_conta.pega_dados_contas(acao='criacao')
            tipo = TipoConta(dados['tipo'])
            conta = Conta(tipo, dados['valor'], dados['mes'], dados['id'])
            if conta in self.__contas:
                raise ResourceAlreadyExistsException('Conta')
            self.__contas.append(conta)
        except ValueError as err:
            print('Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            print(f'{err} (identificador já utilizado)')

    def alterar_conta(self):
        self.__tela_conta.mostra_mensagem("<=======<<EDITAR CONTA>>=======>")
        self.lista_contas()
        try:
            id_conta = self.__tela_conta.seleciona_conta()
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__tela_conta.mostra_conta({
                'valor': conta.valor,
                'tipo': conta.tipo.nome,
                'mes': conta.mes,
                'id': conta.id_conta
            })
            dados_alterados = self.__tela_conta.pega_dados_contas(acao='alteracao', id_conta=conta.id_conta)
            conta.valor = dados_alterados['valor']
            conta.tipo.nome = dados_alterados['tipo']
            conta.mes = dados_alterados['mes']
            conta.id = dados_alterados['id']
        except ValueError as err:
            print(err)

    def excluir_conta(self):
        self.__tela_conta.mostra_mensagem("<=======<<REMOVER CONTA>>=======>")
        self.lista_contas()
        try:
            id_conta = self.__tela_conta.seleciona_conta()
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__contas.remove(conta)
        except ResourceNotFoundException as err:
            print(err)
        except ValueError as err:
            print(err)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        switcher = {
            0: self.retornar,
            1: self.incluir_conta,
            2: self.alterar_conta,
            3: self.excluir_conta,
            4: self.lista_contas
        }

        while True:
            switcher[self.__tela_conta.mostra_opcoes()]()
