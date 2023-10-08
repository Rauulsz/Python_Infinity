from tkinter import *

janela = Tk()
janela.title("Cadastro de alunos")
janela.geometry("400x300")

label_nome = Label(text="Digite o nome").grid(row=0, column=0, padx=5)
entry_nome = Entry()
entry_nome.grid(row=0, column=1)

botao = Button(janela, text="Enviar", width=29)
botao.grid(row=1, column=0, columnspan=2, pady=10, padx=5)

janela.mainloop()