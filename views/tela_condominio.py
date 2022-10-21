from views.tela import Tela


class TelaCondominio(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONDOMÍNIOS>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Incluir Condomínio")
        print("        2 - Alterar Condomínio")
        print("        3 - Excluir Condomínio")
        print("        4 - Listar Condomínios")
        print("        5 - Apartamentos")
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(5)
    