import random

jogadores = {}
for i in range(4):
    jogador = input(f"Digite o nome do jogador {i+1}: ")
    resultado = random.randint(1, 6)
    jogadores[jogador] = resultado

print("Resultados:")
for jogador, resultado in jogadores.items():
    print(f"{jogador}: {resultado}")

vencedor = max(jogadores, key=jogadores.get)
print(f"\nVencedor: {vencedor}")
