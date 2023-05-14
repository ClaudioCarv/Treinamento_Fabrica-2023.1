numeros = []
pares = []
impares = []

while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    if numero == 0:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nNúmeros digitados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
