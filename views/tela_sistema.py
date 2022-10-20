from views.tela import Tela


class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        return print("ALO")