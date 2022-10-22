from abc import ABC, abstractmethod
import time

class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    def checa_opcao(self, valormax):
        while True:    
            try:
                print("")
                opcao = int(input("\033[1;32mPor favor, informe a seção desejada:\033[0m "))
                if 0 <= opcao <= valormax:
                    return opcao
                else:
                    raise ValueError
            except ValueError:
                print("")
                print("\033[0;31mERRO!: Opção inválida, por favor, tente novamente: \033[0m")
                time.sleep(1)
