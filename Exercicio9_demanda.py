texto = input("Digite uma frase: ")

letras = "".join(c for c in texto if c.isalpha())

num_letras = len(letras)

print("Número de letras na frase:", num_letras)
