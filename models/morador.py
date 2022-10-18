from pessoa import Pessoa


class Morador(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int):
        super().__init__(nome, cpf, telefone)
        self.__visitantes = []

    @property
    def visitantes(self) -> list:
        return self.__visitantes
