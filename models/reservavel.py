class Reservavel:
    def __init__(self, nome: str, id_reservavel: int):
        self.__nome = nome
        self.__id_reservavel = id_reservavel
        self.__horarios = dict()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_reservavel(self):
        return self.__id_reservavel

    @id_reservavel.setter
    def id_reservavel(self, id_reservavel: int) -> None:
        self.__id_reservavel = id_reservavel

    @property
    def horarios(self) -> dict:
        return self.__horarios

    def __eq__(self, other) -> bool:
        if isinstance(other, Reservavel):
            return self.__id_reservavel == other.id_reservavel
        return False