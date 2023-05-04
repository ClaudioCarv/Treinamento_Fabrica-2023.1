salario = float(input("Digite o seu salário: "))
despesas = float(input("Digite o total de despesas: "))

if despesas <= salario:
    print("Gastos dentro do orçamento.")
else:
    print("Gastos acima do orçamento.")
