import PySimpleGUI as sg

from abc import ABC, abstractmethod
import time


class Tela(ABC):
    @abstractmethod
    def __init__(self):
        # self.__window = None SE A GENTE QUISER DA PARA NOS COLOCARMOS ESSE ATRIBUTO NA SUPERCLASSE,
        pass                  #ADICIONAR O GETTER E SETTER, DAI NAO PRECISA COLOCAR ELE EM TODAS SUBCLASSES
    
    # @property
    # def window(self):
    #     return self.__window

    # @window.setter
    # def window(self, value):
    #     self.__window = value

    #@abstractmethod depois LEMBRAR de DESCOMENTAR essa linhaa para deixar o metodo como sendo abstrato
    # def init_opcoes(self):
    #     pass
    
    @abstractmethod
    def mostra_opcoes(self):
        pass

    def mostra_mensagem(self, msg=''):
        sg.popup(msg)

    # def open(self):
    #     button, values = self.__window.Read()
    #     return button, values

    # def close(self):
    #     self.__window.Close()

    # DEPOIS DE TERMINAR AS INTERFACES LEMBRAR DE ALTERAR ESSE METODO E TIRAR OS QUE SOBREESCREVEM ELE NAS SUBCLASSES
