from cmath import exp
from views.tela import Tela
import time


class TelaCondominio(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONDOMÍNIOS>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Condomínio")
        print("        2 - Alterar Condomínio")
        print("        3 - Excluir Condomínio")
        print("        4 - Listar Condomínios")
        print("        5 - Outras opções")
        print("        0 - Desligar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(5)

    def mostra_opcoes_2(self):
        print("\033[1;36m")
        print("<=======<<OUTRAS OPÇÕES>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Apartamentos")
        print("        2 - Moradores")
        print("        3 - Funcionários")
        print("        4 - Contas")
        print("        5 - Reservas")
        print("        6 - Entregas")
        print("        0 - Condomínios")
        print("<=======<<=============>>=======> \033[0m")
        return self.checa_opcao(6)

    def mostra_opcoes_apartamento(self):
        print("\033[1;36m")
        print("<=======<<APARTAMENTOS>>=======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Incluir Apartamento")
        print("        2 - Alterar Apartamento")
        print("        3 - Excluir Apartamento")
        print("        4 - Listar Apartamentos")
        print("        0 - Retornar")
        print("<=======<<============>>=======> \033[0m")
        return self.checa_opcao(4)

    def mostra_condo(self, dados):
        print("\033[1;36m")
        print("<=======<<LISTA DE CONDOMINIOS>>=======>")
        print('NOME DO CONDOMÍNIO:', dados['nome'])
        print('NÚMERO DO CONDOMÍNIO:', dados['numero'])
        print('ENDEREÇO DO CONDOMÍNIO:', dados['endereco'])
        print("<=======<<====================>>=======> \033[0m")

    def seleciona_condo(self):
        while True:
            try:
                print("\033[1;36m")
                numero = int(input("SELECIONE O CONDOMÍNIO (digite o numero): "))
                if isinstance(numero, int) and numero > 0:
                    return numero
                raise ValueError
            except ValueError:
                print("\033[0;31mERRO!: Número inválido, por favor, tente novamente: \033[1;36m")

    def pega_dados_condo(self, **kwargs):
        print("\033[1;36m")
        print("<=======<<DADOS CONDOMÍNIO>>=======>")
        nome = input("Digite o nome do condomínio: ")
        if kwargs['acao'] == 'alteracao':
            numero = kwargs['numero']
        else:
            while True:
                try:
                    numero = int(
                        input("Digite um número único (positivo) pro condomínio: "))
                    if numero <= 0:
                        raise ValueError
                except ValueError:
                    print("")
                    print("\033[0;31mERRO!: Número inválido! Por favor, tente novamente!")
                else:
                    break    
        endereco = input("Digite o endereço do condomínio: ")
        print("É necessário o cadastro de um funcionário para o condomínio.")
        return {"nome": nome, "numero": numero, 'endereco': endereco}
        
