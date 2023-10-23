class Cachorro:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

    def comer_racao(self):
        return f"O cachorro {self.nome} é da raça {self.raca}, pesa {self.peso} e come: croc croc croc"


cachorro1 = Cachorro(nome= "Bob", raca="bulldog", peso=15)
cachorro2 = Cachorro(nome= "Princesa", raca="Shi tzu", peso=5)

print(cachorro1.comer_racao())
print(cachorro2.comer_racao())
