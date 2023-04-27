salario = float(input("Digite o valor do salário recebido: "))
gastos = float(input("Digite o valor total de gastos em despesas: "))

if gastos <= salario:
    print("Gastos dentro do orçamento.")
else:
    print("Gastos fora do orçamento.")
