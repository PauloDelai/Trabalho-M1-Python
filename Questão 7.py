idade = int(input("Informe sua idade: "))
renda = float(input("Informe sua renda mensal: "))
dividas = float(input("Informe o valor total de suas dividas mensais: "))

porcentagemDivida = dividas * 100 / renda

if renda <= 2000 and porcentagemDivida >= 50:
    print("Seu nivel de risco é: Alto.")
elif renda <= 5000 and porcentagemDivida < 50 and porcentagemDivida >= 30:
    print("Seu nivel de risco é: Médio.")
elif renda > 5000 and porcentagemDivida < 30:
    print("Seu nivel de risco é: Baixo.")
else:
    print("Seu nivel de risco é: Baixo")