def calcular_preco(distancia):
    if distancia <= 200:
        precco = distancia * 1.5
    else:
        precco = distancia * 1.25
    return precco

while True:
    try:
        distancia = float(input("Digite a distância da viagem em km: "))
        if distancia < 0:
            raise ValueError
        break
    except ValueError:
        print("Entrada inválida. Digite um número positivo.")

preco = calcular_preco(distancia)

print(f"O preço da passagem é R$ {preco:.2f}")
print("Obrigado por usar nosso programa de viagem da fábrica de software!")
