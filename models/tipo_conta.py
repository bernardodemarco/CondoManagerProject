class TipoConta:
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    def __eq__(self, other) -> bool:
        if isinstance(other, TipoConta):
            return self.__nome == other.nome
        return False
