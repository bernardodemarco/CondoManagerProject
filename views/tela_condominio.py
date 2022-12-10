import PySimpleGUI as sg

from multiprocessing.sharedctypes import Value
from views.tela import Tela

from utils.ResourceNotFoundException import ResourceNotFoundException
from utils.ResourceAlreadyExistsException import ResourceAlreadyExistsException

class TelaCondominio(Tela):

    def __init__(self, controlador_condo):
        super().__init__()
        self.__controlador_condo = controlador_condo
        self.__window = None

    @property
    def controlador_condo(self):
        return self.__controlador_condo

    def mostra_opcoes(self):
        sg.theme("DarkBlue2")
        layout = [
            [sg.Text('-------- CONDOMÍNIO ----------', font=("Helvica", 25))],
            [sg.Text('O que vocês gostaria de fazer?', font=("Helvica", 15))],
            [sg.Radio('Alterar condomínio', "RD1", key='1')],
            [sg.Radio('Mostrar dados do condomínio', "RD1", key='2')],
            [sg.Radio('Outras opções', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Desligar'), sg.Button("Resetar")]
        ]
        self.__window = sg.Window('Condomínio').Layout(layout)
        button, values = self.open()
        if button in (None, 'Desligar'):
            self.close()
            return 0
        elif button in (None, "Resetar"):
            self.close()
            return 4
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def mostra_opcoes_2(self):
        layout = [
            [sg.Text('-------- OUTRAS OPÇÕES ----------', font=("Helvica", 25))],
            [sg.Text('Para qual seção gostaria de ir?', font=("Helvica", 15))],
            [sg.Radio('Moradores', "RD1", key='1')],
            [sg.Radio('Funcionários', "RD1", key='2')],
            [sg.Radio('Contas', "RD1", key='3')],
            [sg.Radio('Reservável', "RD1", key='4')],
            [sg.Radio('Reservas', "RD1", key='5')],
            [sg.Radio('Entregas', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Outras opções').Layout(layout)
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def mostra_opcoes_reservavel(self):
        layout = [
            [sg.Text('-------- RESERVÁVEL ----------', font=("Helvica", 25))],
            [sg.Text('Para qual seção gostaria de ir?', font=("Helvica", 15))],
            [sg.Radio('Incluir reservável', "RD1", key='1')],
            [sg.Radio('Alterar reservável', "RD1", key='2')],
            [sg.Radio('Listar reservável', "RD1", key='3')],
            [sg.Radio('Excluir reservável', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Reservável').Layout(layout)
        button, values = self.open()
        if button in (None, 'Retornar'):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)

    def mostra_condo(self, dados):
        sg.popup("Nome do condomínio:", dados["nome"],
        "Cidade do condomínio:", dados["cidade"],
        "Rua do condomínio:", dados["rua"],
        "Número do condomínio:", dados["numero"],
        "Total de apartamentos:", dados["total_ap"],
        "Apartamentos individuais indisponíveis:", ", ".join(dados["apartamentos"]),
         font = ("Halvica", 12), title = "Dados do condomínio")

    def pega_dados_condo(self, **kwargs):
        layout = [
            [sg.Text("DADOS DO CONDOMÍNIO", font=("Helvica", 25))],
            [sg.Text("Digite o nome do condomínio:", size=(40, 1)), sg.InputText("", key="nome")],
            [sg.Text("Digite a cidade do condomínio:", size=(40, 1)), sg.InputText("", key="cidade")],
            [sg.Text("Digite a rua do condomínio:", size=(40, 1)), sg.InputText("", key="rua")],
            [sg.Text("Digite o número do condomínio:", size=(40, 1)), sg.InputText("", key="numero")],
            [sg.Text("Digite o número de apartamentos deste condomínio:", size=(40, 1)), sg.InputText("", key="apartamento")],
            [sg.Button("Enviar")]
        ]
        self.__window = sg.Window("Dados do condomínio").Layout(layout)
        while True:
            button, values = self.open()
            try:
                values["numero"] = int(values["numero"])
                values["apartamento"] = int(values["apartamento"])
                if not values["cidade"].isalpha():
                    raise ValueError
                if values["rua"].isdigit():
                    raise ValueError
                if values["numero"] <= 0:
                    raise ValueError
                if values["apartamento"] <= 0:
                    raise ValueError
                if kwargs['acao'] == 'alteracao':
                    condo = self.__controlador_condo.condominio_dao.get_all()[0]
                    for i in range(1, condo.apartamentos[-1]):
                        if i not in condo.apartamentos:
                            if int(values["apartamento"]) < i:
                                raise ValueError
                self.close()
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
            else:
                break
        return {"nome": values["nome"], "cidade": values["cidade"], "rua": values["rua"], "numero": values["numero"],  "apartamento": values["apartamento"]}

    def pega_dados_reservavel(self, **kwargs):
        layout = [
            [sg.Text("DADOS DO RESERVÁVEL", font=("Helvica", 25))],
            [sg.Text("Digite o nome do reservável:", size=(40, 1)), sg.InputText("", key="nome")],
            [sg.Button("Cadastrar reservável"), sg.Cancel("Retornar")]
        ]
        if kwargs['acao'] == 'alteracao':
            id_reservavel = kwargs['id_reservavel']
            layout.insert(
                2, [sg.Text(f"ID do reservável: {id_reservavel}")]
            )
        else:
            layout.insert(
                2, [sg.Text("Digite um número único (positivo) pro reservável:", size=(40, 1)), sg.InputText("", key="id_reservavel")]
            )
        self.__window = sg.Window("Dados do condomínio").Layout(layout)
        while True:
            button, values = self.open()
            try:
                nome = values["nome"]
                if id_reservavel in values:
                    id_reservavel = int(values["id_reservavel"])
                if id_reservavel <= 0:
                    raise ValueError
                self.close()
            except ValueError:
                sg.popup("Valores inválidos! Tente novamente!", title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
            try:
                if not kwargs['acao'] == 'alteracao':
                    if self.__controlador_condo.pega_reservavel_por_id(id_reservavel):
                        raise ResourceAlreadyExistsException("Reservável")
            except ResourceAlreadyExistsException as err:
                sg.popup(err, title = "ERRO! Tente novamente", font = ("Halvica", 12), text_color="red")
            else:
                break
        return {"nome": nome, "id_reservavel": id_reservavel}

    def mostra_reservavel(self, dados):
        todos_reservaveis = ""
        for reservavel in dados:
            todos_reservaveis += "Nome do reservável: ", str(reservavel["nome"]) + '\n'
            todos_reservaveis += "ID do reservável: ", str(reservavel["id_reservavel"]) + '\n\n'
        sg.popup("LISTA DE TODOS OS RESERVÁVEIS", todos_reservaveis ,font = ("Halveca", 12), title = "Reserváveis")

    def seleciona_reservavel(self, dados):
        layout = [
            [sg.Text("SELECIONE O RESERVÁVEL", font=("Helvica", 25))]
        ]
        for reservavel in dados:
            nome = reservavel["nome"]
            id_reservavel = reservavel["id_reservavel"]
            layout.append(
                [sg.Radio(f"{nome}: ID {id_reservavel}")]
            )
        layout.append(sg.Button("Confirmar"))
        self.__window = sg.Window("Seleção de reservável").Layout(layout)

        button, values = self.open()
        for id_reservavel in values:
            if values[id_reservavel]:
                self.close()
                return int(id_reservavel)


    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
