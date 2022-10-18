from uuid import uuid4


class Reservavel:

    def __init__(self, nome: str):
        self.__nome = nome
        self.__id_reservavel = uuid4()
        self.__horarios_disponiveis = None

# PRA DEIXAR CLARO, TENHO QUE FAZER ISSO AINDA

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_reservavel(self) -> uuid4:
        return self.__id_reservavel
