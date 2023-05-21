def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

resultado_soma = soma(a, b)
print("Soma:", resultado_soma)

resultado_subtracao = subtracao(a, b)
print("Subtração:", resultado_subtracao)

resultado_multiplicacao = multiplicacao(a, b)
print("Multiplicação:", resultado_multiplicacao)
