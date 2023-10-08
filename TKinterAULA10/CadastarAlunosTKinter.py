from tkinter import *

lista_alunos = []

def cadastro():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    nota = float(nota_entry.get())
    lista_alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print(lista_alunos)


janela = Tk()
janela.geometry("300x200")

titulo = Label(text="Cadatro de Alunos").pack()

nome = Label(text="Digite seu nome: ").pack()

nome_entry = Entry()
nome_entry.pack()

idade = Label(text="Digite sua idade: ").pack()

idade_entry = Entry()
idade_entry.pack()

nota = Label(text="Digite sua nota: ").pack()

nota_entry = Entry()
nota_entry.pack()

botao_cadastrar = Button(janela, text="Cadastrar", command=cadastro)
botao_cadastrar.pack()

janela.mainloop()