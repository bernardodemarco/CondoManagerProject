class Condominio:
    def __init__(self, nome: str,
                 cidade: str,
                 rua: str,
                 numero: int,
                 apartamentos: int):
        self.__nome = nome
        self.__cidade = cidade
        self.__rua = rua
        self.__numero = numero
        self.__num_max_ap = int(apartamentos)
        self.__apartamentos = [i for i in range(1, int(apartamentos)+1)]

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def num_max_ap(self):
        return self.__num_max_ap

    @num_max_ap.setter
    def num_max_ap(self, num):
        self.__num_max_ap = num

    @property
    def apartamentos(self) -> list:
        return self.__apartamentos

    @apartamentos.setter
    def apartamentos(self, num):
        num = int(num)
        if num > self.num_max_ap:
            for i in range(self.num_max_ap + 1, num + 1, 1):
                self.apartamentos.append(i)
            self.num_max_ap = num
        elif num < self.num_max_ap:
            del self.apartamentos[-(self.num_max_ap - num):]
            self.num_max_ap = num
        elif num == self.num_max_ap:
            pass
