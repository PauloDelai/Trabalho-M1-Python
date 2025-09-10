nacionalidade = (input("Informe sua nacionalidade: "))
idade = int (input ("Informe sua idade: ")) 

if nacionalidade == "Brasileiro" and idade >= 18 :
    print (f"Seu voto é obrigatório, por ser brasileiro e maior de 18 anos.")
elif nacionalidade == "Brasileiro" and idade < 18 and idade >= 16 :
    print (f"Seu voto é opcional, por ser brasileiro e idade {idade} anos.")
elif nacionalidade == "Brasileiro" and idade < 16 :
    print (f"Não pode votar, por não ter idade legal.")
elif nacionalidade != "Brasileiro" and idade >= 16 :
    print (f"Seu voto é opcional, por ser estrangeiro.")
elif nacionalidade != "Brasileiro" and idade < 16 :
    print (f"Não pode votar, por não ter idade legal.")