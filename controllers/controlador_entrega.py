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

    def pega_dados_entregas(self, **kwargs):
        entregas = None
        if kwargs['status'] == 'todas':
            entregas = self.__entregas
        elif kwargs['status'] == 'pendentes':
            entregas = self.entregas_pendentes()
        dados_entregas = []
        for entrega in entregas:
            dados_entregas.append({
                'destinatario': entrega.destinatario.nome,
                'tipo': entrega.tipo.nome,
                'data_recebimento_condominio': entrega.data_recebimento_condominio,
                'data_recebimento_morador': entrega.data_recebimento_morador,
                'tempo': entrega.tempo_pendente_entrega(),
                'id': entrega.id_entrega
            })
        return dados_entregas

    def pega_dados_tipos(self):
        dados_tipos = []
        for tipo in self.__tipos_entrega:
            dados_tipos.append({
                'nome': tipo.nome,
                'id': tipo.id_tipo
            })
        return dados_tipos

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
            dados_entregas = self.pega_dados_entregas(status='todas')
            self.__tela_entrega.mostra_entrega(dados_entregas)
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)

    def lista_entregas_pendentes(self):
        try:
            if len(self.entregas_pendentes()) == 0:
                raise ResourceNotFoundException('Entregas pendentes')
            dados_entregas = self.pega_dados_entregas(status='pendentes')
            self.__tela_entrega.mostra_entrega(dados_entregas)
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)        

    def lista_tipos_entregas(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise ResourceNotFoundException('Tipos de entrega')

            dados_tipos = self.pega_dados_tipos()
            self.__tela_entrega.mostra_tipo_entrega(dados_tipos)
        except ResourceNotFoundException as err:
            self.__tela_entrega.mostra_mensagem(err)

    def incluir_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                self.__tela_entrega.close()
                self.__tela_entrega.mostra_mensagem(
                    'Cadastre um tipo de entrega primeiro!')
                self.incluir_tipo_entrega()

            self.lista_tipos_entregas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            dados = self.__tela_entrega.pega_dados_entrega()
            entrega = Entrega(tipo, morador, dados['id'])
            if entrega in self.__entregas:
                raise ResourceAlreadyExistsException('Entrega')
            self.__entregas.append(entrega)
            self.__tela_entrega.mostra_mensagem('ENTREGA CADASTRADA COM SUCESSO!')
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
            self.__tela_entrega.mostra_mensagem('TIPO DE ENTREGA CADASTRADA COM SUCESSO!')
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
            self.lista_entregas()
            dados_entregas = self.pega_dados_entregas(status='todas')
            id_entrega = self.__tela_entrega.seleciona_entrega(dados_entregas)
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            self.__tela_entrega.mostra_entrega([{
                'destinatario': entrega.destinatario.nome,
                'tipo': entrega.tipo.nome,
                'data_recebimento_condominio': entrega.data_recebimento_condominio,
                'data_recebimento_morador': entrega.data_recebimento_morador,
                'id': entrega.id_entrega,
                'tempo': entrega.tempo_pendente_entrega()
            }])

            self.lista_tipos_entregas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            morador = self.__controlador_condominio.controlador_pessoa.seleciona_morador()
            entrega.destinatario = morador
            entrega.tipo = tipo
            self.__tela_entrega.mostra_mensagem('ENTREGA ALTERADA COM SUCESSO!')
        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def alterar_tipo_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise Exception('Nenhum tipo de entrega registrado!')

            self.lista_tipos_entregas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da entrega')

            dados_alterados = self.__tela_entrega.pega_dados_tipo(
                acao='alteracao', id_tipo=id_tipo)
            tipo.nome = dados_alterados['nome_tipo']
            tipo.id_tipo = dados_alterados['id']
            self.__tela_entrega.mostra_mensagem('TIPO DE ENTREGA ALTERADA COM SUCESSO!')
        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def excluir_entrega(self):
        try:
            if len(self.__entregas) == 0:
                raise Exception('Nenhuma entrega registrada!')
            self.lista_entregas()
            dados_entregas = self.pega_dados_entregas(status='todas') 
            id_entrega = self.__tela_entrega.seleciona_entrega(dados_entregas)
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            self.__entregas.remove(entrega)
            self.__tela_entrega.mostra_mensagem('ENTREGA EXCLUÍDA COM SUCESSO!')
        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def excluir_tipo_entrega(self):
        try:
            if len(self.__tipos_entrega) == 0:
                raise Exception('Nenhum tipo de entrega registrado!')
            self.lista_tipos_entregas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_entrega.seleciona_tipo_entrega(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo de entrega')
            self.__tipos_entrega.remove(tipo)
            self.__tela_entrega.mostra_mensagem('TIPO DE ENTREGA EXCLUÍDA COM SUCESSO!')
        except ValueError:
            self.__tela_entrega.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_entrega.mostra_mensagem(err)

    def registro_coleta_morador(self):
        try:
            if len(self.entregas_pendentes()) == 0:
                raise ResourceNotFoundException('Entregas pendentes')
            
            self.lista_entregas_pendentes()
            dados_entregas = self.pega_dados_entregas(status='pendentes')
            id_entrega = self.__tela_entrega.seleciona_entrega(dados_entregas)
            entrega = self.pega_entrega_por_id(id_entrega)
            if entrega == None:
                raise ResourceNotFoundException('Entrega')
            entrega.data_recebimento_morador = datetime.now()
            self.__tela_entrega.mostra_mensagem('RECEBIMENTO DO MORADOR REGISTRADO COM SUCESSO')
            self.__tela_entrega.mostra_entrega([{
                'tipo': entrega.tipo.nome,
                'destinatario': entrega.destinatario.nome,
                'data_recebimento_condominio': entrega.data_recebimento_condominio,
                'data_recebimento_morador': entrega.data_recebimento_morador,
                'id': entrega.id_entrega,
                'tempo': entrega.tempo_pendente_entrega()
            }])
            
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
