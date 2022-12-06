from abc import ABC, abstractmethod
import time


class Tela(ABC):
    @abstractmethod
    def __init__(self):
        # self.__window = None SE A GENTE QUISER DA PARA NOS COLOCARMOS ESSE ATRIBUTO NA SUPERCLASSE,
        pass                  #ADICIONAR O GETTER E SETTER, DAI NAO PRECISA COLOCAR ELE EM TODAS SUBCLASSES
    
    # @property
    # def window(self):
    #     return self.__window

    # @window.setter
    # def window(self, value):
    #     self.__window = value

    #@abstractmethod depois LEMBRAR de DESCOMENTAR essa linhaa para deixar o metodo como sendo abstrato
    # def init_opcoes(self):
    #     pass
    
    @abstractmethod
    def mostra_opcoes(self):
        pass

    # DEPOIS LEMBRAR DE TIRAR ESSE METODO
    def checa_opcao(self, valormax):
        while True:
            try:
                print("")
                opcao = int(
                    input("Por favor, informe a seção desejada: "))
                if 0 <= opcao <= valormax:
                    return opcao
                else:
                    raise ValueError
            except ValueError:
                print("")
                print(
                    "ERRO!: Opção inválida, por favor, tente novamente: ")
                time.sleep(1)

    # def open(self):
    #     button, values = self.__window.Read()
    #     return button, values

    # def close(self):
    #     self.__window.Close()

    # DEPOIS DE TERMINAR AS INTERFACES LEMBRAR DE ALTERAR ESSE METODO E TIRAR OS QUE SOBREESCREVEM ELE NAS SUBCLASSES
    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
