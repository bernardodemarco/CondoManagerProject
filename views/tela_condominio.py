from views.tela import Tela


class TelaCondominio(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        while True:
            print("\033[1;36m")
            print("<=======<<Condomínios>>=======>")
            print("Para qual seção gostaria de ir?")
            print("        1 - Incluir Condomínio")
            print("        2 - Alterar Condomínio")
            print("        3 - Excluir Condomínio")
            print("        4 - Apartamentos")
            print("        0 - Retornar")
            print("<=======<<===========>>=======> \033[0m")
            try:
                print("")
                opcao = int(input("\033[1;32mPor favor, informe a seção desejada:\033[0m "))
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    raise ValueError
            except ValueError:
                print("")
                print("\033[0;31mERRO!: Opção inválida, por favor, tente novamente: \033[0m")

    