nome = input("Digite o nome: ")
nac = float(input("Digite a NAC: "))
am = float(input("Digite a AM: "))
ps = float(input("Digite a ps: "))
fal = int(input("Digite o numero de faltas: "))

media = nac*0.2 + am*0.3 + ps*0.5

print ("A média do ", nome, " é: ", media)

if fal>=20:
    print("Reprovado por falta")
else:
    if media >=6:
        print("Aprovado")
    elif media<4:
        print("DP")
    else:
        print("Exame")

print("Até logo")