from DAOs.dao import DAO
from models.condominio import Condominio


class CondominioDAO(DAO):
    def __init__(self) -> None:
        super().__init__('condominio.pkl')

    def add(self, condominio: Condominio):
        if condominio is not None and isinstance(condominio, Condominio):
            super().add(condominio)

    def update(self, condominio: Condominio):
        if condominio is not None and isinstance(condominio, Condominio):
            self._DAO__cache[0] = condominio
            self._DAO__dump()

    def remove(self, condominio: Condominio):
        if condominio is not None and isinstance(condominio, Condominio):
            super().remove(condominio)
