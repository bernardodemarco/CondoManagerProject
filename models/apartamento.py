from morador import Morador

class Apartamento:
    def __init__(self, num: int, morador: Morador):
        self.__num = num
        self.__moradores = [morador]

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def moradores(self) -> list:
        return self.__moradores
