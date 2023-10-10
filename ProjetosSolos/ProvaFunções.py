def calcular_media(notas):
    if len(notas) == 0:
        return 0
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


notas = []
while True:
    escolha_usuario = input("Digite uma nota ou escolha encerrar para fechar o programa: ")
    if escolha_usuario == "encerrar":
        break
    nota = float(escolha_usuario)
    if nota <= 10:
        notas.append(nota)
    else:
        print("Digite um nota de 0 a 10: ")

media = calcular_media(notas)
verificacao = verificar_situacao(media)

print(f"A média do aluno é: {media}")
print(f"Situação: {verificacao}")
