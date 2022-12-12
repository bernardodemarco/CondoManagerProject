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

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)
