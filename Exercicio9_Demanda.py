alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    media = float(input("Digite a média do aluno: "))
    alunos[nome] = media

print("Dados dos alunos:")
for nome, media in alunos.items():
    print(f"Nome: {nome} | Média: {media}")
