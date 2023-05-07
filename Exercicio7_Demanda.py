import random

numero = random.randint(0, 10)

tentativas = 0

while True:
    palpite = int(input("Digite um número entre 0 e 10: "))
    tentativas += 1
    
    if palpite == numero:
        print(f"Parabéns, você acertou em {tentativas} tentativas!")
        break
    elif palpite < numero:
        print("O número é maior, tente novamente.")
    else:
        print("O número é menor, tente novamente.")
