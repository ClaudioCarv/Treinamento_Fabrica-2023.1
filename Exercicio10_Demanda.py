import random

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ''
    
    while tipo != 'P' and tipo != 'I':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}. ', end='')
    print('Deu PAR.' if total % 2 == 0 else 'Deu ÍMPAR.')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!\n')
            vitorias += 1
        else:
            print('Você PERDEU!\n')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!\n')
            vitorias += 1
        else:
            print('Você PERDEU!\n')
            break

print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')
