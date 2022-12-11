from DAOs.dao import DAO
from models.morador import Morador


class MoradorDAO(DAO):
    def __init__(self) -> None:
        super().__init__('morador.pkl')

    def add(self, morador: Morador):
        if morador is not None and isinstance(morador, Morador):
            super().add(morador)

    def update(self, morador: Morador):
        if morador is not None and isinstance(morador, Morador):
            super().update(morador)

    def remove(self, morador: Morador):
        if morador is not None and isinstance(morador, Morador):
            super().remove(morador)
