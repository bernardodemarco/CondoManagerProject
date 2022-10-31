from views.tela import Tela
import time


class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def tutorial_cadastro(self):
        print("Olá! Parece que essa é sua primeira vez utilizando o CondoManager...")
        time.sleep(2)
        print("Antes de tudo, é necessário o cadastro de um condomínio!")
        time.sleep(2)
        print(
            "Será necessário um nome, a cidade do condomínio, a rua do condomínio, o número do condomínio e o número de apartamentos do condomínio!")
        time.sleep(2)


    def aviso_desligar(self):
        print("")
        print("Até mais! Obrigado por usar o CondoManager!")
        time.sleep(1)

    def aviso_resetar(self):
        print("")
        print("ATENÇÃO!! Tem certeza de que deseja resetar o aplicativo?")
        print("")
        time.sleep(1)
        if input("Digite: QUERO RESETAR: ").lower() == "quero resetar":
            print("")
            print("OPERAÇÃO ACEITA!! Até mais!")
            time.sleep(1)
            return True
        else:
            print("")
            print("OPERAÇÃO ABORTADA!! COMANDO INVÁLIDO")
            time.sleep(1)
            return False