class TipoConta:
    def __init__(self, tipo: str) -> None:
        self.__tipo = tipo

    @property
    def tipo(self) -> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self.__tipo = tipo
