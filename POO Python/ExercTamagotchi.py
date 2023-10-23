class Tamagotchi:
    def __init__(self, nome=str, saude=int, energia=int):
        self.nome = nome
        self.saude = saude
        self.energia = energia

    def brincar(self):
        self.energia = self.energia - 10
        return self.energia
    
    def lutar(self):
        self.energia = self.energia - 20
        return self.energia
    
    def comer(self):
        self.energia = self.energia + 10
        return self.energia
    
    def descansar(self):
        self.energia = self.energia + 20
        return self.energia

nome = str(input("Digite o nome do seu Tamagotchi: "))
energiainicial = int(input("Digite a energia inicial do seu Tamagotchi: "))
saudeinicial = int(input("Digite a saúde inicial do seu Tamagotchi: "))
play1 = Tamagotchi(nome=nome, saude=saudeinicial, energia=energiainicial)

while True:
    menu = int(input(f"""
            Bem vindo {play1.nome}
            Saúde inicial {play1.saude}
            Energia inicial {play1.energia}
            
            1 - Brincar
            2 - Lutar
            3 - Comer
            4 - Descansar
            0 - Sair
    """))

    if menu == 1:
        print(play1.brincar())
    elif menu == 2:
        play1.lutar()
    elif menu == 3:
        play1.comer()
    elif menu == 4:
        play1.descansar()
    elif menu == 0:
        break
    else:
        print("Opção inválida")