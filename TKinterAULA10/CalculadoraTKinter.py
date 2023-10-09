from tkinter import *

numero1 = ""
numero2 = ""
operacao = ""
resultado = 0

def calcular():
    global resultado
    global numero1
    global numero2
    global operacao

    numero1_sem_espaco = numero1.strip()
    numero1_float = float(numero1_sem_espaco)

    numero2_sem_espaco = numero2.strip()
    numero2_float = float(numero2_sem_espaco)

    if operacao == "/":
        resultado = numero1_float / numero2_float
    elif operacao == "*":
        resultado = numero1_float * numero2_float
    elif operacao == "+":
        resultado = numero1_float + numero2_float
    elif operacao == "-":
        resultado = numero1_float - numero2_float
    elif operacao == "C":
        resultado == 0
    resultado_tela.config(text=resultado)

def registrar_operacao(op):
    global operacao

    operacao = op
    resultado_tela.config(text=f"{numero1}{operacao}")

def registrar_numero(numero):
    global numero1
    global numero2
    global operacao

    if operacao == "":
        numero1 = f"{numero1}{numero}"
        resultado_tela.config(text=numero1)
    else:
        numero2 = f"{numero2}{numero}"
        resultado_tela.config(text=f"{numero1}{operacao}{numero2}")


janela = Tk()
janela.geometry("325x245")
janela.title("CALCULADORA")
resultado_tela = Label(text="", height=2, bg="#7b7672",fg="#fffbf4", width=40, font=('Ivy 10 bold'))
resultado_tela.grid(row=0, column=0, columnspan=4)

b1 = Button(janela,bg="#7b7672",fg="#fffbf4", text="1", width=10, height=2, command=lambda : registrar_numero("1"))
b1.grid(row=3, column=0)

b2 = Button(janela,bg="#7b7672",fg="#fffbf4", text="2",width=10, height=2, command=lambda : registrar_numero("2"))
b2.grid(row=3, column=1)

b3 = Button(janela,bg="#7b7672",fg="#fffbf4", text="3",width=10, height=2, command=lambda : registrar_numero("3"))
b3.grid(row=3, column=2)

b4 = Button(janela,bg="#7b7672",fg="#fffbf4", text="4",width=10, height=2, command=lambda : registrar_numero("4"))
b4.grid(row=2, column=0)

b5 = Button(janela,bg="#7b7672",fg="#fffbf4", text="5",width=10, height=2, command=lambda : registrar_numero("5"))
b5.grid(row=2, column=1)

b6 = Button(janela,bg="#7b7672",fg="#fffbf4", text="6",width=10, height=2, command=lambda : registrar_numero("6"))
b6.grid(row=2, column=2)

b7 = Button(janela,bg="#7b7672",fg="#fffbf4", text="7",width=10, height=2, command=lambda : registrar_numero("7"))
b7.grid(row=1, column=0)

b8 = Button(janela,bg="#7b7672",fg="#fffbf4", text="8",width=10, height=2, command=lambda : registrar_numero("8"))
b8.grid(row=1, column=1)

b9 = Button(janela,bg="#7b7672",fg="#fffbf4", text="9",width=10, height=2, command=lambda : registrar_numero("9"))
b9.grid(row=1, column=2)

b0 = Button(janela,bg="#7b7672",fg="#fffbf4", text="0",width=33, height=2, command=lambda : registrar_numero("0"))
b0.grid(row=4, column=0, columnspan=3)

bsomar = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="+",width=10, height=2, command= lambda : registrar_operacao("+"))
bsomar.grid(row=1, column=3)

bsubtrair = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="-",width=10, height=2, command= lambda : registrar_operacao("-"))
bsubtrair.grid(row=2, column=3)

bmultiplicar = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="*",width=10, height=2, command= lambda : registrar_operacao("*"))
bmultiplicar.grid(row=3, column=3)

bdividir = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="/",width=10, height=2, command= lambda : registrar_operacao("/"))
bdividir.grid(row=4, column=3)

bresultado = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="=",width=10, height=2, command= calcular)
bresultado.grid(row=5, column=3)

bclear = Button(janela,bg="#ff8f2c", fg="#fffbf4", text="C",width=20, height=2, command= calcular)
bclear.grid(row=5, column=0, columnspan=3)

janela.mainloop()
