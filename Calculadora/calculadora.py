from divisão import *
from multiplicação import *
from soma import *
from subtração import *
while True:
    escolha = int(input("""Bem vindo a calculadora, escolha o que deseja fazer ?
                        1 - Divisão
                        2 - Multiplicação
                        3 - Soma
                        4 - Subtração
                        0 - Encerrar 
                        """
                        ))

    if escolha == 1:
        divisão()

    elif escolha == 2:
        multiplicação()

    elif escolha == 3:
        soma()

    elif escolha == 4:
        subtração()

    elif escolha == 0:
        break
    else:
        print('Opção invalida')
