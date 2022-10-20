from models.tipo_conta import TipoConta
from uuid import uuid4


class Conta:
    def __init__(self, tipo: TipoConta, valor: float, mes: str) -> None:
        self.__id_conta = uuid4()
        self.__tipo = tipo
        self.__mes = mes
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

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor
    
    @property
    def mes(self) -> str:
        return self.__mes
    
    @mes.setter
    def mes(self, mes: str) -> None:
        self.__mes = mes
