class Jogador:
    def __init__(self, nome, equipe):
        self.nome = nome
        self.equipe = equipe
        self.pontuacao = 0

    def marcar_gol(self):
        self.pontuacao += 1

    def imprimir_pontuacao(self):
        print(f"O jogador {self.nome} da equipe {self.equipe} tem uma pontuação de {self.pontuacao} gol(s).")



jogador1 = Jogador("João", "Flamengo")
jogador2 = Jogador("Pedro", "Palmeiras")

jogador1.marcar_gol()
jogador1.marcar_gol()
jogador2.marcar_gol()

jogador1.imprimir_pontuacao()
jogador2.imprimir_pontuacao()
