import tkinter as tk
from tkinter import filedialog

def obter_chave(nome_arquivo):
    f = open(nome_arquivo, mode="r", encoding="utf-8")
    texto = f.read()
    return texto

def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'wb') as f:
        f.write(texto)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'rb') as f:
        return f.read()

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    caminho_arquivo = filedialog.askopenfilename()
    f = open(caminho_arquivo, mode="r", encoding="utf-8")
    return f.read()