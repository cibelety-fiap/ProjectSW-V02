nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))

if idade<16:
    print("Você não é obrigado a votar")
elif idade>=16 and idade<=17 or idade>65:
    print("Se você quiser votar, fique a vonts")
else:
    print(nome,", você é obrigado a votar")
