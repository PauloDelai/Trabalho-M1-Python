resposta_correta = ['B', 'C', 'D', 'A']
resposta_usuario = input("Digite a sequência das cartas: ").upper()
pontos = 0

for i in range(4):
    if resposta_usuario[i] == resposta_correta[i]:
        pontos += 10
    if resposta_usuario[i] == 'A':
        pontos += 5

if "CD" in resposta_usuario:
    pontos += 5

if pontos > 50:
    pontos = 50

print (f"Sua pontuação foi: {pontos}")