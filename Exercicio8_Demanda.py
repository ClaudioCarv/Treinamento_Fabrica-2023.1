continuar = 's'
soma = contador = 0
maior = menor = None

while continuar == 's':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    contador += 1
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    continuar = input('Deseja continuar digitando? (s/n)').lower()

media = soma / contador

print(f'A média dos números digitados é {media:.2f}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
