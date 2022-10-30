from views.tela import Tela
import time


class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def tutorial_cadastro(self):
        print("\u001b[32m")
        print("Olá! Parece que essa é sua primeira vez utilizando o\u001b[34m CondoManager\u001b[32m...")
        time.sleep(2)
        print("Antes de tudo, é necessário o cadastro de um condomínio!")
        time.sleep(2)
        print(
            "Será necessário um\u001b[34m nome\u001b[32m, a\u001b[34m cidade\u001b[32m do condomínio, a\u001b[34m rua\u001b[32m do condomínio, o\u001b[34m número\u001b[32m do condomínio e o número de\u001b[34m apartamentos\u001b[32m do condomínio!.")
        time.sleep(2)


    def aviso_desligar(self):
        print("\033[1;36m")
        print("Até mais! Obrigado por usar o CondoManager! \033[0m")
        time.sleep(1)

    def aviso_resetar(self):
        print("\033[1;31m")
        print("ATENÇÃO!! Tem certeza de que deseja resetar o aplicativo?")
        time.sleep(1)
        if input("Digite: QUERO RESETAR: ").lower() == "quero resetar":
            print("OPERAÇÃO ACEITA!! Até mais!")
            time.sleep(1)
            return True
        else:
            print("OPERAÇÃO ABORTADA!! COMANDO INVÁLIDO")
            time.sleep(1)
            return False