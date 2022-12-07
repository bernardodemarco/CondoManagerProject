import PySimpleGUI as sg

from abc import ABC, abstractmethod
import time


class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    def checa_opcao(self, valormax):
        while True:
            try:
                print("")
                opcao = int(
                    input("Por favor, informe a seção desejada: "))
                if 0 <= opcao <= valormax:
                    return opcao
                else:
                    raise ValueError
            except ValueError:
                print("")
                print(
                    "ERRO!: Opção inválida, por favor, tente novamente: ")
                time.sleep(1)

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)
