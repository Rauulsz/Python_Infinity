from tkinter import *

def checagem():
    nota1 = int(nota1_entry.get())
    nota2 = int(nota2_entry.get())
    nota3 = int(nota3_entry.get())
    nota4 = int(nota4_entry.get())

    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 6:
        resultado.config(fg="green" , text=f"Parabéns {nome.get()} você foi aprovado e sua média foi {media}!")
    else:
        resultado.config(fg="red" , text=f"{nome.get()} você foi reprovado sua média foi {media}!")

janela = Tk()
janela.geometry("400x300")

nome = Label(text="Digite seu nome: ")
nome.pack()

nome = Entry()
nome.pack()

nota1_label = Label(text="Digite a primeira nota: ")
nota1_label.pack()

nota1_entry = Entry()
nota1_entry.pack()

nota2_label = Label(text="Digite a segunda nota: ")
nota2_label.pack()

nota2_entry = Entry()
nota2_entry.pack()

nota3_label = Label(text="Digite a terceira nota: ")
nota3_label.pack()

nota3_entry = Entry()
nota3_entry.pack()

nota4_label = Label(text="Digite a quarta nota: ")
nota4_label.pack()

nota4_entry = Entry()
nota4_entry.pack()

resultado = Label(text="")
resultado.pack()

botao_checar = Button(janela, text="Resultado", command=checagem)
botao_checar.pack()

janela.mainloop()