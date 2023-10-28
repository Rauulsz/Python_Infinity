class Veiculo:
    def __init__(self, nome_veiculo, quant_motores, tem_rodas):
        self.nome_veiculo = nome_veiculo
        self.quant_motores = quant_motores
        self.tem_rodas = tem_rodas
    
    def informacoes(self):
        return f"""
            Nome: {self.nome_veiculo}
            Quantidade de motores: {self.quant_motores}
            Possuir rodas: {self.tem_rodas}
        """

    def buzinar(self):
        return "Som indefinido"
    
class Carro(Veiculo):
    def __init__(self, quant_motores, tem_rodas):
        super().__init__(nome_veiculo="Carro", quant_motores=quant_motores, tem_rodas=tem_rodas)

    def buzinar(self):
        return "Biiii"
    
class Barco(Veiculo):
    def __init__(self, quant_motores, tem_rodas):
        super().__init__(nome_veiculo="Barco", quant_motores=quant_motores, tem_rodas=tem_rodas)

    def buzinar(self):
        return "Foooom"

class Aviao(Veiculo):
    def __init__(self, quant_motores, tem_rodas):
        super().__init__(nome_veiculo="Avião", quant_motores=quant_motores, tem_rodas=tem_rodas)

    def buzinar(self):
        return "Tem buzina?"

carro1 = Carro(quant_motores="1", tem_rodas="Sim")
barco1 = Barco(quant_motores="2", tem_rodas="Não")
aviao1 = Aviao(quant_motores="3", tem_rodas="Sim")

print(carro1.buzinar())
print(barco1.buzinar())
print(aviao1.buzinar())

print(carro1.informacoes())