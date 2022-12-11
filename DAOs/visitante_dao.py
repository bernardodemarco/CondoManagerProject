from DAOs.dao import DAO
from models.visitante import Visitante


class VisitanteDAO(DAO):
    def __init__(self, morador) -> None:
        super().__init__(f'visitante_{morador.cpf}.pkl')

    def add(self, visitante: Visitante):
        if visitante is not None and isinstance(visitante, Visitante):
            super().add(visitante)

    def update(self, visitante: Visitante):
        if visitante is not None and isinstance(visitante, Visitante):
            super().update(visitante)

    def remove(self, visitante: Visitante):
        if visitante is not None and isinstance(visitante, Visitante):
            super().remove(visitante)
