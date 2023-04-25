while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")
