nome = input("Digite seu nome:")
print("É um prazer te conhecer, {}!".format(nome))

idade = int(input("Qual a sua idade?"))

if idade< 18:
    print("Você é menor de idade")
elif idade >= 18:
    print("Você é maior de idade")
