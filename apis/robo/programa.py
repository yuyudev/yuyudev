from distutils.command.upload import upload
import string
from tkinter import filedialog
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tratamento_banqi
import tratamento_privalia
import tratadados


janela = Tk()
janela.title("Tratamento dos dados de ASO")
janela.geometry("500x300")


listaClientes = ["BanQi", "Privalia"]

lb_clientes = Label(janela, text="Selecione o cliente:")
lb_clientes.pack()

cb_clientes = ttk.Combobox(janela, values=listaClientes)
cb_clientes.set("BanQi")
cb_clientes.pack()



lb_periodo = Label(janela, text="Selecione o período dos dados:")
lb_periodo.pack()



lb_inicio = Label(janela, text="Início: ")
lb_inicio.pack()
dataInicial = Entry(janela, width=10)
dataInicial.pack()



lb_final = Label(janela, text="Final: ")
lb_final.pack()
dataFinal = Entry(janela, width=10)
dataFinal.pack()


def trataDados():
    if listaClientes[0]:
        tratar_banqi()
    elif listaClientes[1]:
        tratar_privalia()
def lerArquivo():
    arquivo = filedialog.askopenfile(mode="r", initialdir="/Desktop", title="Selecione um arquivo", filetypes=(("Arquivos CSV", "*.csv")))
    conteudo = arquivo.read()

df = pd.read_csv(lerArquivo(), encoding = "UTF-8", sep = ",")

def tratar_banqi():
    df
    datas = df.T[string(dataInicial):string(dataFinal)]
    termos = df["Term"]
    posicoes = df.T[string(dataInicial):string(dataFinal)]
    x = posicoes.to_numpy()

    #seleção dos dados de datas

    datas.reset_index(inplace=True)
    datas = datas["index"]

    colunaTermos = column = termos
    colunaDatas = column = datas


    #tratamento dos dados

    dados = []
    chave = []

    for i in x:
        for y in i:
            chave.append(y)
    i = 0
    j = 0

    for data in datas:
        for termo in termos:      
            dados.append((data,termo,chave[i]))
            i = i + 1
        

    base = pd.DataFrame(dados, columns = ["datas", "termos", "posição"])
    base.to_csv("nova_base.csv")
def tratar_privalia():
    df
    datas = df.T[string(dataInicial):string(dataFinal)]
    termos = df["Term"]
    appId = df["App ID"].values
    posicoes = df.T[string(dataInicial):string(dataFinal)]
    x = posicoes.to_numpy()

    #seleção dos dados de datas

    datas.reset_index(inplace=True)
    datas = datas["index"]

    colunaTermos = column = termos
    colunaAppID = column = appId
    colunaDatas = column = datas


    #tratamento dos dados

    dados = []
    chave = []

    for i in x:
        for y in i:
            chave.append(y)
    i = 0
    j = 0

    for data in datas:
        for termo in termos:      
            dados.append((data,termo,appId[j],chave[i]))
            j = j + 1
            i = i + 1
        j=0
        


    base = pd.DataFrame(dados, columns = ["datas", "termos", "id", "posição"])
    base.to_csv("nova_base.csv")


up_arquivo = Button(janela, text="Selecione o arquivo", width=5, height=1, background="lightgreen", command=(lerArquivo))

botao = Button(janela, text="Go!", width=5, height=1, background="lightblue", command=trataDados())
botao.pack()


janela.mainloop()