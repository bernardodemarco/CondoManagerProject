from DAOs.dao import DAO
from models.reserva import Reserva


class ReservaDAO(DAO):
    def __init__(self) -> None:
        super().__init__('reservas.pkl')

    def add(self, reserva: Reserva):
        if reserva is not None and isinstance(reserva, Reserva):
            super().add(reserva)

    def update(self, reserva: Reserva):
        if reserva is not None and isinstance(reserva, Reserva):
            super().update(reserva)

    def remove(self, reserva: Reserva):
        if reserva is not None and isinstance(reserva, Reserva):
            super().remove(reserva)
