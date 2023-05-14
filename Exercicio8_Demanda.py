import random

jogadores = {}

for i in range(1, 5):
    jogador = input(f"Digite o nome do jogador {i}: ")
    resultado = random.randint(1, 6)
    jogadores[jogador] = resultado

jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("\nRESULTADO DO JOGO:")
for jogador, resultado in jogadores_ordenados:
    print(f"{jogador}: {resultado}")

vencedor = jogadores_ordenados[0][0]
print(f"\nO vencedor é: {vencedor}")
