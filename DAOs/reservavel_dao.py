from DAOs.dao import DAO
from models.reservavel import Reservavel


class ReservavelDAO(DAO):
    def __init__(self) -> None:
        super().__init__('reservavel.pkl')

    def add(self, reservavel: Reservavel):
        if reservavel is not None and isinstance(reservavel, Reservavel):
            super().add(reservavel)

    def update(self, reservavel: Reservavel):
        if reservavel is not None and isinstance(reservavel, Reservavel):
            super().update(reservavel)

    def remove(self, reservavel: Reservavel):
        if reservavel is not None and isinstance(reservavel, Reservavel):
            super().remove(reservavel)
