from models.pessoa import Pessoa
from DAOs.visitante_dao import VisitanteDAO


class Morador(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int, apartamento: int):
        super().__init__(nome, cpf, telefone)
        self.__apartamento = apartamento
        self.__visitantes_dao = VisitanteDAO(self)

    @property
    def visitantes_dao(self) -> list:
        self.__visitantes_dao = VisitanteDAO(self)
        return self.__visitantes_dao

    @property
    def apartamento(self):
        return self.__apartamento

    @apartamento.setter
    def apartamento(self):
        return self.__apartamento

    def get_visitantes_pickle(self):
        self.__visitantes_dao = VisitanteDAO(self)
