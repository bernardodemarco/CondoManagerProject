from models.tipo_conta import TipoConta


class Conta:
    def __init__(self, tipo: TipoConta, valor: float, data, id_conta: int):
        self.__id_conta = id_conta
        self.__tipo = tipo
        self.__data = data
        self.__valor = valor

    @property
    def tipo(self) -> TipoConta:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoConta) -> None:
        self.__tipo = tipo

    @property
    def id_conta(self):
        return self.__id_conta

    @id_conta.setter
    def id_conta(self, id_conta: int) -> None:
        self.__id_conta = id_conta

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data) -> None:
        self.__data = data

    def __eq__(self, other) -> bool:
        if isinstance(other, Conta):
            return self.__id_conta == other.id_conta
        return False
