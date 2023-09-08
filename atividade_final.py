import json
from datetime import date
class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.nome = nome
        self.especialidade = especialidade
        self.sala = sala
    def get_nome(self):
        return self.nome
    def get_sala(self):
        return self.sala
class Visitante:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento
    def get_visitante(self):
        return self.visitante

    def get_profissional(self):
        return self.profissional

    def get_data_entrada(self):
        return self.data_entrada
class Visita:
    def __init__(self,visitante,profissional, data_entrada):
        self.visitante = visitante
        self.profissional = profissional
        self.data_entrada = data_entrada
    def get_profissional(self):
        return self.profissional
    def get_visitante(self):
        return self.visitante
    def get_data_entrada(self):
        return self.data_entrada

def ler_profissionais():
    caminho = "C:/Users/Usuário\Documents/"
    arquivo = open(caminho+"profissionais.txt","r")
    for ind, linha in enumerate(arquivo):
        pro_arq = linha.split(':')
        profissonal = Profissional(pro_arq[0],pro_arq[1],pro_arq[2])
        l_profissionais.append(profissonal)
        print(pro_arq)
    arquivo.close()
    print(l_profissionais)

def ler_visitantes():
    caminho = "C:/Users/Usuário\Documents/"
    arquivo = open(caminho+"visitantes.txt","r")
    for ind, linha in enumerate(arquivo):
        pro_arq = linha.split(':')
        visitante = Visitante(pro_arq[0],pro_arq[1])
        l_visitantes.append(visitante)
        print(pro_arq)
    arquivo.close()
    print(l_profissionais)

def add_profissional():
    nome = input("Qual o nome do profissional? ")
    especialidade = input("Qual a especialidade? ")
    sala = input("Qual a sala? ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    print(l_profissionais)
def add_visitantes():
    nome = input("Qual seu nome? ")
    documento = input("Qual seu documento? ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    print(l_visitantes)

def localizar():
    nome_digitado = input("Qual o nome do profissional que procuras?")
    for ind in l_profissionais:
        pro = getattr(ind, "nome")
        if nome_digitado == pro:
            print(pro)
    else:
        print("Profissional nao encontrado")
def registrar_visita():
    visitante_selecionado = str
    profissional_selecionado = str
    visitante_digitado = input("Qual o nome do VISITANTE que procuras?")
    for ind in l_visitantes:
        visitante = getattr(ind, "nome")
        if visitante == visitante_digitado:
            visitante_selecionado = visitante

    nome_digitado = input("Qual o nome do profissional que procuras?")
    for ind in l_profissionais:
        pro = getattr(ind, "nome")
        if pro == nome_digitado:
            profissional_selecionado = pro
    dia = date.today()
    visita = Visita(visitante_selecionado, profissional_selecionado, dia)
    dict_visitas[visitante_selecionado] = visita
    print(dict_visitas[visitante_selecionado])
def serializar_visita(visita):
    return {
        'visitante': visita.get_visitante(),
        'profissional': visita.get_profissional(),
        'data_entrada': visita.get_data_entrada().isoformat()
    }

def armazenar_registros():
    registros_serializados = {visitante: serializar_visita(visita) for visitante, visita in dict_visitas.items()}
    with open("registros.json", "w") as file:
        json.dump(registros_serializados, file, indent=4)
    print("Arquivo de registros criado")

l_profissionais = []
l_visitantes = []
pro_arq = []
dict_visitas = {}
while True:
    escolha =input("""======================
MENU
======================
1- Cadastrar Profissional 
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Gerar arquivo de Registros do dia
6- Ler arquivos profissionais / visitantes
0- Sair do loop
Escolha:""")
    if escolha == "1":
        add_profissional()
    if escolha == "2":
        add_visitantes()
    if escolha == "3":
        localizar()
    if escolha == "4":
        registrar_visita()
    if escolha == "5":
        pass#armazenar_registros()
    if escolha == "6":
        ler_profissionais()
        ler_visitantes()
    if escolha == "0":
        break