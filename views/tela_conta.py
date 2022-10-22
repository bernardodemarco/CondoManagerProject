from views.tela import Tela

class TelaConta(Tela):
    def __init__(self) -> None:
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<=======<<CONTAS>>=======>")
        print("O que você gostaria de fazer?")
        print("        1 - Incluir conta")
        print("        2 - Alterar conta")
        print("        3 - Excluir conta")
        print("        4 - Listar contas")
        print("        0 - Retornar")
        print("<=======<<===========>>=======> \033[0m")
        return self.checa_opcao(4)

    def pega_dados_tipo(self):
        print("<=======<<DADOS TIPO DA CONTA>>=======>")
        tipo = input('Digite o nome do tipo da conta:')
        return tipo

    def pega_dados_contas(self, **kwargs):
        tipo = self.pega_dados_tipo()
        print("<=======<<DADOS CONTA>>=======>")
        valor = float(input("Digite o valor da conta: "))
        mes = input('Digite o mês:')
        if kwargs['acao'] == 'alteracao':
            id_conta = kwargs['id_conta']
        else:
            id_conta = int(input('Digite um identificador (número inteiro positivo) para a conta: '))
        
        if (isinstance(tipo, str) and isinstance(valor, float) and
                valor > 0 and isinstance(mes, str) and
                isinstance(id_conta, int) and id_conta > 0):
            return {"tipo": tipo, "valor": valor, "mes": mes, 'id': id_conta}
        else:
            raise ValueError('Valores inválidos, tente novamente!')

    def mostra_conta(self, dados):
        print('TIPO DA CONTA:', dados['tipo'])
        print('VALOR DA CONTA:', dados['valor'])
        print('MES DA CONTA:', dados['mes'])
        print('ID DA CONTA:', dados['id'])
        print("<=======<<===========>>=======> \033[0m")

    def seleciona_conta(self):
        try:
            id_conta = int(input(('SELECIONE A CONTA (digite o identificador): ')))
            if isinstance(id_conta, int) and id_conta > 0:
                return id_conta
            raise ValueError
        except:
            raise ValueError('Valor do id inválido')

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
    
