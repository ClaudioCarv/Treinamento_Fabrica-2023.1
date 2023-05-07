from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"Você tem {idade} anos. Ainda faltam {18 - idade} anos para você se alistar")
elif idade == 18:
    print(f"Você tem {idade} anos. Está na hora de se alistar!")
else:
    print(f"Você tem {idade} anos. Já passou o tempo de alistamento há {idade - 18} anos")
