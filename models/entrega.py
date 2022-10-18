from tipo_entrega import TipoEntrega
#from morador import Morador
from uuid import uuid4
from datetime import date, datetime

class Morador:
    def __init__(self, nome) -> None:
        self.nome = nome

class Entrega:
    def __init__(self, tipo: TipoEntrega, destinatario: Morador) -> None:
        self.__id_entrega = uuid4()
        self.__data_recebimento_condominio = date.today()
        self.__data_recebimento_morador = None
        self.__tipo = tipo
        self.__destinatario = destinatario

    @property
    def id_entrega(self):
        return self.__id_entrega
    
    @property
    def tipo(self) -> TipoEntrega:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoEntrega) -> None:
        self.__tipo = tipo

    @property
    def destinatario(self) -> Morador:
        return self.__destinatario

    @destinatario.setter
    def destinatario(self, destinatario: Morador) -> None:
        self.__destinatario = destinatario

    @property
    def data_recebimento_condominio(self):
        return self.__data_recebimento_condominio

    @property
    def data_recebimento_morador(self):
        return self.__data_recebimento_morador

    @data_recebimento_morador.setter
    def data_recebimento_morador(self, data):
        self.__data_recebimento_morador = data
