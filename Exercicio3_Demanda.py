palavras = ('python', 'programacao', 'computador', 'desenvolvimento')

for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    print(f'Vogais da palavra "{palavra}": {", ".join(vogais)}')
