import PySimpleGUI as sg

from views.tela import Tela


class TelaSistema(Tela):

    def __init__(self):
        super().__init__()
        self.__window = None

    def mostra_opcoes(self):
        pass

    def tutorial_cadastro(self):
        sg.theme("DarkBlue2")
        sg.popup("Olá! Parece que essa é sua primeira vez utilizando o CondoManager...",
                 "Antes de tudo, é necessário o cadastro de um condomínio!",
                 "Será necessário um nome, a cidade do condomínio, a rua do condomínio, o número do condomínio e o número de apartamentos do condomínio!",
                 title="CondoManager",
                 font=("Halvica", 12))

    def aviso_desligar(self):
        sg.popup("Até mais! Obrigado por usar o CondoManager!",
                 title="CondoManager",
                 font=("Halvica", 12))

    def aviso_resetar(self):
        layout = [
            [sg.Text("ATENÇÃO!! Tem certeza de que deseja resetar o aplicativo?",
             font=("Halvica", 25), text_color="DarkRed")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("RESET").Layout(layout)
        button, values = self.open()
        if button in (None, "Confirmar"):
            self.close()
            return 1
        self.close()
        return 0

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
