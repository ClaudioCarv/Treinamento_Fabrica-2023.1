valores = []
pares = []
impares = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort()

print("Valores pares em ordem crescente:", pares)
print("Valores ímpares em ordem crescente:", impares)
