class InvalidTimeException(Exception):
    def __init__(self) -> None:
        super().__init__(
            '''
            Horário inválido. Lembre-se que as reservas
            podem ser efetuadas das 07:00
            até as 22:00 e o horário deve ser
            inserido na forma HORAS:MINUTOS.
            '''
        )
