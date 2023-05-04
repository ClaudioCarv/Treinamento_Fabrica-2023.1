numero = float(input("Digite um número inteiro: "))

if not numero.is_integer():
    print("O número digitado não é inteiro")
else:
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
