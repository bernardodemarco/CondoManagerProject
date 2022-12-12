import PySimpleGUI as sg

from utils.InvalidCPFException import InvalidCPFException
from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException
from utils.validate_cpf import validate_cpf
from views.tela import Tela
import re


class TelaFuncionario(Tela):
    def __init__(self, controlador_pessoa):
        super().__init__()
        self.__controlador_pessoa = controlador_pessoa
        self.__window = None

    def mostra_opcoes(self):
        layout = [
            [sg.Text('-------- FUNCIONÁRIOS ----------', font=("Helvica", 25))],
            [sg.Text('O que gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Incluir Funcionário', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário', "RD1", key='2')],
            [sg.Radio('Excluir Funcionário', "RD1", key='3')],
            [sg.Radio('Listar Funcionário', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Funcionários').Layout(layout)
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def pega_dados_funcionario(self, **kwargs):
        layout = [
            [sg.Text("DADOS DO FUNCIONÁRIO", font=("Helvica", 25))],
            [sg.Text("Digite o nome do funcionário: ", size=(40, 1)),
             sg.InputText("", key="nome")],
            [sg.Text("Digite o telefone do funcionário: ", size=(
                40, 1)), sg.InputText("", key="telefone")],
            [sg.Text("Digite o cargo do funcionário: ", size=(40, 1)),
             sg.InputText("", key="cargo")],
            [sg.Text("Digite o salário do funcionário: ", size=(
                40, 1)), sg.InputText("", key="salario")],
            [sg.Button("Enviar")]
        ]
        if kwargs['acao'] == 'alteracao':
            cpf = kwargs["cpf"]
            layout.insert(
                3, [sg.Text(f"CPF do funcionário: {cpf}")]
            )
        else:
            layout.insert(
                3, [sg.Text("Digite o CPF do funcionário: ", size=(
                    40, 1)), sg.InputText("", key="cpf")]
            )
        self.__window = sg.Window("Dados do funcionário").Layout(layout)

        while True:
            button, values = self.open()
            try:
                if "cpf" in values:
                    cpf = ''.join(re.findall('[0-9]', values["cpf"]))
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', values["nome"])) == False:
                    raise ValueError
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', values["telefone"])) == False:
                    raise ValueError
                nome = values["nome"].title()
                telefone = ''.join(re.findall('[0-9]+', values["telefone"]))
                cargo = values["cargo"]
                salario = float(values["salario"])
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title="ERRO! Tente novamente", font=(
                    "Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    validate_cpf(values["cpf"])
            except InvalidCPFException:
                sg.popup("CPF inválido! Tente novamente!", title="ERRO! Tente novamente", font=(
                    "Halvica", 12), text_color="red")
                continue
            try:
                if not kwargs['acao'] == 'alteracao':
                    if self.__controlador_pessoa.pega_funcionario_por_cpf(values["cpf"]):
                        raise ResourceAlreadyExistsException("Funcionário")
            except (ResourceAlreadyExistsException) as err:
                sg.popup(err, title="ERRO! Tente novamente",
                         font=("Halvica", 12), text_color="red")
            else:
                self.close()
                break
        return {"nome": nome, "cpf": cpf, 'telefone': telefone, 'cargo': cargo, 'salario': salario}

    def mostra_funcionario(self, dados):
        todos_funcionario = ""
        for funcionario in dados:
            todos_funcionario += "Nome do morador: " + \
                funcionario['nome'] + "\n"
            todos_funcionario += "Telefone do morador: " + \
                funcionario['telefone'] + "\n"
            todos_funcionario += "CPF do morador: " + funcionario['cpf'] + "\n"
            todos_funcionario += "Cargo do morador: " + \
                funcionario['cargo'] + "\n"
            todos_funcionario += f"Salário do morador: {float(funcionario['salario']):.2f} \n\n"
        sg.popup("LISTA DE TODOS OS FUNCIONÁRIOS", todos_funcionario)

    def seleciona_funcionario(self, dados_funcionarios):
        layout = [
            [sg.Text("SELECIONE O FUNCIONÁRIO", font=("Halvica", 25))]
        ]
        for funcionario in dados_funcionarios:
            nome = funcionario["nome"]
            telefone = funcionario["telefone"]
            cpf = funcionario["cpf"]
            cargo = funcionario["cargo"]
            salario = funcionario["salario"]
            layout.append(
                [sg.Radio(f" NOME: {nome}\n TEL: {telefone}\n CPF: {cpf}\n CARGO: {cargo}\n SALÁRIO: {salario:.2f}",
                          "funcionarios", key=str(funcionario['cpf']))]
            )
        layout.append([sg.Button('Confirmar')])
        self.__window = sg.Window('Seleção de funcionário').Layout(layout)

        button, values = self.open()
        for cpf in values:
            if values[cpf]:
                self.close()
                return cpf

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
