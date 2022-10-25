from models.tipo_entrega import TipoEntrega
from models.morador import Morador
from datetime import date


class Entrega:
    def __init__(self, tipo: TipoEntrega, destinatario: Morador, id_entrega: int) -> None:
        self.__tipo = tipo
        self.__destinatario = destinatario
        self.__id_entrega = id_entrega
        self.__data_recebimento_condominio = date.today()
        self.__data_recebimento_morador = None

    @property
    def id_entrega(self) -> int:
        return self.__id_entrega
    
    @id_entrega.setter
    def id_entrega(self, id_entrega: int) -> None:
        self.__id_entrega = id_entrega

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

    def __eq__(self, other) -> bool:
        if isinstance(other, Entrega):
            return self.__id_entrega == other.id_entrega
        return False
