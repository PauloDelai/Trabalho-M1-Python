senha = (input("Mínimo de 8 caractéres\nContém pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 dos seguintes símbolos: !@#$%.\n\nInsira sua senha: "))

if len (senha) >= 8 and any(n.isupper() for n in senha) and any(n.islower() for n in senha) and any(n.isdigit() for n in senha) and any(n in "!@#$%" for n in senha) :
    print (f"Senha: {senha}\nÉ válida.")
else :
    print (f"Senha: {senha}\nInválida.")