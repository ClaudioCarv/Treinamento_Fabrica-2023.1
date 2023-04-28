frase = "treinamento hoje de backend"

# Captura as duas palavras do usuário
palavra_antiga = input("Digite a palavra que deseja substituir: ")
nova_palavra = input("Digite a nova palavra: ")

# Verifica se a palavra antiga está presente na frase
if palavra_antiga in frase:
    # Substitui a palavra antiga pela nova palavra na frase
    nova_frase = frase.replace(palavra_antiga, nova_palavra)
    # Imprime a nova frase com a palavra substituída
    print("Nova frase:", nova_frase)
else:
    print("Erro: a palavra que deseja substituir não foi encontrada na frase.")
