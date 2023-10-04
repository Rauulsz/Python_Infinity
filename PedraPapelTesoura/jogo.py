import random

print("Bem-vindo ao jogo Pedra, Papel ou Tesoura ^-^")

npc = ["pedra", "papel" , "tesoura"]

cont_npc = 0
cont_usuario = 0
empate = 0

def checar ():
    global cont_npc
    global cont_usuario
    global empate
    if escolha_do_npc == "pedra" and escolha_do_usuario == "pedra":
        empate += 1
        print("Empate")
    elif escolha_do_npc == "pedra" and escolha_do_usuario == "tesoura":
        cont_npc += 1
        print("Você perdeu")
    elif escolha_do_npc == "pedra" and escolha_do_usuario == "papel":
        cont_usuario += 1
        print("Você venceu")
    if escolha_do_npc == "papel" and escolha_do_usuario == "papel":
        empate += 1
        print("Empate")
    elif escolha_do_npc == "papel" and escolha_do_usuario == "tesoura":
        cont_usuario += 1
        print("Você venceu")
    elif escolha_do_npc == "papel" and escolha_do_usuario == "pedra":
        cont_npc += 1
        print("Você perdeu")
    if escolha_do_npc == "tesoura" and escolha_do_usuario == "tesoura":
        empate += 1
        print("Empate")
    elif escolha_do_npc == "tesoura" and escolha_do_usuario == "papel":
        cont_npc += 1
        print("Você perdeu")
    elif escolha_do_npc == "tesoura" and escolha_do_usuario == "pedra":
        cont_usuario += 1
        print("Você venceu")
 
    print(f"Nós escolhemos {escolha_do_npc} e você {escolha_do_usuario}.")

while True:
    menu = int(input("""
    Deseja uma das opções abaixo: 
    1 - Jogar                
    2 - Ver placar
    3 - Sair                                 
    
    """))
    escolha_do_npc = random.choice(npc)
    if menu == 1:
        escolha_do_usuario = str(input("Você escolhe pedra, papel ou tesoura? "))
        checar()
    elif menu == 2:    
        print(f"""
    PC: {cont_npc}
    USÚARIO: {cont_usuario}
    EMPATE: {empate}
""")
    elif menu == 3:    
        break
    else:
        print("Escolha inválida.")