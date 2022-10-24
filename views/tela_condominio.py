from cmath import exp
from views.tela import Tela
import time


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

    def pega_dados_condo(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS CONDOMÍNIO>>=======>")
        try:
            nome = input("Digite o nome do condomínio: ")
            if kwargs['acao'] == 'alteracao':
                numero = kwargs['numero']
            else:
                numero = int(
                    input("Digite um número único (positivo) pro condomínio: "))
                if numero <= 0:
                    raise ValueError
            endereco = input("Digite o endereço do condomínio: ")
            print("É necessário o cadastro de um funcionário para o condomínio.")
            return {"nome": nome, "numero": numero, 'endereco': endereco}
        except ValueError:
            print("")
            print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
