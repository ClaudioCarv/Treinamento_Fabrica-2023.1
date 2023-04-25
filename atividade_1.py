#variáveis#
n1 = (input('Digite o primeiro numero: '))
n2 = (input('Digite o segundo numero: '))

#operações#
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2

print('Escolha uma das operações abaixo\n')
print(' 1-Soma\n 2-Subtração \n 3-Multiplicação \n 4-Divisão')

escolha = (input('escolha:'))

#ifs e elifs#
if escolha == 1:
    
    print('a soma entre {} e {} é igual a {}' . format (n1, n2, soma))

elif escolha == 2:
    
    print('a soma entre {} e {} é igual a {}' . format (n1, n2, sub))

elif escolha == 3:
    
    print('a soma entre {} e {} é igual a {}' . format (n1, n2, multi))

elif escolha == 4:
    
    print('a soma entre {} e {} é igual a {}' . format (n1, n2, div))