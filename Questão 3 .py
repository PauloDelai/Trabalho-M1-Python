peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc}")

if imc < 18.5:
    print("Seu peso está abaixo do ideal")
elif imc < 24.9:
    print("Você está com o peso ideal")
elif imc < 29.9:
    print("Você está com sobrepeso")
elif imc < 34.9:
    print("Você está com obsidade grau I")
elif imc < 39.9:
    print("Você está com obsidade grau II")
elif imc >= 40:
    print("Você está com obsidade grau III")