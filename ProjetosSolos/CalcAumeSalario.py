# Solicita o salário do colaborador ao usuário
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

# Calcula o aumento de acordo com as faixas salariais
if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

# Calcula o valor do aumento
aumento = (percentual_aumento / 100) * salario_atual

# Calcula o novo salário
novo_salario = salario_atual + aumento

# Exibe as informações
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")

