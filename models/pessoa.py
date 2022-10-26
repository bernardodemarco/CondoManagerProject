from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
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

    def __str__(self):
        return f"Esse morador é o {self.nome}"
