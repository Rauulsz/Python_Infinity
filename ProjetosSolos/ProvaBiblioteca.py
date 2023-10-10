alunos = {}

while True:
    menu = int(input("""
Digite uma das opções abaixo:
1 - Adicionar um novo aluno.
2 - Remover um aluno.
3 - Vizualizar todos os alunos.
4 - Sair

"""))
    if menu == 1:
        nome = input("Digite o nome do novo aluno: ")
        matricula = input("Digite a Matricula do novo aluno: ")
        alunos[matricula] = nome
        print(f"Aluno {nome} matriculado.")
    elif menu == 2:
        matricula = input("Digite o número de matrícula do aluno que será removido: ")
        if matricula in alunos:
            nome = alunos.pop(matricula)
            print(f"Aluno '{nome}' removido!")
        else:
            print("Aluno não encontrado")   
    elif menu == 3:
        print(f"""
            Segue lista de alunos:
            {alunos}
""")
    elif menu == 4:
        break
    else:
        print("Você digitou uma opção inválida")
    
    