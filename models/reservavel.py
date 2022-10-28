class Reservavel:

    def __init__(self, nome: str, id_reservavel: int):
        self.__nome = nome
        self.__id_reservavel = id_reservavel
        self.__horarios_indisponiveis = []

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
    def horarios_indisponiveis(self):
        return self.__horarios_indisponiveis
