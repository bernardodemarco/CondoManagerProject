from abc import ABC, abstractmethod


class Controlador(ABC):
    @abstractmethod
    def __init__(self):
        self.__contador_id = 0

    @abstractmethod
    def retornar(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass

