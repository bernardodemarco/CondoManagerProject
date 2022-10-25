from models.reservavel import Reservavel
from models.morador import Morador
from uuid import uuid4


class Reserva:
    def __init__(self, horario: str, reservavel: Reservavel, morador: Morador) -> None:
        self.__id_reserva = uuid4()
        self.__horario = horario
        self.__reservavel = reservavel
        self.__morador = morador

    @property
    def id_reserva(self):
        return self.__id_reserva

    @property
    def horario(self) -> str:
        return self.__horario

    @horario.setter
    def horario(self, horario: str) -> None:
        self.__horario = horario

    @property
    def reservavel(self) -> Reservavel:
        return self.__reservavel

    @reservavel.setter
    def reservavel(self, reservavel: Reservavel) -> None:
        self.__reservavel = reservavel

    @property
    def morador(self) -> Morador:
        return self.__morador

    @morador.setter
    def morador(self, morador: Morador) -> None:
        self.__morador = morador
