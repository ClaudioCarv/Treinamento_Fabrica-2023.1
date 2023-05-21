def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    if passo > 0:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    elif passo < 0:
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
    print()


contador(1, 10, 1)


contador(10, 0, -2)

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))
contador(inicio, fim, passo)
