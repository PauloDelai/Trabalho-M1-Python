#Verifica se os lados formam um triângulo
def verifica_resultado(a, b, c):
    #Verifica se é um triângulo ou não
    if a + b > c and a + c > b and b + c > a:
        print("É um triângulo!")
        
        #Define tipo de triângulo
        if a == b == c:
            print("Tipo: Equilátero")
        elif a == b or a == c or b == c:
            print("Tipo: Isósceles")
        else:
            print("Tipo: Escaleno")
    else:
        print("Não é um triângulo.")

# recebe resposta do usuario
l1 = float(input("Digite o tamanho do primeiro lado: "))
l2 = float(input("Digite o tamanho do segundo lado: "))
l3 = float(input("Digite o tamanho do terceiro lado: "))

#Chama funçao 
verifica_resultado(l1, l2, l3)