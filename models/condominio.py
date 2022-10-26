from models.funcionario import Funcionario


class Condominio:

    def __init__(self, nome: str,
                 numero: int,
                 endereco: str,
                 funcionario: Funcionario):
        self.__nome = nome
        self.__numero = numero
        self.__endereco = endereco
        self.__funcionarios = [funcionario]
        self.__apartamentos = []
        self.__reservaveis = []
        self.__contas = []
        self.__entregas = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def funcionarios(self) -> list:
        return self.__funcionarios

    @property
    def apartamentos(self) -> list:
        return self.__apartamentos

    @property
    def reservaveis(self) -> list:
        return self.__reservaveis

    @property
    def contas(self) -> list:
        return self.__contas

    @property
    def entregas(self) -> list:
        return self.__entregas
