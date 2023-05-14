numeros = []
while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    if numero == 0:
        break
    numeros.append(numero)

print(f"\nQuantidade de números digitados: {len(numeros)}")
print(f"Números digitados em ordem decrescente: {sorted(numeros, reverse=True)}")
if 5 in numeros:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
