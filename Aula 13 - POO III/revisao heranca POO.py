class Funcionario():
    def __init__(self, nome=str, cpf=str, datanasc=str, cep=str):
        self.nome = nome
        self.cpf = cpf
        self.data = datanasc
        self.cep = cep

    def bateroponto(self):
        return f"Ponto registrado {self.nome}"

class Gerente(Funcionario):
    def __init__(self, nome, cpf, datanasc, cep, login, senha):
        super().__init__(nome, cpf, datanasc, cep)
        self.login = login
        self.senha = senha

    def admitir(self, novo_func):
        return f"Você foi admitido {novo_func}"
    
    def demitir(self, func_demitido):
        return f"Você foi demitido {func_demitido}"
    
class Coordenador(Funcionario):
    def __init__(self, nome, cpf, datanasc, cep):
        super().__init__(nome, cpf, datanasc, cep)

    def gerar_relatorio(self):
        return "Relatório gerado"

novo_coordenador = Coordenador(nome= "Bruno", cpf="020.020.015-00", datanasc="08/04/1982", cep="15680-00")


novo_gerente = Gerente(nome= "Mário", cpf="080.010.000-50", datanasc="05/03/1965", cep="14410-50", login="marinho", senha="123456")


novo_funcionario = Funcionario(nome="Raul", cpf="000.000.000-00", datanasc="07/05/2000", cep="00000-00")
print(novo_funcionario.bateroponto())

