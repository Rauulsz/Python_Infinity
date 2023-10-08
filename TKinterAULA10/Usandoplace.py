from tkinter import *

janela = Tk()
janela.title("Cadastro de alunos")
janela.geometry("400x300")

label_nome = Label(text="Digite o nome").place(x=5, y=10)
entry_nome = Entry()
entry_nome.place(x=90, y=10)

botao = Button(janela, text="Enviar", width=29)
botao.place(x=5,y=38)

janela.mainloop()