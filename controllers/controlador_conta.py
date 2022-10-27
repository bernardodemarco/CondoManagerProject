from controllers.controlador import Controlador

from views.tela_conta import TelaConta

from models.conta import Conta
from models.tipo_conta import TipoConta

from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.ResourceNotFoundException import ResourceNotFoundException


class ControladorConta(Controlador):
    def __init__(self, controlador_condominio) -> None:
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_conta = TelaConta()
        self.__contas = []
        self.__tipos_conta = []

    def pega_conta_por_id(self, id_conta: int):
        for conta in self.__contas:
            if conta.id_conta == id_conta:
                return conta
        return None

    def pega_tipo_por_id(self, id_tipo: int):
        for tipo in self.__tipos_conta:
            if tipo.id_tipo == id_tipo:
                return tipo
        return None

    def lista_contas(self):
        try:
            if len(self.__contas == 0):
                raise ResourceNotFoundException('Contas')

            self.__tela_conta.mostra_mensagem(
                '<=======<<TODAS CONTAS CADASTRADAS>>=======>')
            for conta in self.__contas:
                self.__tela_conta.mostra_conta({
                    'valor': conta.valor,
                    'tipo': conta.tipo.nome,
                    'data': conta.data,
                    'id': conta.id_conta
                })
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)

    def lista_tipos_contas(self):
        try:
            if len(self.__tipos_conta == 0):
                raise ResourceNotFoundException('Tipos de conta')

            self.__tela_conta.mostra_mensagem(
                '<=======<<TODAS OS TIPOS DE CONTA CADASTRADOS>>=======>')
            for tipo in self.__tipos_conta:
                self.__tela_conta.mostra_tipo_conta({
                    'nome': tipo.nome,
                    'id': tipo.id_tipo
                })
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)

    def incluir_conta(self):
        try:
            if len(self.__tipos_conta) == 0:
                self.__tela_conta.mostra_mensagem(
                    'Cadastre um tipo de conta primeiro!')
                self.incluir_tipo_conta()

            self.lista_tipos_contas()
            id_tipo = self.__tela_conta.seleciona_tipo_conta()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')

            dados = self.__tela_conta.pega_dados_contas(acao='criacao')
            conta = Conta(tipo, dados['valor'], dados['data'], dados['id'])
            if conta in self.__contas:
                raise ResourceAlreadyExistsException('Conta')
            self.__contas.append(conta)

        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            self.__tela_conta.mostra_mensagem(
                f'{err} (identificador já utilizado)')
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)

    def incluir_tipo_conta(self):
        try:
            dados = self.__tela_conta.pega_dados_tipo(acao='criacao')
            tipo = TipoConta(dados['nome_tipo'], dados['id'])

            if tipo in self.__tipos_conta:
                raise ResourceAlreadyExistsException('Tipo de conta')
            self.__tipos_conta.append(tipo)

        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            self.__tela_conta.mostra_mensagem(
                f'{err} (Ou id já utilizado ou nome já cadastrado)')

    def alterar_conta(self):
        try:
            if len(self.__contas) == 0:
                raise Exception('Nenhuma conta registrada!')

            self.__tela_conta.mostra_mensagem(
                "<=======<<EDITAR CONTA>>=======>")
            self.lista_contas()
            id_conta = self.__tela_conta.seleciona_conta()
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__tela_conta.mostra_conta({
                'valor': conta.valor,
                'tipo': conta.tipo.nome,
                'id': conta.id_conta,
                'data': conta.data
            })

            self.lista_tipos_contas()
            id_tipo = self.__tela_conta.seleciona_tipo_conta()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')

            dados_alterados = self.__tela_conta.pega_dados_contas(
                acao='alteracao', id_conta=conta.id_conta)
            conta.tipo = tipo
            conta.valor = dados_alterados['valor']
            conta.id_conta = dados_alterados['id']
            conta.data = dados_alterados['data']

        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)
        except Exception as err:
            self.__tela_conta.mostra_mensagem(err)

    def alterar_tipo_conta(self):
        try:
            if len(self.__tipos_conta) == 0:
                raise Exception('Nenhum tipo de conta registrado!')

            self.__tela_conta.mostra_mensagem(
                "<=======<<EDITAR TIPO DE CONTA>>=======>")
            self.lista_tipos_contas()
            id_tipo = self.__tela_conta.seleciona_tipo_conta()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')

            dados_alterados = self.__tela_conta.pega_dados_tipo(
                acao='alteracao', id_tipo=id_tipo)
            tipo.nome = dados_alterados['nome_tipo']
            tipo.id_tipo = dados_alterados['id']

        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_conta.mostra_mensagem(err)

    def excluir_conta(self):
        try:
            if len(self.__contas) == 0:
                raise Exception('Nenhuma conta registrada!')

            self.__tela_conta.mostra_mensagem(
                "<=======<<REMOVER CONTA>>=======>")
            self.lista_contas()
            id_conta = self.__tela_conta.seleciona_conta()
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__contas.remove(conta)

        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_conta.mostra_mensagem(err)

    def excluir_tipo_conta(self):
        try:
            if len(self.__tipos_conta) == 0:
                raise Exception('Nenhum tipo de conta registrado!')

            self.__tela_conta.mostra_mensagem(
                "<=======<<REMOVER TIPO DE CONTA>>=======>")
            self.lista_tipos_contas()
            id_tipo = self.__tela_conta.seleciona_tipo_conta()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo de conta')
            self.__tipos_conta.remove(tipo)

        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)
        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except Exception as err:
            self.__tela_conta.mostra_mensagem(err)

    def gerar_relatorio_mes(self):
        pass

    def retornar(self):
        self.__controlador_condominio.abre_tela_2()

    def abre_tela(self):
        switcher = {
            0: self.retornar,
            1: self.incluir_conta,
            2: self.alterar_conta,
            3: self.excluir_conta,
            4: self.lista_contas,
            5: self.incluir_tipo_conta,
            6: self.alterar_tipo_conta,
            7: self.excluir_tipo_conta,
            8: self.lista_tipos_contas,
            9: self.gerar_relatorio_mes
        }

        while True:
            switcher[int(self.__tela_conta.mostra_opcoes())]()
