import random

quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

jogos = []

for _ in range(quantidade_jogos):
    jogo = []
    for _ in range(5):
        numero = random.randint(1, 50)
        jogo.append(numero)
    jogos.append(jogo)

print("Palpites gerados:")
for jogo in jogos:
    print(jogo)
