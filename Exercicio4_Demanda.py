def notar(*notas, situacao=False):
    resultado = {}
    resultado['quantidade'] = len(notas)
    resultado['maior'] = max(notas)
    resultado['menor'] = min(notas)
    resultado['media'] = sum(notas) / len(notas)
    
    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'Aprovado'
        else:
            resultado['situacao'] = 'Reprovado'
    
    return resultado

turma = [7.5, 8.3, 6.9, 9.1, 5.7]
estatisticas = notar(*turma, situacao=True)

print("Quantidade de notas:", estatisticas['quantidade'])
print("Maior nota:", estatisticas['maior'])
print("Menor nota:", estatisticas['menor'])
print("Média da turma:", estatisticas['media'])

if 'situacao' in estatisticas:
    print("Situação da turma:", estatisticas['situacao'])
