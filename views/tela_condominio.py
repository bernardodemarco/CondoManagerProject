from views.tela import Tela


class TelaCondominio(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("Olá, você está na seção de condomínio!")
        return input()
    