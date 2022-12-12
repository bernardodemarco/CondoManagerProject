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
            [sg.Button("Enviar")]
        ]
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs["cpf"]
            apartamento = kwargs["apartamento"]
            layout.insert(
                3, [sg.Text(f"CPF do morador: {cpf}")]
            )
            layout.insert(
                4, [sg.Text(f"Apartamento do morador: {apartamento}")]
            )
        else:
            layout.insert(
                3, [sg.Text("Digite o CPF do morador: ", size=(40, 1)), sg.InputText("", key="cpf")]
            )
            layout.insert(
                4, [sg.Text("Digite o apartamento do morador: ", size=(40, 1)), sg.InputText("", key="apartamento")]
            )
        self.__window = sg.Window("Dados do morador").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if "cpf" in values:
                    cpf = ''.join(re.findall('[0-9]', values["cpf"]))
                    apartamento = int(values["apartamento"])
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', values["nome"])) == False:
                    raise ValueError
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', values["telefone"])) == False:
                    raise ValueError
                nome = values["nome"]
                telefone = ''.join(re.findall('[0-9]+', values["telefone"]))
                if not kwargs['acao'] == 'alteracao':
                    if apartamento not in apartamentos:
                        raise ValueError
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    validate_cpf(values["cpf"])
            except InvalidCPFException:
                sg.popup("CPF inválido! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    if self.__controlador_pessoa.pega_morador_por_cpf(cpf):
                        raise ResourceAlreadyExistsException("Morador")
            except (ResourceAlreadyExistsException) as err:
                sg.popup(err, title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")   
            else:
                self.close()
                break            
        return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'apartamento': apartamento}

    def mostra_morador(self, dados_moradores):
        todos_moradores = ""
        for morador in dados_moradores:
            todos_moradores += "Nome do morador: " + morador['nome'] + "\n"
            todos_moradores += "Telefone do morador: " + morador['telefone'] + "\n"
            todos_moradores += "CPF do morador: " + morador['cpf'] + "\n"
            todos_moradores += "Apartamento do morador: " + str(morador['apartamento']) + "\n\n"
        sg.popup("LISTA DE TODOS OS MORADORES", todos_moradores)

    def seleciona_morador(self, dados_moradores):
        layout = [
            [sg.Text("SELECIONE O MORADOR", font = ("Halvica", 25))]
            ]
        for morador in dados_moradores:
            nome = morador["nome"]
            telefone = morador["telefone"]
            cpf = morador["cpf"]
            ap = morador["apartamento"]
            layout.append(
                [sg.Radio(f" NOME: {nome}\n TEL: {telefone}\n CPF: {cpf}\n AP: {ap}", "moradores", key=str(morador['cpf']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.__window = sg.Window('Seleção de morador').Layout(layout)

        button, values = self.open()
        for cpf in values:
            if values[cpf]:
                self.close()
                return cpf

#   VISITANTES  #

    def mostra_opcoes_visitantes(self):
        layout = [
            [sg.Text('-------- VISITANTES ----------', font=("Helvica", 25))],
            [sg.Text('O que gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir Visitante', "RD1", key='1')],
            [sg.Radio('Alterar Visitante', "RD1", key='2')],
            [sg.Radio('Excluir Visitante', "RD1", key='3')],
            [sg.Radio('Listar Visitante', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Visitantes').Layout(layout)
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def pega_dados_visitante(self, morador, **kwargs):
        layout = [
            [sg.Text("DADOS DO VISITANTE", font=("Helvica", 25))],
            [sg.Text("Digite o nome do visitante: ", size=(40, 1)), sg.InputText("", key="nome")],
            [sg.Text("Digite o telefone do visitante: ", size=(40, 1)), sg.InputText("", key="telefone")],
            [sg.Button("Enviar")]
        ]
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs["cpf"]
            layout.insert(
                3, [sg.Text(f"CPF do visitante: {cpf}")]
            )        
        else:
            layout.insert(
                3, [sg.Text("Digite o CPF do visitante: ", size=(40, 1)), sg.InputText("", key="cpf")]
            )
        self.__window = sg.Window("Dados do visitante").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if "cpf" in values:
                    cpf = ''.join(re.findall('[0-9]', values["cpf"]))
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', values["nome"])) == False:
                    raise ValueError
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', values["telefone"])) == False:
                    raise ValueError
                nome = values["nome"]
                telefone = ''.join(re.findall('[0-9]+', values["telefone"]))
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    validate_cpf(values["cpf"])
            except InvalidCPFException:
                sg.popup("CPF inválido! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    if self.__controlador_pessoa.pega_visitante_por_cpf(morador, cpf):
                        raise ResourceAlreadyExistsException("Visitante")
            except ResourceAlreadyExistsException as err:
                sg.popup(err, title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
            else:
                self.close()
                break            
        return {"nome": nome, "cpf": cpf, 'telefone': telefone}
    
    def seleciona_visitante(self, dados_visitantes):
        layout = [
            [sg.Text("SELECIONE O VISITANTE", font = ("Halvica", 25))]
            ]
        for visitante in dados_visitantes:
            nome = visitante["nome"]
            telefone = visitante["telefone"]
            cpf = visitante["cpf"]
            layout.append(
                [sg.Radio(f"NOME: {nome}\n TEL: {telefone}\n CPF: {cpf}", "visitantes", key=str(visitante['cpf']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.__window = sg.Window('Seleção de visitante').Layout(layout)

        button, values = self.open()
        for cpf in values:
            if values[cpf]:
                self.close()
                return cpf

    def mostra_visitante(self, dados):
        todos_visitantes = ""
        for visitante in dados:
            todos_visitantes += "Nome do visitante: " + visitante['nome'] + "\n"
            todos_visitantes += "Telefone do visitante: " + visitante['telefone'] + "\n"
            todos_visitantes += "CPF do visitante: " + visitante['cpf'] + "\n\n"
        sg.popup("LISTA DE TODOS OS VISITANTES", todos_visitantes)
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()