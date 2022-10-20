from abc import ABC, abstractmethod


class Controlador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def retornar(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass
    
