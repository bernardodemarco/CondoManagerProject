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
        print("")
        print("<=======<<FUNCIONÁRIOS>>=======>")
        print("    O que gostaria de fazer?")
        print("        1 - Incluir Funcionário")
        print("        2 - Alterar Funcionário")
        print("        3 - Excluir Funcionário")
        print("        4 - Listar Funcionário")
        print("        0 - Retornar")
        print("<=======<<============>>=======>")
        return self.checa_opcao(5)

    def pega_dados_funcionario(self, **kwargs):
        layout = [
            [sg.Text("DADOS DO FUNCIONÁRIO", font=("Helvica", 25))],
            [sg.Text("Digite o nome do funcionário: ", size=(40, 1)), sg.InputText("", key="nome")],
            [sg.Text("Digite o telefone do funcionário: ", size=(40, 1)), sg.InputText("", key="telefone")],
            [sg.Text("Digite o cargo do funcionário: ", size=(40, 1)), sg.InputText("", key="cargo")],
            [sg.Text("Digite o salário do funcionário: ", size=(40, 1)), sg.InputText("", key="salario")],
            [sg.Button("Enviar")]
        ]
        if kwargs['acao'] == 'alteracao':
            values["cpf"] = kwargs["cpf"]
        else:
            layout.insert(
                3, [sg.Text("Digite o CPF do funcionário: ", size=(40, 1)), sg.InputText("", key="cpf")]
            )
        self.__window = sg.Window("Dados do funcionário").Layout(layout)

        while True:
            button, values = self.open()
            try:
                values["salario"] = float(values["salario"])
                if bool(re.match('[a-zA-Zà-ÿÀ-Ý\s]+$', values["nome"])) == False:
                    raise ValueError
                if bool(re.match(r'\(?[1-9]{2}\)?\ ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', values["telefone"])) == False:
                    raise ValueError
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                validate_cpf(values["cpf"])
            except InvalidCPFException:
                sg.popup("CPF inválido! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
                continue
            try:
                if self.__controlador_pessoa.pega_funcionario_por_cpf(values["cpf"]):
                    raise ResourceAlreadyExistsException("Funcionário")
            except (ResourceAlreadyExistsException) as err:
                sg.popup(err, title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")   
            else:
                self.close()
                break            
        return {"nome": values["nome"], "cpf": values["cpf"], 'telefone': values["telefone"], 'cargo': values["cargo"], 'salario': values["salario"]}

    def mostra_funcionario(self, dados):
        print('NOME DO FUNCIONÁRIO:', dados['nome'])
        print('TELEFONE DO FUNCIONÁRIO:', dados['telefone'])
        print('CPF DO FUNCIONÁRIO:', dados['cpf'])
        print('CARGO DO FUNCIONÁRIO:', dados['cargo'])
        print(f'SALÁRIO DO FUNCIONÁRIO: R${dados["salario"]:.2f}')
        print("<=======<<======================>>=======>")

    def seleciona_funcionario(self):
        while True:
            try:
                cpf_funcionario = input(('SELECIONE O FUNCIONÁRIO (digite o CPF): '))
                validate_cpf(cpf_funcionario)
                if self.__controlador_pessoa.pega_funcionario_por_cpf(cpf_funcionario) is not None:
                    return cpf_funcionario
                else:
                    raise ResourceNotFoundException("Funcionário")
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
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()