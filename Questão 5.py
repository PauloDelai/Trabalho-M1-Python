dia = int(input("Informe o dia: ")) 
mes = int(input("Informe o mês: ")) 
ano = int(input("Informe o ano: "))

if ano < 0:
    print("Esse ano não existe.")
else:
    if mes < 1 or mes > 12:
        print("Esse mês não existe.")
    else:
        if mes == 2:
            if ano % 4 == 0 or (ano % 400 == 0 and ano % 100 == 0 ):
                if dia < 1 or dia > 29:
                    print("Esse dia não existe.")
                else:
                    print("Essa data existe.")   
            else:
                if dia < 1 or dia > 29:
                    print("Esse dia não existe.")
                elif dia == 29:
                    print("Esse mês possui apenas 28 dias, pois esse não é um ano bissexto.")
                else:
                    print("Essa data existe.")
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia < 1 or dia > 31:
                print("Esse dia não existe.")
            else:
                print("Essa data existe.")
        else:
            if dia < 1 or dia > 31:
                print("Esse dia não existe.")
            elif dia == 31:
                print("Esse mês possui apenas 30 dias.")
            else:
                print("Essa data existe.")