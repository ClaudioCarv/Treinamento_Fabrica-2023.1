jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")
num_partidas = int(input("Digite a quantidade de partidas jogadas: "))

gols_por_partida = []
total_gols = 0

for partida in range(1, num_partidas + 1):
    gols = int(input(f"Digite a quantidade de gols feitos na partida {partida}: "))
    gols_por_partida.append(gols)
    total_gols += gols

jogador['gols_por_partida'] = gols_por_partida
jogador['total_gols'] = total_gols

print("\nDados do jogador:")
for chave, valor in jogador.items():
    print(f"{chave}: {valor}")
