from views.tela import Tela


class TelaCondominio(Tela):

    def __init__(self, controlador_condo):
        super().__init__()
        self.__controlador_condo = controlador_condo

    @property
    def controlador_condo(self):
        return self.__controlador_condo

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONDOMÍNIOS>>=======>")
        print("Para qual seção gostaria de ir?")
        print("    1 - Incluir Condomínio")
        print("    2 - Alterar Condomínio")
        print("    3 - Excluir Condomínio")
        print("    4 - Listar Condomínios")
        print("    5 - Apartamentos")
        print("    0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(5)
    
    def pega_dados_condo(self):
        print("\033[1;36m")
        print("<=======<<DADOS CONDOMÍNIO>>=======>")
        nome_condo = input("Nome do condomínio: ")
        endereco_condo = input("Endereço do condomínio: ")
        numero_condo = input("Número do condomínio: ")
        self.controlador_condo.controlador_sistema.controlador_pessoa.incluir_funcionario()