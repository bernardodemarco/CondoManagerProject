import PySimpleGUI as sg
from views.tela import Tela
from utils.InvalidCPFException import InvalidCPFException
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.validate_cpf import validate_cpf
import re


class TelaMorador(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa
        self.__window = None

    def mostra_opcoes(self):
        layout = [
            [sg.Text('-------- MORADORES ----------', font=("Helvica", 25))],
            [sg.Text('O que gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir Morador', "RD1", key='1')],
            [sg.Radio('Alterar Morador', "RD1", key='2')],
            [sg.Radio('Excluir Morador', "RD1", key='3')],
            [sg.Radio('Listar Moradores', "RD1", key='4')],
            [sg.Radio('Visitas', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Moradores').Layout(layout)
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def pega_dados_morador(self, apartamentos, **kwargs):
        layout = [
            [sg.Text("DADOS DO MORADOR", font=("Helvica", 25))],
            [sg.Text("Digite o nome do morador: ", size=(40, 1)), sg.InputText("", key="nome")],
            [sg.Text("Digite o telefone do morador: ", size=(40, 1)), sg.InputText("", key="telefone")],
            [sg.Text("Digite o apartamento do morador: ", size=(40, 1)), sg.InputText("", key="apartamento")],
            [sg.Button("Enviar")]
        ]
        if kwargs['acao'] == 'alteracao':
            values["cpf"] = kwargs["cpf"]
        else:
            layout.insert(
                3, [sg.Text("Digite o CPF do morador: ", size=(40, 1)), sg.InputText("", key="cpf")]
            )
        self.__window = sg.Window("Dados do morador").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', values["nome"])) == False:
                    raise Exception
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', values["telefone"])) == False:
                    raise Exception
                if apartamento not in apartamentos:
                    raise Exception
            except Exception:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                validate_cpf(values["cpf"])
            except InvalidCPFException:
                sg.popup("CPF inválido! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if self.__controlador_pessoa.pega_morador_por_cpf(cpf):
                    raise ResourceAlreadyExistsException("Morador")
            except (ResourceAlreadyExistsException) as err:
                sg.popup(err, title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")  
            else:
                break            
        return {"nome": values["nome"], "cpf": values["cpf"], 'telefone': values["telefone"], 'apartamento': values["apartamento"]}

    def mostra_morador(self, dados):
        print('NOME DO MORADOR:', dados['nome'])
        print('TELEFONE DO MORADOR:', dados['telefone'])
        print('CPF DO MORADOR:', dados['cpf'])
        print('APARTAMENTO:', dados["apartamento"])
        print("<=======<<======================>>=======>")

    def seleciona_morador(self):
        while True:
            try:
                cpf_morador = input(('SELECIONE O MORADOR (digite o CPF): '))
                validate_cpf(cpf_morador)
                if self.__controlador_pessoa.pega_morador_por_cpf(cpf_morador) is not None:
                    return cpf_morador
                else:
                    raise ResourceNotFoundException("Morador")
            except InvalidCPFException as err:
                print("")
                print(err)
                print("")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    print("")
                    return None
            except ResourceNotFoundException as err:
                print("")
                print(err)
                print("")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    print("")
                    return None

#   VISITANTES  #

    def mostra_opcoes_visitantes(self):
        print("")
        print("<=======<<VISITANTES>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Visitante")
        print("        2 - Alterar Visitante")
        print("        3 - Excluir Visitante")
        print("        4 - Listar Visitante")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(4)

    def pega_dados_visitante(self, morador, **kwargs):
        print("")
        print("<=======<<DADOS VISITANTE>>=======>")
        while True:
            try:
                nome = input("Digite o nome do visitante: ")
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', nome)) == False:
                    raise Exception
                else:
                    nome = nome.title()
                    break
            except Exception:
                print("")
                print("ERRO!: Nome inválido, por favor, tente novamente")
                print("")
        while True:
            try:
                telefone = input("Digite o telefone do visitante: ")
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', telefone)) == False:
                    raise Exception
                else:
                    break
            except Exception:
                print("")
                print("ERRO!: Telefone inválido, por favor, tente novamente")
                print("")
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs['cpf']
        else:
            while True:
                cpf = input("Digite o CPF do visitante: ")
                try:
                    validate_cpf(cpf)
                    if self.__controlador_pessoa.pega_visitante_por_cpf(morador, cpf) and self.__controlador_pessoa.pega_morador_por_cpf(cpf):
                        raise ResourceAlreadyExistsException
                except (InvalidCPFException, ResourceAlreadyExistsException)as err:
                    print("")
                    print(err)
                    print("")
                else:
                    break
        print("<=======<<==================>>=======>")        
        return {"nome": nome, "cpf": cpf, 'telefone': telefone}
    
    def seleciona_visitante(self, morador):
        while True:
            try:
                cpf_visitante = input(('SELECIONE O VISITANTE (digite o CPF): '))
                validate_cpf(cpf_visitante)
                if self.__controlador_pessoa.pega_visitante_por_cpf(morador, cpf_visitante) is not None:
                    return cpf_visitante
                else:
                    raise ResourceNotFoundException("Visitante")
            except InvalidCPFException as err:
                print("")
                print(err)
                print("")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    print("")
                    return None
            except ResourceNotFoundException as err:
                print("")
                print(err)
                print("")
                if input("Gostaria de tentar novamente? Caso não queira, digite CANCELAR ").lower() == 'cancelar':
                    print("")
                    return None
    
    def mostra_visitante(self, dados):
        print('NOME DO VISITANTE:', dados['nome'])
        print('TELEFONE DO VISITANTE:', dados['telefone'])
        print('CPF DO VISITANTE:', dados['cpf'])
        print("<=======<<======================>>=======>")
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()