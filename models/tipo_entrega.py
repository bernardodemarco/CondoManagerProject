class TipoEntrega:
    def __init__(self, nome: str, id_tipo: int) -> None:
        self.__nome = nome
        self.__id_tipo = id_tipo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def id_tipo(self) -> int:
        return self.__id_tipo

    @id_tipo.setter
    def id_tipo(self, id_tipo: int) -> None:
        self.__id_tipo = id_tipo

    def __eq__(self, other) -> bool:
        if isinstance(other, TipoEntrega):
            return (self.__nome == other.nome or
                    self.__id_tipo == other.id_tipo)
        return False
