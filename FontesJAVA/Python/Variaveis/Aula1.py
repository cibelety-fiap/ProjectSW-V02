nome = input("Digite o nome: ")
nac = float(input("Digite a NAC: "))
am = float(input("Digite a AM: "))
ps = float(input("Digite a ps: "))
media = nac*0.2 + am*0.3 + ps*0.5
print ("A média do ", nome, " é: ", media)
if media >=6:
    print("Aprovado")
elif media<4:
    print("DP")
else:
    print("Exame")

print("Até logo")