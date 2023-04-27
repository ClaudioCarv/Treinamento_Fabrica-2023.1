ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2023

idade = ano_atual - ano_nasc

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

print("Sua idade é:", idade, "anos.")
