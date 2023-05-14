pessoas = []
mais_pesadas = []
mais_leves = []

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append({"nome": nome, "peso": peso})

quantidade_pessoas = len(pessoas)
print(f"\nForam cadastradas {quantidade_pessoas} pessoas.")

maior_peso = max(pessoas, key=lambda x: x["peso"])["peso"]
mais_pesadas = [pessoa for pessoa in pessoas if pessoa["peso"] == maior_peso]

menor_peso = min(pessoas, key=lambda x: x["peso"])["peso"]
mais_leves = [pessoa for pessoa in pessoas if pessoa["peso"] == menor_peso]

print("\nPessoas mais pesadas:")
for pessoa in mais_pesadas:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']}")

print("\nPessoas mais leves:")
for pessoa in mais_leves:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']}")
