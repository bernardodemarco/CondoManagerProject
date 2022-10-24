from views.tela import Tela
import time

class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def tutorial_cadastro(self):
        print("\u001b[32m")
        print("Olá! Parece que essa é sua primeira vez utilizando o CondoManager...")
        time.sleep(2)
        print("Antes de tudo, é necessário o cadastro de um condomínio!")
        time.sleep(2)
        print(
            "Será necessário um\u001b[34m nome\u001b[32m, um\u001b[34m numero\u001b[32m, um\u001b[34m endereço\u001b[32m, e um\u001b[34m funcionario.\u001b[32m")
        time.sleep(2)
        print("INDO PARA CADASTRO DE CONDOMÍNIOS")
        time.sleep(1)
        print('\033[1A\033[33C.')
        time.sleep(1)
        print('\033[1A\033[34C.')
        time.sleep(1)
        print('\033[1A\033[35C.')
        time.sleep(2)


    def desligar(self):
        print("\033[1;36m")
        print("Até mais! Obrigado por usar o CondoManager! \033[0m")
        time.sleep(1)
