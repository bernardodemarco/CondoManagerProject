from abc import ABC, abstractmethod
from controlador_sistema import ControladorSistema


class Controlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    @abstractmethod
    def abre_tela(self):
        pass
    
