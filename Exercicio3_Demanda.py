valores = []

while True:
    numero = int(input("Digite um valor (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    if numero not in valores:
        valores.append(numero)

valores.sort()

print("Valores únicos digitados (em ordem crescente):")
for valor in valores:
    print(valor)
