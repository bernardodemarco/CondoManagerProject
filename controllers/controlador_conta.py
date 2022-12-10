from controllers.controlador import Controlador

from views.tela_conta import TelaConta

from models.conta import Conta
from models.tipo_conta import TipoConta

from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.ResourceNotFoundException import ResourceNotFoundException

from DAOs.conta_dao import ContaDAO
from DAOs.tipo_conta_dao import TipoContaDAO


class ControladorConta(Controlador):
    def __init__(self, controlador_condominio) -> None:
        super().__init__()
        self.__controlador_condominio = controlador_condominio
        self.__tela_conta = TelaConta()
        self.__contas_dao = ContaDAO()
        self.__tipos_dao = TipoContaDAO()

    def pega_dados_contas(self):
        dados_contas = []
        for conta in self.__contas_dao.get_all():
            dados_contas.append({
                'valor': conta.valor,
                'tipo': conta.tipo.nome,
                'data': conta.data,
                'id': conta.id_conta
            })
        return dados_contas

    def pega_dados_tipos(self):
        dados_tipos = []
        for tipo in self.__tipos_dao.get_all():
            dados_tipos.append({
                'nome': tipo.nome,
                'id': tipo.id_tipo
            })
        return dados_tipos

    def pega_conta_por_id(self, id_conta: int):
        for conta in self.__contas_dao.get_all():
            if conta.id_conta == id_conta:
                return conta
        return None

    def pega_tipo_por_id(self, id_tipo: int):
        for tipo in self.__tipos_dao.get_all():
            if tipo.id_tipo == id_tipo:
                return tipo
        return None

    def lista_contas(self):
        try:
            if len(self.__contas_dao.get_all()) == 0:
                raise ResourceNotFoundException('Contas')
            dados_contas = self.pega_dados_contas()
            self.__tela_conta.mostra_conta(dados_contas)
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)

    def lista_tipos_contas(self):
        try:
            if len(self.__tipos_dao.get_all()) == 0:
                raise ResourceNotFoundException('Tipos de conta')
            dados_tipos = self.pega_dados_tipos()
            self.__tela_conta.mostra_tipo_conta(dados_tipos)
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)

    def incluir_conta(self):
        try:
            if len(self.__tipos_dao.get_all()) == 0:
                self.__tela_conta.close()
                self.__tela_conta.mostra_mensagem(
                    'Cadastre um tipo de conta primeiro!')
                self.incluir_tipo_conta()

            self.lista_tipos_contas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_conta.seleciona_tipo_conta(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')

            dados = self.__tela_conta.pega_dados_contas(acao='criacao')
            conta = Conta(tipo, dados['valor'], dados['data'], dados['id'])
            if conta in self.__contas_dao.get_all():
                raise ResourceAlreadyExistsException('Conta')
            self.__contas_dao.add(conta)
            self.__tela_conta.mostra_mensagem('CONTA INCLUÍDA COM SUCESSO!')

        except ValueError:
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

            if tipo in self.__tipos_dao.get_all():
                raise ResourceAlreadyExistsException('Tipo de conta')
            self.__tipos_dao.add(tipo)
            self.__tela_conta.mostra_mensagem('TIPO DE CONTA INCLUÍDO COM SUCESSO!')

        except ValueError:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except ResourceAlreadyExistsException as err:
            self.__tela_conta.mostra_mensagem(
                f'{err} (Ou id já utilizado ou nome já cadastrado)')

    def alterar_conta(self):
        try:
            if len(self.__contas_dao.get_all()) == 0:
                raise Exception('Nenhuma conta registrada!')

            self.lista_contas()
            dados_contas = self.pega_dados_contas()
            id_conta = self.__tela_conta.seleciona_conta(dados_contas)
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__tela_conta.mostra_conta([{
                'valor': conta.valor,
                'tipo': conta.tipo.nome,
                'id': conta.id_conta,
                'data': conta.data
            }])

            self.lista_tipos_contas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_conta.seleciona_tipo_conta(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')
            dados_alterados = self.__tela_conta.pega_dados_contas(
                acao='alteracao', id_conta=conta.id_conta)
            conta.tipo = tipo
            conta.valor = dados_alterados['valor']
            conta.id_conta = dados_alterados['id']
            conta.data = dados_alterados['data']
            self.__contas_dao.update(conta)
            self.__tela_conta.mostra_mensagem('CONTA ATUALIZADA COM SUCESSO!')
        except ValueError as err:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_conta.mostra_mensagem(err)

    def alterar_tipo_conta(self):
        try:
            if len(self.__tipos_dao.get_all()) == 0:
                raise Exception('Nenhum tipo de conta registrado!')

            self.lista_tipos_contas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_conta.seleciona_tipo_conta(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo da conta')
            dados_alterados = self.__tela_conta.pega_dados_tipo(
                acao='alteracao', id_tipo=id_tipo)
            tipo.nome = dados_alterados['nome_tipo']
            tipo.id_tipo = dados_alterados['id']
            self.__tipos_dao.update(tipo)
            self.__tela_conta.mostra_mensagem('TIPO DE CONTA ATUALIZADO COM SUCESSO!')
        except ValueError:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_conta.mostra_mensagem(err)

    def excluir_conta(self):
        try:
            if len(self.__contas_dao.get_all()) == 0:
                raise Exception('Nenhuma conta registrada!')
            self.lista_contas()
            dados_contas = self.pega_dados_contas()
            id_conta = self.__tela_conta.seleciona_conta(dados_contas)
            conta = self.pega_conta_por_id(id_conta)
            if conta == None:
                raise ResourceNotFoundException('Conta')
            self.__contas_dao.remove(conta)
            self.__tela_conta.mostra_mensagem('CONTA EXCLUÍDA COM SUCESSO')
        except ValueError:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_conta.mostra_mensagem(err)

    def excluir_tipo_conta(self):
        try:
            if len(self.__tipos_dao.get_all()) == 0:
                raise Exception('Nenhum tipo de conta registrado!')

            self.lista_tipos_contas()
            dados_tipos = self.pega_dados_tipos()
            id_tipo = self.__tela_conta.seleciona_tipo_conta(dados_tipos)
            tipo = self.pega_tipo_por_id(id_tipo)
            if tipo == None:
                raise ResourceNotFoundException('Tipo de conta')
            self.__tipos_dao.remove(tipo)
            self.__tela_conta.mostra_mensagem('TIPO DE CONTA EXCLUÍDO COM SUCESSO!')
        except ValueError:
            self.__tela_conta.mostra_mensagem(
                'Valores inválidos, tente novamente!')
        except (ResourceNotFoundException, Exception) as err:
            self.__tela_conta.mostra_mensagem(err)

    def gerar_relatorio_mes(self):
        ''' Geração de relatório de contas de um mês e ano específico ''' 
        try:
            contas = self.__contas_dao.get_all()
            if len(contas) == 0:
                raise ResourceNotFoundException('Conta')

            dados_relatorio = self.__tela_conta.pega_dados_relatorio()  
            mes = dados_relatorio['mes']
            ano = dados_relatorio['ano']       
            contas_relatorio = [conta for conta in contas if conta.data.year == ano and conta.data.month == mes]       
            total = 0
            dados = dict()
            dados['mes'] = mes
            dados['ano'] = ano
            for conta in contas_relatorio:
                dados[conta.tipo.nome] = dados.get(conta.tipo.nome, 0) + conta.valor
                total += conta.valor
            dados['TOTAL'] = total
            self.__tela_conta.mostra_relatorio(dados)
        except ResourceNotFoundException as err:
            self.__tela_conta.mostra_mensagem(err)
    
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
            switcher[self.__tela_conta.mostra_opcoes()]()
