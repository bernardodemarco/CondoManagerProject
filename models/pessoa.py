from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, telefone: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def telefone(self) -> int:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
