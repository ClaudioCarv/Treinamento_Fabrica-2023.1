numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

numero = int(input('Digite um número entre 0 e 10: '))

if numero < 0 or numero > 10:
    print('Número inválido. Digite um número entre 0 e 10.')
else:
    extenso = numeros_extenso[numero]
    print(f'O número {numero} por extenso é: {extenso}')
