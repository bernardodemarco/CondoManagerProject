from models.reservavel import Reservavel
from models.morador import Morador


class Reserva:
    def __init__(self, id_reserva: int, horario: tuple, reservavel: Reservavel, morador: Morador) -> None:
        self.__id_reserva = id_reserva
        self.__horario = horario
        self.__reservavel = reservavel
        self.__morador = morador

    @property
    def id_reserva(self) -> int:
        return self.__id_reserva

    @id_reserva.setter
    def id_reserva(self, id_reserva: int) -> None:
        self.__id_reserva = id_reserva

    @property
    def horario(self) -> tuple:
        return self.__horario

    @horario.setter
    def horario(self, horario: tuple) -> None:
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

    def __eq__(self, other) -> bool:
        if isinstance(other, Reserva):
            return self.__id_reserva == other.id_reserva
        return False
