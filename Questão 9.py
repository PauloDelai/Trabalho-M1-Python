preco = float(input("Informe o preço do produto: "))
vip = bool(input("Você é um cliente VIP? "))
desconto = 0
descontoVIP = 0
teste = 0

if preco < 50:
    teste = 1
elif preco < 100:
    desconto = preco * 0.1
elif preco >= 100:
    desconto = preco * 0.2

if vip == True:
    descontoVIP = preco * 0.05

preco -= desconto
preco -= descontoVIP

print(f"Seu disconto foi de {desconto + descontoVIP}\nO valor final de seu produto ficou: {preco}")