class Cadastrodotime:
   def __init__(self, nome_time=str, cidade_time=str, mascote_time=str):
    self.__nome_time = nome_time
    self.__cidade_time = cidade_time
    self.__mascote_time = mascote_time

    def getNome(self):
        return self.__nome_time

    def setNome(self, novo_nome=str):
        self.__nome_time = novo_nome
        return self.__nome_time

    def getCidade(self):
        return self.__cidade_time

    def setCidade(self, nova_cidade=str):
        self.__cidade_time = nova_cidade
        return self.__cidade_time
    
    def getMascote(self):
        return self.__mascote_time

    def setMascote(self, novo_mascote=str):
        self.__mascote_time = novo_mascote
        return self.__mascote_time

class Cadastrodojogador:
    def __init__(self, nome_jogador=str, time_atual=str, numero_camisa=int):
        self.__nome_jogador = nome_jogador
        self.__time_atual = time_atual
        self.__numero_camisa = numero_camisa

    def getNome(self):
        return self.__nome_jogador

    def setNome(self, novo_jogador=str):
        self.__nome_jogador = novo_jogador
        return self.__nome_jogador

    def getTime(self):
        return self.__time_atual

    def setTime(self, novo_time=str):
        self.__time_atual = novo_time
        return self.__time_atual
    
    def getNumerocamisa(self):
        return self.__numero_camisa

    def setNumerocamisa(self, nova_camisa=int):
        self.__numero_camisa = nova_camisa
        return self.__numero_camisa

class Cadastrocomissaotec:
    def __init__(self, tecnico=str, auxiliar=str, preparador_fisico=str):
        self.__tecnico = tecnico
        self.__auxiliar = auxiliar
        self.__preparador_fisico = preparador_fisico

    def getTecnico(self):
        return self.__tecnico
    
    def setTecnico(self, novo_tecnico=str):
        self.__tecnico = novo_tecnico
        return self.__tecnico

    def getAuxiliar(self):
        return self.__auxiliar
    
    def setAuxiliar(self, novo_auxiliar=str):
        self.__auxiliar = novo_auxiliar
        return self.__auxiliar

    def getPreparador_fisico(self):
        return self.__preparador_fisico
    
    def setPreparador_fisico(self, novo_preparador_fisico=str):
        self.__preparador_fisico = novo_preparador_fisico
        return self.__preparador_fisico

class Tecnico:
    def __init__(self, nome=str, time=str, esquema_tatico=str):
        self.__nome = nome
        self.__time = time
        self.__esquema_tatico = esquema_tatico

    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_nome=str):
        self.__nome = novo_nome
        return self.__nome

    def getTime(self):
        return self.__time
    
    def setTime(self, novo_time=str):
        self.__time = novo_time
        return self.__time

    def getEsquema_tatico(self):
        return self.__esquema_tatico
    
    def setEsquema_tatico(self, novo_esquema_tatico=str):
        self.__esquema_tatico = novo_esquema_tatico
        return self.__esquema_tatico

    def dar_coletiva(self):
        return f"O técnico {self.getNome()} está dando uma coletiva de imprensa."

class Auxiliar(Tecnico):
    def __init__(self, nome=str, time=str, esquema_tatico=str):
        super().__init__(nome, time, esquema_tatico)

    def dar_coletiva(self):
        return f"O auxiliar {self.getNome()} está dando uma coletiva de imprensa."

class PreparadorFisico(Tecnico):
    def __init__(self, nome=str, time=str, elenco_de_treino=str):
        super().__init__(nome, time)

        self.__elenco_de_treino = elenco_de_treino

    def getElenco_de_treino(self):
        return self.__elenco_de_treino
    
    def setElenco_de_treino(self, novo_elenco_de_treino=str):
        self.__elenco_de_treino = novo_elenco_de_treino
        return self.__elenco_de_treino
    
    def dar_coletiva(self):
        return f"O preparado físico {self.getNome()} está dando uma coletiva de imprensa."



while True:
    escolha = int(input("""
        Escolha uma opção :
        1 - Cadastrar um time
        2 - Cadastrar um jogador
        3 - Cadastrar a comissão técnica
        0 - Sair do programa
"""))
    match escolha:
        case 1 :
            nome = str(input("Digite o nome do time: "))
            cidade = str(input("Digite a cidade do time: "))
            mascote = str(input("Digite o nome do mascote: "))
            time = Cadastrodotime(nome_time=nome, cidade_time=cidade, mascote_time=mascote)

        case 2 :
            nome_jogador = str(input("Digite o nome do jogador: "))
            time_atual = str(input("Digite o nome do time atual: "))
            numero_camisa = int(input("Digite o número da camisa: "))
            jogador = Cadastrodojogador(nome_jogador=nome_jogador, time_atual=time_atual, numero_camisa=numero_camisa)

        case 3 :
            nome_tecnico = str(input("Digite o nome do técnico: "))
            time_tecnico = str(input("Digite o time do técnico: "))
            esquema_tecnico = str(input("Digite o esquema preferido do técnico: "))
            tecnico = Tecnico(nome=nome_tecnico, time=time_tecnico, esquema_tatico=esquema_tecnico)

            nome_auxiliar = str(input("Digite o nome do auxiliar: "))
            time_auxiliar = str(input("Digite o time do auxiliar: "))
            esquema_auxiliar = str(input("Digite o esquema preferido do auxiliar: "))
            auxiliar = Auxiliar(nome=nome_auxiliar, time=time_auxiliar, esquema_tatico=esquema_auxiliar)

            nome_preparador_fisico = str(input("Digite o nome do preparador_fisico: "))
            time_preparador_fisico = str(input("Digite o time do preparador_fisico: "))
            esquema_preparador_fisico = str(input("Digite o esquema preferido do preparador_fisico: "))
            preparador_fisico = PreparadorFisico(nome=nome_preparador_fisico, time=time_preparador_fisico, elenco_de_treino=esquema_preparador_fisico)


            Cadastrocomissaotec(tecnico=tecnico, auxiliar=auxiliar, preparador_fisico=preparador_fisico)
        
        case 0:
            break