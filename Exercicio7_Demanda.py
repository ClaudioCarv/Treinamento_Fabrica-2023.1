alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2, "media": media})

print("\nBOLETIM")

for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Nota 1: {aluno['nota1']}")
    print(f"Nota 2: {aluno['nota2']}")
    print(f"Média: {aluno['media']}")

while True:
    opcao = input("\nDigite o nome do aluno para ver as notas (ou 'sair' para encerrar): ")
    if opcao.lower() == "sair":
        break

    aluno_encontrado = False
    for aluno in alunos:
        if aluno['nome'] == opcao:
            print(f"\nNotas do(a) aluno(a) {opcao}:")
            print(f"Nota 1: {aluno['nota1']}")
            print(f"Nota 2: {aluno['nota2']}")
            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print("Aluno não encontrado!")
