nota1 = int(input("informe sua nota da primeira prova:\n"))
nota2 = int(input("informe sua nota da segunda prova:\n"))
nota3 = int(input("informe sua nota da terceira prova:\n"))

resultado = (nota1 + nota2 + nota3) / 3

if nota1 == 0 :
    print("voce reprovou na primeira nota")
    breakpoint
elif nota2 == 0 :
    print("voce reprovou na segunda nota")
    breakpoint
elif nota3 == 0 :
    print("voce reprovou na terceira nota5")
    breakpoint
elif resultado >= 7:
    print("voce foi aprovado, nota final:", resultado)
elif resultado >= 5:
    print("voce ficou em recuperacao, nota final:", resultado)
elif resultado < 5:
    print("voce reprovou, nota final:", resultado)