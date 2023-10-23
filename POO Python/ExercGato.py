class Gato:
    def __init__(self, nome):
        self.nome = nome

    def derrubar_coisas(self):
        return f"A Gata {self.nome} quebrou algo."

gato1 = Gato(nome= "Nina")

print(gato1.derrubar_coisas())
