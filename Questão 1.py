salario = float(input("Informe o valor de seu salario: "))
tempo = int(input("Informe o tempo de empresa: "))
bonus = 0

if salario < 2000 and tempo >= 5 :
    bonus = salario * 0.2
elif salario < 2000 and tempo < 5 :
    bonus = salario * 0.1
elif salario >= 2000 and tempo >= 5 :
    bonus = salario * 0.05
elif salario >= 2000 and tempo < 5 :
    bonus = 0

salario += bonus

print(f"Seu bonus é: {bonus}, e no total fica {salario}.")