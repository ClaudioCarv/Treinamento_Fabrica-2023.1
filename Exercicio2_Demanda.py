numeros = []
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)
