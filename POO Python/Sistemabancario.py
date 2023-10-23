class sistemabancario:
    def __init__(self, identnumero, nome, saldo):
        self.identnumero = identnumero
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo = self.saldo + valor

class Contacorrente(sistemabancario):
    def __init__(self, identnumero, nome, saldo):
        super().__init__(identnumero, nome, saldo)

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        return self.saldo
        
class Contapoupanca(sistemabancario):
    def __init__(self, identnumero, nome, saldo, juros):
        super().__init__(identnumero, nome, saldo)
        self.juros = juros