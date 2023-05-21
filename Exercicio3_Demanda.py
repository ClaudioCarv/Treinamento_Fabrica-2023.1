def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(f'  {texto}')
    print('-' * tamanho)

mensagem = input('Digite um texto: ')
escreva(mensagem)
