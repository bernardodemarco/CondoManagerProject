from views.tela import Tela
import time

class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\033[1;36m")
        print("<======<<CondoManager>>======>")
        print("Para qual seção gostaria de ir?")
        print("        1 - Condomínios")
        print("        2 - Pessoas")
        print("        3 - Reservas")
        print("        4 - Entregas")
        print("        5 - Contas")
        print("        0 - Desligar Sistema")
        print("<======<<============>>======> \033[0m")
        return self.checa_opcao(5)

    def desligar(self):
        print("\033[1;36m")
        print("Até mais! Obrigado por usar o CondoManager! \033[0m")
        time.sleep(1)

