from datetime import date

dados = {}

dados['nome'] = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
dados['idade'] = date.today().year - ano_nascimento
dados['ctps'] = int(input("Digite o número da Carteira de Trabalho (0 se não tiver): "))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input("Digite o ano de contratação: "))
    dados['salario'] = float(input("Digite o salário: "))
    idade_aposentadoria = dados['ano_contratacao'] - ano_nascimento + 35
    dados['idade_aposentadoria'] = idade_aposentadoria if idade_aposentadoria >= 0 else 0

print("\nDados cadastrados:")
for chave, valor in dados.items():
    print(f"{chave}: {valor}")
