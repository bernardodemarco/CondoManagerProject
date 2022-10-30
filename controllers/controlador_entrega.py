from datetime import datetime

from controllers.controlador import Controlador

from views.tela_entrega import TelaEntrega

from models.entrega import Entrega
from models.tipo_entrega import TipoEntrega

from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.ResourceNotFoundException import ResourceNotFoundException


class ControladorEntrega(Controlador):
    def __init__(self, controlador_condominio):
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_entrega = TelaEntrega()
        self.__entregas = []
        self.__tipos_entrega = []

    def pega_entrega_por_id(self, id_entrega: int):
        for entrega in self.__entregas:
            if entrega.id_entrega == id_entrega:
                return entrega
        return None

    def pega_tipo_por_id(self, id_tipo: int):
        for tipo in self.__tipos_entrega:
            if tipo.id_tipo == id_tipo:
                return tipo
        return None

    def entregas_pendentes(self):
        ''' Retorna lista de entregas que não foram coletadas pelos moradores '''
        return [entrega for entrega in self.__entregas if not entrega.data_recebimento_morador]

    def lista_entregas(self):
        try:
            if len(self.__entregas) == 0:
                raise ResourceNotFoundException('Entrega')

            self.__tela_entrega.mostra_mensagem(
                '<=======<<TODAS ENTREGAS CADASTRADAS>>=======>')
            for entrega in self.__entregas:
                self.__tela_entrega.mostra_entrega({
                    'destinatario': entrega.destinatario.nome,
                    'tipo': entrega.tipo.nome,
                    'data_recebimento_condominio': entrega.data_recebimento_condominio,
                    'data_recebimento_morador': entrega.data_recebimento_morador,
                    'id': entrega.id_entrega,
                    'tempo': entrega.tempo_pendente_entrega()
                })
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)

    def lista_entregas_pendentes(self):
        try:
            if len(self.entregas_pendentes()) == 0:
                raise ResourceNotFoundException('Entregas pendentes')

            self.__tela_entrega.mostra_mensagem(
                '<=======<<TODAS ENTREGAS PENDENTES>>=======>')
            for entrega in self.__entregas:
                if entrega.data_recebimento_morador == None:
                    self.__tela_entrega.mostra_entrega({
                        'destinatario': entrega.destinatario.nome,
                        'tipo': entrega.tipo.nome,
                        'data_recebimento_condominio': entrega.data_recebimento_condominio,
                        'data_recebimento_morador': entrega.data_recebimento_morador,
                        'id': entrega.id_entrega,
                        'tempo': entrega.tempo_pendente_entrega()
                    })
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)        

    def lista_tipos_entregas(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise ResourceNotFoundException('Tipos de entrega')

            self.__tela_entrega.mostra_mensagem(
                '<=======<<TODAS OS TIPOS DE ENTREGA CADASTRADOS>>=======>')
            for tipo in self.__tipos_entrega:
                self.__tela_entrega.mostra_tipo_entrega({
                    'nome': tipo.nome,
                    'id': tipo.id_tipo
                })
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)

    def incluir_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                self.__tela_entrega.mostra_mensagem(
                    'Cadastre um tipo de entrega primeiro!')
                self.incluir_tipo_entrega()

            self.lista_tipos_entregas()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            dados = self.__tela_entrega.pega_dados_entrega(acao='criacao')
            entrega = Entrega(tipo, morador, dados['id'])
            if entrega in self.__entregas:
                raise ResourceAlreadyExistsException('Entrega')
            self.__entregas.append(entrega)

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            self.__tela_entrega.mostra_mensagem(
                f'{err} (identificador já utilizado)')
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)

    def incluir_tipo_entrega(self):
        try:
            dados = self.__tela_entrega.pega_dados_tipo(acao='criacao')
            tipo = TipoEntrega(dados['nome_tipo'], dados['id'])

            if tipo in self.__tipos_entrega:
                raise ResourceAlreadyExistsException('Tipo de entrega')
            self.__tipos_entrega.append(tipo)

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            self.__tela_entrega.mostra_mensagem(
                f'{err} (Ou id já utilizado ou nome já cadastrado)')

    def alterar_entrega(self):
        try:
            if len(self.__entregas) == 0:
                raise Exception('Nenhuma entrega registrada!')

            self.__tela_entrega.mostra_mensagem(
                "<=======<<EDITAR ENTREGA>>=======>")
            self.lista_entregas()
            id_entrega = self.__tela_entrega.seleciona_entrega()
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            self.__tela_entrega.mostra_entrega({
                'destinatario': entrega.destinatario.nome,
                'tipo': entrega.tipo.nome,
                'data_recebimento_condominio': entrega.data_recebimento_condominio,
                'data_recebimento_morador': entrega.data_recebimento_morador,
                'id': entrega.id_entrega,
                'tempo': entrega.tempo_pendente_entrega()
            })

            self.lista_tipos_entregas()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            dados_alterados = self.__tela_entrega.pega_dados_entrega(
                acao='alteracao', id_entrega=entrega.id_entrega)
            entrega.destinatario = morador
            entrega.id_entrega = dados_alterados['id']
            entrega.tipo = tipo

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def alterar_tipo_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise Exception('Nenhum tipo de entrega registrado!')

            self.__tela_entrega.mostra_mensagem(
                "<=======<<EDITAR TIPO DE ENTREGA>>=======>")
            self.lista_tipos_entregas()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            dados_alterados = self.__tela_entrega.pega_dados_tipo(
                acao='alteracao', id_tipo=id_tipo)
            tipo.nome = dados_alterados['nome_tipo']
            tipo.id_tipo = dados_alterados['id']

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def excluir_entrega(self):
        try:
            if len(self.__entregas) == 0:
                raise Exception('Nenhuma entrega registrada!')

            self.__tela_entrega.mostra_mensagem(
                "<=======<<REMOVER ENTREGA>>=======>")
            self.lista_entregas()
            id_entrega = self.__tela_entrega.seleciona_entrega()
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            self.__entregas.remove(entrega)

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def excluir_tipo_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise Exception('Nenhum tipo de entrega registrado!')

            self.__tela_entrega.mostra_mensagem(
                "<=======<<REMOVER TIPO DE ENTREGA>>=======>")
            self.lista_tipos_entregas()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega()
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo de entrega')
            self.__tipos_entrega.remove(tipo)

        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def registro_coleta_morador(self):
        try:
            if len(self.entregas_pendentes()) == 0:
                raise ResourceNotFoundException('Entregas pendentes')
            
            self.__tela_entrega.mostra_mensagem(
                "<=======<<REGISTRANDO RECEBIMENTO DA ENTREGA PELO MORADOR>>=======>")
            self.lista_entregas_pendentes()
            id_entrega = self.__tela_entrega.seleciona_entrega()
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            entrega.data_recebimento_morador = datetime.now()
            self.__tela_entrega.mostra_mensagem(
                "<=======<<DATA DE RECEBIMENTO DO MORADOR REGISTRADA COM SUCESSO>>=======>")
            self.__tela_entrega.mostra_entrega({
                'tipo': entrega.tipo.nome,
                'destinatario': entrega.destinatario.nome,
                'data_recebimento_condominio': entrega.data_recebimento_condominio,
                'data_recebimento_morador': entrega.data_recebimento_morador,
                'id': entrega.id_entrega,
                'tempo': entrega.tempo_pendente_entrega()
            })
            
        except (ResourceNotFoundException, ValueError) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def retornar(self):
        self.__controlador_condominio.abre_tela_2()

    def abre_tela(self):
        switcher = {
            0: self.retornar,
            1: self.incluir_entrega,
            2: self.alterar_entrega,
            3: self.excluir_entrega,
            4: self.lista_entregas,
            5: self.lista_entregas_pendentes,
            6: self.incluir_tipo_entrega,
            7: self.alterar_tipo_entrega,
            8: self.excluir_tipo_entrega,
            9: self.lista_tipos_entregas,
            10: self.registro_coleta_morador
        }

        while True:
            switcher[self.__tela_entrega.mostra_opcoes()]()
