from tkinter import *

def saudacao():
    print(f"Seja Bem vindo {nome_entrada.get()}")
    nome_entrada.delete(0, END)

janela = Tk()

cinza = "#76777c"
preto = "#000000"

titulo = Label(text="Bem vindo",bg=cinza,fg=preto)
titulo.pack()

nome_texto = Label(text="Nome: ")
nome_texto.pack()

nome_entrada = Entry(bg=cinza,fg=preto, width=45)
nome_entrada.pack()

botao_enviar = Button(janela, text="Enviar", width=15, command=saudacao)
botao_enviar.pack()

janela.mainloop()