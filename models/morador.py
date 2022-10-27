from models.pessoa import Pessoa


class Morador(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int, apartamento: int): 
        super().__init__(nome, cpf, telefone)
        self.__apartamento = apartamento
        self.__visitantes = []

    @property
    def visitantes(self) -> list:
        return self.__visitantes

    @property
    def apartamento(self):
        return self.__apartamento

    @apartamento.setter
    def apartamento(self):
        return self.__apartamento