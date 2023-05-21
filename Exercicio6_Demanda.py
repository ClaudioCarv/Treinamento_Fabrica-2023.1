def ficha(nome='', gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    print(f"O jogador {nome} fez {gols} gol(s).")

nome_jogador = input("Digite o nome do jogador: ")
qtd_gols = input("Digite a quantidade de gols: ")

if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0

ficha(nome_jogador, qtd_gols)
