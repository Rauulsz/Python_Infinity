from tkinter import *

def checagem():
    numero1 = int(numero1_entry.get())
    numero2 = int(numero2_entry.get())

    if numero1 > numero2:
        resultado.config(bg="green", text= f"O número {numero1} é o maior")
    else:
        resultado.config(bg="red", text= f"O número {numero2} é o maior")


janela = Tk()

titulo = Label(text="Maior dos dois")
titulo.pack()

numero1_label = Label(text="Digite o primeiro número: ")
numero1_label.pack()

numero1_entry = Entry()
numero1_entry.pack()

numero2_label = Label(text="Digite o segundo número: ")
numero2_label.pack()

numero2_entry = Entry()
numero2_entry.pack()

resultado = Label(text="")
resultado.pack()

botao_checar = Button(janela, text="Checando", command=checagem)
botao_checar.pack()


janela.mainloop()