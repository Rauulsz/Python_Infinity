import random

print("Bem-vindo ao jogo Pedra, Papel ou Tesoura ^-^")

npc = ["pedra", "papel" , "tesoura"]

def checar ():
    if escolha_do_npc == "pedra" and escolha_do_usuario == "pedra":
        print("Empate")
    elif escolha_do_npc == "pedra" and escolha_do_usuario == "tesoura":
        print("Você perdeu")
    elif escolha_do_npc == "pedra" and escolha_do_usuario == "papel":
        print("Você venceu")
    if escolha_do_npc == "papel" and escolha_do_usuario == "papel":
        print("Empate")
    elif escolha_do_npc == "papel" and escolha_do_usuario == "tesoura":
        print("Você venceu")
    elif escolha_do_npc == "papel" and escolha_do_usuario == "pedra":
        print("Você perdeu")
    if escolha_do_npc == "tesoura" and escolha_do_usuario == "tesoura":
        print("Empate")
    elif escolha_do_npc == "tesoura" and escolha_do_usuario == "papel":
        print("Você perdeu")
    elif escolha_do_npc == "tesoura" and escolha_do_usuario == "pedra":
        print("Você venceu")
 
    print(f"Nós escolhemos {escolha_do_npc} e você {escolha_do_usuario}.")
while True:
    menu = str(input("Deseja jogar ou sair? "))
    escolha_do_npc = random.choice(npc)
    if menu == "jogar":
        escolha_do_usuario = str(input("Você escolhe pedra, papel ou tesoura? "))
        checar()
    elif menu == "sair":    
        break
    else:
        print("Escolha inválida.")