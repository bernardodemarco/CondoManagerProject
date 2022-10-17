class Cargo:
    def __init__(self, funcao: str, salario: int):
        self.__funcao = funcao
        self.__salario = salario

    @property
    def funcao(self) -> str:
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    @property
    def salario(self) -> int:
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
